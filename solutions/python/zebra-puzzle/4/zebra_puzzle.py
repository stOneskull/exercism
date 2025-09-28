from itertools import permutations


def solve_puzzle():
    houses = range(1, 6)
    orderings = list(permutations(houses))

    for (red, green, ivory, yellow, blue) in orderings:
        if green != ivory + 1:
            continue

        for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings:
            if Englishman != red:
                continue
            if Norwegian != 1:
                continue
            if abs(Norwegian - blue) != 1:
                continue

            for (coffee, tea, milk, oj, water) in orderings:
                if coffee != green:
                    continue
                if Ukrainian != tea:
                    continue
                if milk != 3:
                    continue

                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments
                ) in orderings:
                    if Kools != yellow:
                        continue
                    if LuckyStrike != oj:
                        continue
                    if Japanese != Parliaments:
                        continue

                    for (fox, horse, snails, dog, zebra) in orderings:
                        if Spaniard != dog:
                            continue
                        if OldGold != snails:
                            continue
                        if abs(Chesterfields - fox) != 1:
                            continue
                        if abs(Kools - horse) != 1:
                            continue

                        return {
                            "red": red, "green": green, "ivory": ivory, 
                            "yellow": yellow, "blue": blue, 
                            "Englishman": Englishman, "Spaniard": Spaniard, 
                            "Ukrainian": Ukrainian, "Japanese": Japanese, 
                            "Norwegian": Norwegian,
                            "coffee": coffee, "tea": tea, "milk": milk, 
                            "orange juice": oj, "water": water,
                            "Old Gold": OldGold, "Kools": Kools, 
                            "Chesterfields": Chesterfields, 
                            "Lucky Strike": LuckyStrike, 
                            "Parliaments": Parliaments,
                            "fox": fox, "horse": horse, "snails": snails, 
                            "dog": dog, "zebra": zebra,
                        }


solution = solve_puzzle()

people = ("Norwegian", "Ukrainian", "Englishman", "Spaniard", "Japanese")


def drinks_water():
    for person in people:
        if solution[person] == solution["water"]:
            return person


def owns_zebra():
    for person in people:
        if solution[person] == solution["zebra"]:
            return person
