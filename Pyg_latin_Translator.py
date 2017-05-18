word = raw_input("Enter any Word In English : ")

if word.isalpha():
    temp = word[0]
    word = word[1:] + temp + "ay."
    print word
    
else:
    print "Better Luck next time"
