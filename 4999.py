mine = input()
doctor = input()
if len(mine) < len(doctor):
    print('no')
else:
    temp = len(mine) - len(doctor)

    if mine[temp:] == doctor:
        print('go')
    else:
        print('no')
