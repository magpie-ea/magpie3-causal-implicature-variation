# ’npm install’ -> ’npm run serve’

names = ['Themaglin', 'Rebosen','Denoden','Flembers', 'Agoriv','Ceflar']
stims = []
for x in names:
    for y in names:
        if x != y:
            stims.append(['first','having', x, y, 'Having ' + x + ' is associated with ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['first','getting', x, y, 'Getting ' + x + ' is associated with ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['first','having', x, y, 'Having ' + x + ' is associated with ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['first','getting', x, y, 'Getting ' + x + ' is associated with ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['second','having', x, y, x + ' is associated with getting ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['second','getting', x, y, x + ' is associated with having ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['second','having', x, y, x + ' is associated with getting ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['second','getting', x, y, x + ' is associated with having ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            

csv="targeted,itemType,name1,name2,prompt,choiceNameFirst,choice1,choice2\n"
for x in stims:
    for y in x:
        csv = csv + y + ","
    csv = csv[:-1] + "\n"   

fl = open("trials.csv", 'w')
fl.write(csv)
fl.close()