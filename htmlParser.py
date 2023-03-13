# html parser
# example text:
# <mainText><stats><attention>50%</attention> Base Mana Regen</stats></mainText><br>


# input string, only append char if outside of <>
# htmlString = "<mainText><stats><attention>50%</attention> Base Mana Regen</stats></mainText><br>"


def parse(htmlString):
    toScreen = ''

    pointer1 = 0
    pointer2 = 0
    counter = 0
    closeCount = 0

    # sliding window
    while pointer1 != len(htmlString)-1:

        # to stop computer crash
        counter += 1
        if counter >= 100:
            break

        if htmlString[pointer1] == "<":
            # will always be a closed
            while htmlString[pointer2] != ">":
                pointer2 += 1

                # to stop computer crash
                counter += 1
                if counter >= 100:
                    break
            closeCount += 1
            if closeCount >= 4:
                toScreen += ' '

            # if next pointer isn't the end of the string, iterate ahead
            if pointer2 != len(htmlString)-1:
                pointer2 += 1
                pointer1 = pointer2
        else:
            # i moved the window all the way and appended, but there was no change, kept jumping to else block at same pointer
            toScreen += htmlString[pointer1]
            pointer2 += 1
            pointer1 = pointer2


    return(toScreen)
