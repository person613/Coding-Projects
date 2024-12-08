def rot(message,rotby):
    letterindex = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    input = message
    output = ""
    for i in range(len(input)):
        for x in range(26):
            if input[i] == letterindex[x]:
                output += letterindex[(x+rotby)%26]
        if input[i] == " ":
            output += " "
    return output
    
print(rot(str(input("What do you want to rotate? (Capital Only :\)")),int(input("How much do you want to rotate by?"))))
