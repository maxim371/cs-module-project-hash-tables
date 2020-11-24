# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

final = {}
count = {}
text = ''

with open('C:/Users/Owner/Desktop/project/CS_2/cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt', encoding='utf-8') as cipher_text:
    cipher = cipher_text.read()
letters =  ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
for c in cipher:
    if c.isalpha():
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
sorting = list(count.items())
sorting.sort(reverse=True, key = lambda item: item[1])
print(sorting)
for i, e in enumerate(letters):
    final[sorting[i][0]] = letters[i]

for c in cipher:
    if c.isalpha():
        text += final[c]
    else:
        text += c
print(text)

