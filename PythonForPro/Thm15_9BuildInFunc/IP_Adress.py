
ip = input()
if ip.count(".") != 3:
    print(False)
    quit()
for i in ip.split("."):
    if not i.isdigit():
        print(False)
        quit()

ip = [int(i) for i in ip.split(".")]
print(all(map(lambda x: 0 <= x <= 255, ip)))