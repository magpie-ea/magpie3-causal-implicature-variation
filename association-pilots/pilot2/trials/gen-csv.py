names = ['Themaglin', 'Rebosen','Denoden','Flembers', 'Agoriv','Ceflar']
stims = []
for x in names:
    for y in names:
        if x != y:
            stims.append(['firstTopic', x, y, 'Speaking of ' + x, ' it is associated with ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['firstTopic', x, y, 'Speaking of ' + x, ' it is associated with ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['secondTopic', x, y, 'Speaking of ' + y, x  + ' is associated with it.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['secondTopic', x, y, 'Speaking of ' + y, x  + ' is associated with it.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])

csv="condition,name1,name2,promptPart1,promptPart2,choiceNameFirst,choice1,choice2\n"
for x in stims:
    for y in x:
        csv = csv + y + ","
    csv = csv[:-1] + "\n"   

fl = open("trials.csv", 'w')
fl.write(csv)
fl.close()