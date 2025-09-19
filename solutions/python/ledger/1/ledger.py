from datetime import datetime


currencies = {
    'USD': '$',
    'EUR': '€',
}

locales = {
    "en_US": {
        "header": f"{'Date':<10} | {'Description':<25} | {'Change':<13}",        
        "date": "%m/%d/%Y",
    },

    "nl_NL": {
        "header": f"{'Datum':<10} | {'Omschrijving':<25} | {'Verandering':<13}",
        "date": "%d-%m-%Y",
    },
}


def create_entry(date, description, change):
    return {
        'date': datetime.strptime(date, '%Y-%m-%d'),
        'description': description,
        'change': change,
    }


def format_money(currency, locale, change):
    currency = currencies[currency]

    if locale == 'en_US':
        if change < 0:
            return f"({currency}{change/100:,.2f})".replace('-', '')
        return f"{currency}{change/100:,.2f} "    
            
    if locale == 'nl_NL':
        money = f"{currency} {change/100:,.2f} "
        money = money.translate({44:46, 46:44})
        return money


def format_entries(currency, locale, entries):
    book = [locales[locale]["header"]]

    entries.sort(
        key=lambda entry: (
            entry["date"], entry["description"], entry["change"]
            )
        )

    for entry in entries:
        date = entry["date"].strftime(locales[locale]["date"])
        description = entry["description"]
        if len(description) > 25:
            description = description[:22] + "..."
        money = format_money(currency, locale, entry["change"])
        book.append(
            f"{date:<10} | {description:<25} | {money:>13}"
            )
        
    return '\n'.join(book)


# changes:
# removed: # -*- coding: utf-8 -*- as it is the default encoding
# made a ledger entry be a dictionary instead of an object
# replaced object attribute references to dictionary key references
# sort entries at start of format_entries function
# added locales dictionary to store locale specific strings
# added currencies dictionary to store currency symbols
# made format_money function 
