my_text = 'Thirty years ago, Marseilles lay burning in the sun, one day.'


# Place name, pt 1
city_name = my_text[18:28]

print(city_name)

text_length = len(my_text)

city_name_length = len(city_name)

print('The whole text has: ' + str(text_length) + ' ' + 'characters')

print('The name of the city has: ' + str(city_name_length) + ' ' + 'characters')


# Place name, pt 2
percentage = (city_name_length / text_length) * 100

print(str(percentage) + '%' + ' ' + 'of the sentence is made up of the name of the city')


# Place name, pt 3
city_name_upper = city_name.upper()
new_text = my_text.replace(city_name,city_name_upper)
print(new_text)
