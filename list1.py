sentence = "Don't panic!"
#0-d |  1-o |  n-2 |  3-' 4- t | _ - 5 | 6-p | 7 - a | 8 - n | 9 - i | 10 - c | 11 - !
plist = list(sentence)
new_sentence = ""
# the expected output is "on tap"
for c in range(4):
    plist.pop()
for c in range(0, 4, 2):
    plist.pop(c)
plist.insert(2, plist.pop(3))
plist.insert(4,plist.pop(5))
new_sentence = new_sentence.join(plist)
print(new_sentence)

#cutting the list from the start
print(plist[6:])
#cutting the list from the end
print (plist[:-7])
#cutting every second letter
print(plist[::2])

