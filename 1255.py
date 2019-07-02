N = int(input())

for i in range(0, N):
    string = input().lower()
    letters = {}

    for letter in string:
        if letter.isalpha():
            if letter not in letters: letters[letter] = 1
            else: letters[letter] += 1

    letters = sorted(letters.items(),key=lambda kv: kv[1], reverse=True)
    lett_frequency = []
    lett_frequency.append(letters[0][0])

    for i in range(1, len(letters)):
        if letters[i][1] == letters[0][1]:
            lett_frequency.append(letters[i][0])
        else: break

    lett_frequency.sort()
    print("".join(lett_frequency))