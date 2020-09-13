# List
print("List")

names = ["Tifa", "Cloud"]
print(names)
print(len(names))

names.append("Aerith")
print(names)

print(names[1])
print(names[0:3])

for index in range(0, len(names)):
    print(names[index])

for name in names:
    print(name)

names.sort()

for name in names:
    print(name)

scores = [87, 92, 43]
scores.sort()
for score in scores:
    print(score)