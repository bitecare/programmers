lists = ["a","e","i","o","u"]

while True:
    word = input()
    aeiou_count = 0
    cont_aeiou = 0
    cont_bcd = 0
    last_word = word[0]
    acceptable = True
    
    if word == "end":
        break
    
    for i in range(len(word)):
        
        if word[i] in lists:
            aeiou_count +=1
            cont_aeiou +=1
            cont_bcd = 0
        else :
            cont_aeiou = 0
            cont_bcd += 1
            
        if cont_aeiou == 3 or cont_bcd == 3:
            acceptable = False

        if i >= 1 :
            if last_word == word[i] and last_word != "e" and last_word != "o" :
                acceptable = False
            else :
                last_word = word[i]

    if aeiou_count == 0:
        acceptable = False

    if acceptable :
        print(f"<{word}> is acceptable.")
    else :
        print(f"<{word}> is not acceptable.")

    