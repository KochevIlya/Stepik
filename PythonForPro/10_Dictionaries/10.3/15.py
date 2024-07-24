text = [i.strip(",./!;:?") for i in input().lower().split()]
result = {}

for i in text:
    result[i] = result.get(i, 0) + 1
word = text[0]
count = result[word]
for i in result:
    if result[i] < count or result[i] == count and word > i:
        word = i
        count = result[i]
print(word)
