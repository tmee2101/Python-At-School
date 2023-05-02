E = {(12, 3, 7, 11), (2, 9, 5, 13), (1, 4, 8)}

a = set()
for tp in E:
    avr = sum(tp) / len(tp)
    a.add((tp[0], avr))

print(a)


