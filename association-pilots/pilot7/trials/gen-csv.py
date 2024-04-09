names = ['Themaglin', 'Rebosen','Denoden','Flembers', 'Agoriv','Ceflar']
stims = []
for x in names:
    for y in names:
        if x != y:
            stims.append(['asymmetric', x, y, x + ' is associated with ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['asymmetric', x, y, x + ' is associated with ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['symmetric', x, y, x + ' and ' + y + ' are associated.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['symmetric', x, y, x + ' and ' + y + ' are associated.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])

csv="condition,name1,name2,prompt,choiceNameFirst,choice1,choice2\n"
for x in stims:
    for y in x:
        csv = csv + y + ","
    csv = csv[:-1] + "\n"   

fl = open("trials.csv", 'w')
fl.write(csv)
fl.close()