while True:
    var_a, var_b = input().split()
    carry = int(0)
    c = int(0)

    if var_a == '0' and var_b == '0': break

    while len(var_a) < len(var_b): var_a = '0' + var_a
    while len(var_b) < len(var_a): var_b = '0' + var_b

    for i in reversed(range(0, len(var_a))):
        if (((int(var_a[i]) + int(var_b[i])) > 9) or ((int(var_a[i]) + int(var_b[i]) + c)) > 9):
            carry += 1
            c = 1
        else: c = 0

    if carry == 0: print("No carry operation.")
    elif carry == 1:  print("1 carry operation.")
    else: print("{} carry operations.".format(carry))