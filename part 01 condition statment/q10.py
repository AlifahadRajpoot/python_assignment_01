#  Write a program to determine if a given character is a vowel or consonant.

txt = input("Enter  a character: ")

if txt.isalpha():
    if txt.lower() in 'aeiou':
        print(txt, "is a vowel")
    else:
        print("consonant")
else:
    print("Not a letter")
    
