# Задание 1

with open('temps.txt', encoding="utf8") as file:
    content = []
    sum_of_content = 0

    for line in file:
        content.append(line[:2])

    for element in content:
        sum_of_content += int(element)

    average_temp = sum_of_content / len(content)
    print(round(average_temp, 1), 'F')
