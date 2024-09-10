str = input ("Enter String: ")
vowel = set("aeiouAEIOU")
count = 0
for alphabet in str:
    if alphabet in vowel: 
       count = count + 1
print("Number Of Vowels: ", count) 