def count_c_v(s):
    vowels = 0
    consonants = 0
    for char in s.lower():
        if char.isalpha():
            if char in "aeiou":
                vowels+=1
            else:
                consonants+=1
    return vowels,consonants
v,c = count_c_v("Amity University")
print("Vovels: ",v)
print("consonants: ",c)
