my_text = 'Night is generally my time for walking. In the summer I often leave home early in the morning, and roam about fields and lanes all day, or even escape for days or weeks together; but, saving in the country, I seldom go out until after dark, though, Heaven be thanked, I love its light and feel the cheerfulness it sheds upon the earth, as much as any creature living.'

text_length = len(my_text)
print('The length of whole text is: '+ str(text_length) + ' ' +'characters')

#calculate the length of short sentence
sentence_one = my_text.find('.')
#print(sentence_one)
print('The length of first sentence is: ' + str(sentence_one + 1) + ' ' + 'characters')

#calculate the length of long sentence
sentence_two = text_length - (sentence_one + 1)
print('The length of second sentence is: ' + str(sentence_two) + ' ' + 'characters')
