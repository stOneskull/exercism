import json
from dataclasses import dataclass, asdict



@dataclass
class User:
    name: str
    owes: dict
    owed_by: dict
    balance: float

    def _update_debt(self, other, amount):
        self.owes[other.name] = self.owes.get(other.name, 0) + amount
        other.owed_by[self.name] = other.owed_by.get(self.name, 0) + amount

    def borrow_from(self, lender, amount):
        self.balance -= amount
        lender.balance += amount

        debt_from_lender = lender.owes.get(self.name, 0)
        
        if debt_from_lender > 0:
            settle_amount = min(debt_from_lender, amount)
            lender.owes[self.name] -= settle_amount
            self.owed_by[lender.name] -= settle_amount
            amount -= settle_amount

        if amount > 0:
            self._update_debt(lender, amount)



class RestAPI:
    def __init__(self, database=None):       
        self.users = [User(**user) for user in database['users']]
        self._user_map = {user.name: user for user in self.users}

    def get(self, url='/users', payload=None):
        if payload:
            users_to_return = [
                asdict(self._user_map[name]) 
                for name in json.loads(payload)["users"]]
        else:
            users_to_return = [asdict(user) for user in self.users]
        
        return json.dumps({"users": users_to_return})
            

    def post(self, url, payload=None):
        data = json.loads(payload)

        if url == "/add":
            name = data["user"]
            new_user = User(name=name, owes={}, owed_by={}, balance=0.0)
            self.users.append(new_user)
            self._user_map[name] = new_user
            return json.dumps(asdict(new_user))
        
        if url == "/iou":
            lender = self._user_map[data["lender"]]
            borrower = self._user_map[data["borrower"]]
            amount = data["amount"]

            borrower.borrow_from(lender, amount)

            self._cleanup_debts(lender, borrower)

            response_users = sorted([lender, borrower], key=lambda u: u.name)
            return json.dumps({"users": [asdict(u) for u in response_users]})

    def _cleanup_debts(self, *users):
        for user in users:
            user.owes = {k: v for k, v in user.owes.items() if v > 0}
            user.owed_by = {k: v for k, v in user.owed_by.items() if v > 0}