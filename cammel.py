"""
In this program text in variable word is convert to pseudo-cammel style where first word always start from big letter, no spaces and char like . , !?, etc. count
"""
word = input("Input the sentence:") 
#"This is a test"
new = ""
list_word = word.split(" ")
for items in list_word:
    for num, item in enumerate(items):
        if num%2:
            new += item.lower()
        else:
            new += item.upper()
    new += " "
new = new[:-1]
print(new)
