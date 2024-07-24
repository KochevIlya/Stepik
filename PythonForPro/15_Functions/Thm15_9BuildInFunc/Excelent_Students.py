n = int(input())

def check_student():
    student = input()
    if student[-1] == "5":
        return True

def check_class():
    k = int(input())
    result = []
    for i in range(k):
        result.append(check_student())
    return any(result)

result = []
for i in range(n):
    result.append(check_class())
print("YES" if all(result) else "NO")