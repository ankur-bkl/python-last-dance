# niu language
# vowels -> n
# -----------

# dog -> dng
# cat -> cng

    
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation+="N"
            else:
                translation+="n"
        else:
            translation=translation + letter
    return translation
print(translate(input("Enter the phrase: ")))