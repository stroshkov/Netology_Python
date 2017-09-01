# Задание 3
import osa


def convert_distance(distance):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    return client.service.ChangeLengthUnit(
        LengthValue=distance,
        fromLengthUnit='Miles',
        toLengthUnit='Kilometers'
    )


def calculation(file_for_calculation):
    distance_of_trip = 0

    for line in file_for_calculation:
        content = line.split(' ')
        length = content[1]
        clear_length = length.replace(',', '')
        length_for_calculation = float(clear_length)
        distance_of_trip += length_for_calculation

    distance_of_trip_in_km = convert_distance(distance_of_trip)
    return distance_of_trip_in_km


with open('travel.txt', encoding="utf8") as file:
    print(round(calculation(file), 2), 'Miles')
