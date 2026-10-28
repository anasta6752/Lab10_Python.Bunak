
import os

files = os.listdir(".")

print("Вміст поточного каталогу:")
for name in files:
    print(name)

f_files = [
    name for name in files
    if name.startswith("f") and os.path.isfile(name)
]

print("Файли, які починаються з літери f:")
print(f_files)
