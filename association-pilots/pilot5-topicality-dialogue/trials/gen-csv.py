# \'npm install\' -> \'npm run serve\'

names = ['Themaglin', 'Rebosen','Denoden','Flembers', 'Agoriv','Ceflar']
stims = []
for x in names:
    for y in names:
        if x != y:
            stims.append(['first','first', x, y, 'Can you tell me something about ' + x + '?', x + ' is associated with ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['second','first', x, y, 'Can you tell me something about ' + y + '?', x + ' is associated with ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['first','second', x, y, 'Can you tell me something about ' + x + '?', y + ' is associated with ' + x + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['second','second', x, y, 'Can you tell me something about ' + y + '?', y + ' is associated with ' + x + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['first','first', x, y, 'Can you tell me something about ' + x + '?', x + ' is associated with ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['second','first', x, y, 'Can you tell me something about ' + y + '?', x + ' is associated with ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['first','second', x, y, 'Can you tell me something about ' + x + '?', y + ' is associated with ' + x + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['second','second', x, y, 'Can you tell me something about ' + y + '?', y + ' is associated with ' + x + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])

csv="topic,statementFirst,name1,name2,QUD,statement,choiceNameFirst,choice1,choice2\n"
for x in stims:
    for y in x:
        csv = csv + y + ","
    csv = csv[:-1] + "\n"   

fl = open("trials.csv", 'w')
fl.write(csv)
fl.close()