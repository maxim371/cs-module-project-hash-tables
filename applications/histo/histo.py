# Your code here

f = open('C:/Users/Owner/Desktop/project/CS_2/cs-module-project-hash-tables/applications/histo/robin.txt', 'r')
remove = ["\"", ":", ";", ",", ".", "-", "+", "=", "/", "\\","|", "[", "]", "{", "}", "(", ")", "*", "^", "&", '', "!", "?"]
space = ' '

cache = {}
word = ''

for i in f.read().lower():
    if i in remove:
        continue

    if i == space or i == '\n':
        if i in cache:
            cache[word] = 1
        else:
            cache[word] = 1
        word = ''
    else:
        word += i

print(cache)

sorting = sorted(cache.items(), key=lambda keyandVal: (keyandVal[1], keyandVal[0]))
sorting = sorting[::-1]
str = ''
spaces = 20

for item in sorting:
    str += item[0]
    for r in range(0, spaces - len(str)):
        str += ' '
    for r in range(0, item[1]):
        str += '*'
    print(str)
    str = ''
