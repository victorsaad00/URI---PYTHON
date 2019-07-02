from difflib import SequenceMatcher

while True:
    try:
        sub_1 = input()
        sub_2 = input()
        sub = SequenceMatcher(None, sub_1, sub_2)
        s_size = sub.find_longest_match(0, len(sub_1), 0, len(sub_2))
        print(s_size.size)

    except EOFError:
        break