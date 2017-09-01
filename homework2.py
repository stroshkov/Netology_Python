# Задание 2
#нахождение стоимости перелета
import osa


def convert_currency(choose_price, choose_currency):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    return client.service.ConvertToNum(
        fromCurrency=choose_currency,
        toCurrency='RUB',
        amount=choose_price,
        rounding=False
    )


def calculation(file_for_calculation):
    price_of_trip = 0

    for line in file_for_calculation:
        content = line.split(' ')
        price = content[1]
        dirty_currency = content[2]
        currency = dirty_currency[:-1]
        price_of_trip += convert_currency(price, currency)

    return price_of_trip

with open('currencies.txt', encoding="utf8") as file:
    print(round(calculation(file), 2), 'RUB')
