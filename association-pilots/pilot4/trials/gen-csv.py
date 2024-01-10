# \'npm install\' -> \'npm run serve\'

names = ['Themaglin', 'Rebosen','Denoden','Flembers', 'Agoriv','Ceflar']
stims = []
for x in names:
    for y in names:
        if x != y:
            stims.append(['first','first','observation', x, y, 'I was surprised to see ' + x + ' in yesterday\'s sample.', x + ' is associated with ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['first','first','avoidance', x, y, 'I am surprised that you think ' + x + ' should be removed from the samples.', x + ' is associated with ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['second','first','observation', x, y, 'I was surprised to see ' + y + ' in yesterday\'s sample.', x + ' is associated with ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['second','first','avoidance', x, y, 'I am surprised that you think ' + y + ' should be removed from the samples.', x + ' is associated with ' + y + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['first','second','observation', x, y, 'I was surprised to see ' + x + ' in yesterday\'s sample.', y + ' is associated with ' + x + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['first','second','avoidance', x, y, 'I am surprised that you think ' + x + ' should be removed from the samples.', y + ' is associated with ' + x + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['second','second','observation', x, y, 'I was surprised to see ' + y + ' in yesterday\'s sample.', y + ' is associated with ' + x + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['second','second','avoidance', x, y, 'I am surprised that you think ' + y + ' should be removed from the samples.', y + ' is associated with ' + x + '.', x, x + ' causes ' + y + '.', y + ' causes ' + x + '.'])
            stims.append(['first','first','observation', x, y, 'I was surprised to see ' + x + ' in yesterday\'s sample.', x + ' is associated with ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['first','first','avoidance', x, y, 'I am surprised that you think ' + x + ' should be removed from the samples.', x + ' is associated with ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['second','first','observation', x, y, 'I was surprised to see ' + y + ' in yesterday\'s sample.', x + ' is associated with ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['second','first','avoidance', x, y, 'I am surprised that you think ' + y + ' should be removed from the samples.', x + ' is associated with ' + y + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['first','second','observation', x, y, 'I was surprised to see ' + x + ' in yesterday\'s sample.', y + ' is associated with ' + x + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['first','second','avoidance', x, y, 'I am surprised that you think ' + x + ' should be removed from the samples.', y + ' is associated with ' + x + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['second','second','observation', x, y, 'I was surprised to see ' + y + ' in yesterday\'s sample.', y + ' is associated with ' + x + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            stims.append(['second','second','avoidance', x, y, 'I am surprised that you think ' + y + ' should be removed from the samples.', y + ' is associated with ' + x + '.', y, y + ' causes ' + x + '.', x + ' causes ' + y + '.'])
            

csv="QUDTarget,statementFirst,treatment,name1,name2,QUD,statement,choiceNameFirst,choice1,choice2\n"
for x in stims:
    for y in x:
        csv = csv + y + ","
    csv = csv[:-1] + "\n"   

fl = open("trials.csv", 'w')
fl.write(csv)
fl.close()