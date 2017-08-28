import osa

with open('travel.txt', encoding="utf8") as file:
    content = []

    for line in file:
        content.append(line)

new_content = ''.join(content)
new_new_content = new_content.split(' ')
moscow_london_length = float(new_new_content[1])
london_newyork_length = float(new_new_content[3])
newyork_brasilia_length = float(new_new_content[5])
brasilia_peking_length = float(new_new_content[7])
peking_seoul_length = float(new_new_content[9])
seoul_delhi_length = float(new_new_content[11])
delhi_moscow_length = float(new_new_content[13])
sum_length = moscow_london_length + london_newyork_length + newyork_brasilia_length + brasilia_peking_length + peking_seoul_length + seoul_delhi_length + delhi_moscow_length
client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
result = client.service.ChangeLengthUnit('Content-Length:'=sum_length, fromLengthUnit=Mils, toLengthUnit=Kilometers)
print(round(result, 2))
