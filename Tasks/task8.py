# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no
print('Enter the heigth of the chocolate bar')
h = int(input())
print('Enter the width of the chocolate bar')
w = int(input())
print('Enter how many pieces of chocolate do you want to break')
k = str(input())
ch = h*w
if(ch%int(k[0])==0 and ch%int(k[1])==0 and ch%int(k[2])==2):
    print('Yes')
else:
    print('No')


