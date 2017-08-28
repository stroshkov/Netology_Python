# Задание 2
import osa

with open('currencies.txt', encoding="utf8") as file:
    content = []

    for line in file:
        content.append(line)

new_content = ''.join(content)
new_new_content = new_content.split(' ')
moscow_london_price = int(new_new_content[1])
london_newyork_price = int(new_new_content[3])
newyork_brasilia_price = int(new_new_content[5])
brasilia_peking_price = int(new_new_content[7])
peking_seoul_price = int(new_new_content[9])
seoul_delhi_price = int(new_new_content[11])
delhi_moscow = int(new_new_content[13])
client = osa.Client('http://www.webservicex.net/CurrencyConvertor.asmx?WSDL')
moscow_london = client.service.ConversionRate('Content-Length:'=moscow_london_price, FromCurrency=EUR, ToCurrency=RUB)
london_newyork = client.service.ConversionRate('Content-Length:'=london_newyork_price, FromCurrency=USD, ToCurrency=RUB)
newyork_brasilia = client.service.ConversionRate('Content-Length:'=newyork_brasilia_price, FromCurrency=BRL, ToCurrency=RUB)
brasilia_peking = client.service.ConversionRate('Content-Length:'=brasilia_peking_price, FromCurrency=CNY, ToCurrency=RUB)
peking_seoul = client.service.ConversionRate('Content-Length:'=peking_seoul_price, FromCurrency=KRW, ToCurrency=RUB)
seoul_delhi = client.service.ConversionRate ('Content-Length:'=seoul_delhi_price, FromCurrency=INR, ToCurrency=RUB)
result = moscow_london + london_newyork + newyork_brasilia + brasilia_peking + peking_seoul + seoul_delhi + delhi_moscow
print(round(result, 0))
