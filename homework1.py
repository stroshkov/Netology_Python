# Задание 1
# нахождение средней температуры с округлением до десятых
import osa


def convert_temperature(temp):
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    return client.service.ConvertTemp(
        Temperature=temp,
        FromUnit='degreeFahrenheit',
        ToUnit='degreeCelsius'
    )


with open('temps.txt', encoding="utf8") as file:
    content = []
    sum_of_content = 0

    for line in file:
        content.append(line[:2])

    for element in content:
        sum_of_content += int(element)

    average_temp = sum_of_content / len(content)
    average_temp_in_Celsius = convert_temperature(average_temp)
    print(round(average_temp_in_Celsius, 1), 'градусов по Цельсию')
