def translator(phrase):
    translation=""
    for index in phrase:
        if index in "AEIOUaeiou":
            if index.isupper():
                translation+="Fvck"
            else:
                translation+="Hvll"
        else:
            translation+=index
    return translation
print(translator(input("Enter the phrase to fck with: ")))
                