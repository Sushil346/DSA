# 2. You have a list of your favourite marvel super heros
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this list


heros=['spider man','thor','hulk','iron man','captain america']

print("Length is:", len(heros))
heros.append('black panther')
print(heros)

heros.remove('black panther')
print(heros)

heros.insert(3, 'black panther')
print(heros)

heros[1:2]=['doctor strange']
print(heros)

heros.sort()
print(heros)
