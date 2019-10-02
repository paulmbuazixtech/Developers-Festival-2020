# Solution using while loop and return
def neutralize_uppercase(stringy):
    count = 0
    while count < len(stringy):
        if stringy[count] == stringy[count].upper():
            return ""
        count += 1
    return stringy
