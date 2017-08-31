# Задание 2
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

# эта строчка сделана для проверки
        print(price, currency, convert_currency(price, currency), price_of_trip)
# в приложении №1 (внизу кода) указан вывод верхней строки. Всплывает ошибка в самом конце, когда уже все посчитано   
    
    return round(price_of_trip, 1)


with open('currencies.txt', encoding="utf8") as file:
    print(calculation(file))

# Приложение №1
#C:\Users\User\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/User/PycharmProjects/untitled/3.5/homework2.py
#120 EUR 8294.820000000002 8294.820000000002
#235 USD 13737.016913319238 22031.83691331924
#112 BRL 2069.4552258754343 24101.292139194673
#243 CNY 2151.835214389116 26253.12735358379
#97 KRW 5.036717822749058 26258.16407140654
#130 INR 118.86394751288037 26377.02801891942
#Traceback (most recent call last):
# File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\osa\method.py", line 106, in __call__
# response = urlopen(request)
# File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 223, in urlopen
# return opener.open(url, data, timeout)
#   File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 532, in open
#     response = meth(req, response)
#   File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 642, in http_response
#     'http', request, response, code, msg, hdrs)
#   File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 570, in error
#     return self._call_chain(*args)
#   File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 504, in _call_chain
#     result = func(*args)
#   File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 650, in http_error_default
#     raise HTTPError(req.full_url, code, msg, hdrs, fp)
# urllib.error.HTTPError: HTTP Error 500: Internal Server Error
# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "C:/Users/User/PycharmProjects/untitled/3.5/homework2.py", line 34, in <module>
#     print(calculation(file))
#   File "C:/Users/User/PycharmProjects/untitled/3.5/homework2.py", line 27, in calculation
#     price_of_trip += convert_currency(price, currency)
#   File "C:/Users/User/PycharmProjects/untitled/3.5/homework2.py", line 11, in convert_currency
#     rounding=False
#   File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\osa\method.py", line 155, in __call__
#     string, detail))
# RuntimeError: SOAP Fault http://fx.currencysystem.com/webservices/CurrencyServer4.asmx: ConvertToNum <soap:Server> Server was unable to process request. ---> Currency not found. 

# Process finished with exit code 1
