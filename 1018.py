note = int(input())
div_notes = [100,50,20,10,5,2,1]
result = [1] * len(div_notes)

print("%d"%note)
for i in range(len(div_notes)):
    result[i] = float(note) / div_notes[i]
    note = float(note) % div_notes[i]

for j in range(7):
    print('{} nota(s) de R$ {},00'.format(int(result[j]), int(div_notes[j])))

