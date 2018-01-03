statsFile = open("stats.txt", "w")
statsFile.write("Count: 0")
statsFile.close()
print("Write done")

myFile = open("stats.txt", "r")
stats = myFile.read().replace('Count:', ' ')
print(stats)

stats = int(stats) + 1
print(stats)
