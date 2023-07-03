#Task 5: Positional and keyword arguments + default values
# a pig_latin function. This function will receive any amount of String objects. For each word in those strings, it should transform the word according to these rules:

    #If the word starts with vowel, add ay at the end.
    #If not, move the first letter to the end and add ay

def pig_latin(*args, suffix='ay', single=False):
    result = []
    for string in args:
        words = string.split()
        transformed_words = []
        for word in words:
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                transformed_word = word + suffix
            else:
                transformed_word = word[1:] + word[0] + suffix
            transformed_words.append(transformed_word)
        
        if single:
            result.append(' '.join(transformed_words))
        else:
            result.extend(transformed_words)
    
    if single:
        return result[0]
    else:
        return result
test1_data = ["Word", "Apple"]
test1_config = {}

test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}


print(pig_latin(*test1_data, **test1_config))  # ['Ordway', 'Appleay']
print(pig_latin(*test2_data, **test2_config))  # ['Ythonpoy', 'Unctionsfoy']
print(pig_latin(*test3_data, **test3_config))  # If the word starts with a vowelay add the suffix to the worday
