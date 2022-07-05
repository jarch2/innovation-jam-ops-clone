def altcase(sl):
    output = ''
    index = 0
    for char in sl:
        if not char.isalnum():
            output += char
            continue
        if index % 2 == 0:
            output += char.upper()
        else:
            output += char.lower()
        index += 1
    return output

print(altcase("Yay I created a working program :)!!"))
