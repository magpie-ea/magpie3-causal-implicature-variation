import itertools

names = ['Themaglin', 'Rebosen','Denoden','Flembers', 'Agoriv','Ceflar']

# create a list with all shuffles of the 'names' list
shuffled_names = list(itertools.permutations(names))

stims = []
for s in shuffled_names:
    stims.append([
        s[0], s[1], s[2], s[3], s[4], s[5],
        s[4] + ' is associated with ' + s[5] + '.',
        s[4] + ' causes ' + s[5] + '.',
        s[5] + ' causes ' + s[4] + '.'])

csv="name1,name2,name3,name4,name5,name6,prompt,choice1,choice2\n"
for x in stims:
    for y in x:
        csv = csv + y + ","
    csv = csv[:-1] + "\n"   

fl = open("trials.csv", 'w')
fl.write(csv)
fl.close()
