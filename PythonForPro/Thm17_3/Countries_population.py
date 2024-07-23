with open("population.txt") as file:
    Data = file.readlines()
    countries, population = [], []
    
    for i in Data:
        words = i.split("\t")
        countries.append(words[0])
        population.append(words[1])

    for i in range(len(population)):
        if int(population[i]) > 500_000 and countries[i][0] == "G":
            print(countries[i])
