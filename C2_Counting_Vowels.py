my_text = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way - in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.'

#convert the whole text in lower case
low_my_text = my_text.lower()

#count the number of letters
a_count = low_my_text.count('a')

e_count = low_my_text.count('e')

i_count = low_my_text.count('i')

o_count = low_my_text.count('o')

u_count = low_my_text.count('u')

#Count the number of vowels
number_of_vowels = a_count + e_count + i_count + o_count + u_count

spaces_count = my_text.count(' ') #count the spaces

my_text_count = len(my_text) #count whole text

#now print the counts
print("Number of a's: " + str(a_count))

print("Number of e's: " + str(e_count))

print("Number of i's: " + str(i_count))

print("Number of o's: " + str(o_count))

print("Number of u's: " + str(u_count))

print("Vowels: " + str(number_of_vowels))

print("Number of spaces: " + str(spaces_count)) 

print("Total number of characters: " + str(my_text_count))

#proportion of vowels
Proportion = (number_of_vowels / my_text_count)
print("The proportion of vowels in this text is: " + str(Proportion))

#percentage of vowels
Percentage = Proportion * 100
print("The percentage of vowels in this text is: " + str(Percentage))
 

