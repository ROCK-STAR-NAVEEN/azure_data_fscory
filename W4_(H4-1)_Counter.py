def counter(description):
    list_of_words = description.split()
    new_word_list = []
    for word in list_of_words:
        if word.isupper():
            new_word_list.append(word)
        else:
            new_word_list.append(word.title())
    new_description = ' '.join(new_word_list)
    print("The updated description : ")
    print(new_description)

    print("+-----------------------------------------------------+")

    space = 0
    upper_char = 0
    lower_char = 0
    alphabets = 0
    digits = 0

    for char in new_description:

        if char.isalpha():
            alphabets += 1

        if char.isupper():
            upper_char += 1
        elif char.islower():
            lower_char += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            space += 1
        else:
            pass

    print("The number of alphabetic characters : {}".format(alphabets))
    print("The number of UpperCase characters : {}".format(upper_char))
    print("The number of LowerCase characters : {}".format(lower_char))
    print("The number of numeric digits : {}".format(digits))
    print("The number of spaces in the description : {}".format(space))


description = input("Enter a description: ")
counter(description)
