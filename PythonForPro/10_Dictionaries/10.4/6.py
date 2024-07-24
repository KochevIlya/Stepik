n = int(input())
tel_book = {}
for i in range(n):
    number, name = input().lower().split()
    telephones = tel_book.get(name, [])
    telephones.append(number)
    tel_book[name] = telephones
m = int(input())
for i in range(m):

    print(*tel_book.get(input().lower(), ["абонент не найден"]))
