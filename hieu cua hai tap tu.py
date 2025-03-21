with open("DATA1.in") as file: set1 = set(file.read().lower().split())
with open("DATA2.in") as file: set2 = set(file.read().lower().split())
print(' '.join(sorted(set1.difference(set2))))
print(' '.join(sorted(set2.difference(set1))))