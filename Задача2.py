msg = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_msg = ''
for i in range(len(msg)):
    for a in range(len(msg[i])):
        if msg[i][0].isdigit() == True and len(msg[i]) == 2:
            msg[i] = '"' + msg[i] + '"'
            break
        if msg[i][a].isdigit() == True:
            msg[i] = msg[i].zfill(len(msg[i]) + 1)
            msg[i] = '"' + msg[i] + '"'
for n in range(len(msg)):
    new_msg += msg[n]
    new_msg += ' '
print(new_msg)
