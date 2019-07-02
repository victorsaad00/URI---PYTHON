entry = int(input())
list = {
    # Empty Dictonary
}

for i in range(entry):
	v = int(input())
	if v in list: list[v] += 1 # +1 in v
	else: list[v] = 1
'''
list = {
    v : list[v],
    a : list[a],
    ...
}
'''

list_keys = list.keys()
list_keys = sorted(list_keys) # sort keys

for i in list_keys: # i = keys : list[i] = dictonary values
    print('{} aparece {} vez(es)'.format(i,list[i]))
