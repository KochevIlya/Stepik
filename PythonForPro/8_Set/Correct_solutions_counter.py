n = int(input())
correct_sollutions = set()
counter = 0
for i in range(n):
    string = input()
    lst = string.split()
    if lst[-1] == "Correct":
        counter += 1
        correct_sollutions.add(string[:string.find(":")])
print("Вы можете стать первым, кто решит эту задачу" if len(correct_sollutions) == 0 else f"Верно решили {len(correct_sollutions)} учащихся\nИз всех попыток {int(100 * counter / n + 0.5)}% верных")
    
