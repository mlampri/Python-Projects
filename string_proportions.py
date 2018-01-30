def get_string_prop(text, strings = ['a', 'e', 'i', 'o', 'u']):
    total = 0
    for string in strings:
        string_count = text.lower().count(string.lower())
        total = total + string_count * len(string)
    proportion = total / len(text)
    return round(proportion,2)

ge = open('great_expectations_complete.txt').read()

print(get_string_prop(ge, ['and', 'to', 'the', 'of', 'a']))
