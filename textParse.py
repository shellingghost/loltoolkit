
#text = "Periodically, Aatrox's next basic attack deals bonus <physicalDamage>physical damage"
def textParse(text):
    finText = ''

    pointer1 = 0
    pointer2 = 0

    for x in range(0,len(text)):
        # if point on text is at the beginning of a < block
        if text[x] == '<':
            # set pointer2 to current position
            pointer2 = x
            # increment pointer2 until end of text, then match pointer1 to it
            while text[pointer2] != '>':
                pointer2 += 1
            if len(text) != pointer2:
                pointer1 = pointer2
                pointer1 += 1
        # if x has inc to a valid pointer position, add it to text        
        elif pointer1 == x:
            finText += text[pointer1]
            pointer1 += 1

    return(finText)
#print(textParse(text))