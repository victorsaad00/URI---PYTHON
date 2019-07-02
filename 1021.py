note = float(input())
div_notes = [100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01]
result = [1] * len(div_notes)

for i in range(len(div_notes)):
    result[i] = float(note) / div_notes[i]
    note = float(note) % div_notes[i]
    if i == (len(div_notes) - 1):
        for j in range(0, 12):
            if j < 6:
                if j == 0: print("NOTAS:")
                print('{} nota(s) de R$ {}.00'.format(int(result[j]), div_notes[j]))
            elif j >= 6 or j <= 11:
                if j == 6: print("MOEDAS:")
                print('{:0.0f} moeda(s) de R$ {:0.2f}'.format(float(result[j]), float(div_notes[j])))

#print('{:0.0f} moeda(s) de R$ {:0.2f}'.format(float(result[11]),float(div_notes[11])))


