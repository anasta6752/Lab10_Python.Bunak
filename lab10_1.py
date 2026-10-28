
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("s1.txt", "w", encoding="utf-8") as f:
    for i, line in enumerate(lines, start=1):
        if i % 2 == 0:
            f.write(line)

with open("s2.txt", "w", encoding="utf-8") as f:
    for i, line in enumerate(lines, start=1):
        if i % 2 != 0:
            f.write(line)

print("Рядки записано у файли s1.txt та s2.txt")
