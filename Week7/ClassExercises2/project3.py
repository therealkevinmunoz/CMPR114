baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

print("The following students are on the baseball team")

for name in baseball:
    print(name)

print()
print("The following students are on both the baseball and basketball team")
for name in baseball.intersection(basketball):
    print(name)

print()
print("The following students are on either on the baseball or basketball team")
for name in baseball.union(basketball):
    print(name)

print()
print("The following students play baseball, but not basketball")
for name in baseball.difference(basketball):
    print(name)

print()
print("The following students play basketball, but not baseball")
for name in basketball.difference(baseball):
    print(name)

print()
print("The following students play one sport, but not both")
for name in baseball.symmetric_difference(basketball):
    print(name)