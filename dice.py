throws = "6526366334622464452646525326663442366264262264265666634122663261255665433664446453556422156224425261"
results = [0, 0, 0, 0, 0, 0]


for throw in throws:
    results[int(throw) - 1] = results[int(throw) - 1] + 1

for i in range(0, 6):
    print("Number of ", i + 1, ":", results[i])
