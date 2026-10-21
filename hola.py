import os

print("Archivos encontrados:")

for archivo in os.listdir():
    print("-", archivo)
