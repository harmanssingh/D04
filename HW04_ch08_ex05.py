# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.
def rotate_word(word,shiftint):
    word1=''
    numa=ord('a')
    numz=ord('z')
    for s in word:
        if shiftint>0 and ord(s)+shiftint>numz:
            word1=word1+chr(ord(s)+shiftint-26)
        elif shiftint<0 and ord(s)+shiftint<numa:
            word1=word1+chr(ord(s)+shiftint+26)
        else:
            word1=word1+chr(ord(s)+shiftint)
    return word1


rotate_word('Hello',10)
rotate_word('World',-8)
