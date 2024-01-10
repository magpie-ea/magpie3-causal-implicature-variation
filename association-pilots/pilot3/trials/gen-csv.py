# ’npm install’ -> ’npm run serve’

names = ['Themaglin', 'Rebosen','Denoden','Flembers', 'Agoriv','Ceflar']
stims = []
for x in names:
    for y in names:
        if x != y:
            stims.append(['first','drug', x, y, 'The drug ' + x + ' has been found to be associated with ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['first','disease', x, y, 'The disease ' + x + ' has been found to be associated with ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['first','drug', x, y, 'The drug ' + x + ' has been found to be associated with ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['first','disease', x, y, 'The disease ' + x + ' has been found to be associated with ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['second','drug', x, y, x + ' has been found to be associated with the drug ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['second','disease', x, y, x + ' has been found to be associated with the disease ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['second','drug', x, y, x + ' has been found to be associated with the drug ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['second','disease', x, y, x + ' has been found to be associated with the disease ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            

csv="targeted,itemType,name1,name2,prompt,choiceNameFirst,choice1,choice2\n"
for x in stims:
    for y in x:
        csv = csv + y + ","
    csv = csv[:-1] + "\n"   

fl = open("trials.csv", 'w')
fl.write(csv)
fl.close()