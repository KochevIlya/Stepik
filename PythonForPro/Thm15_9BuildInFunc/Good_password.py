passwrd = input()

print("YES" if all( [len(passwrd) >= 7, any(map(lambda x: x.isdigit(), passwrd)), any(map(lambda x: x.isalpha() and x.islower(), passwrd)), any(map(lambda x: x.isalpha() and x.isupper(), passwrd))]) else "NO")