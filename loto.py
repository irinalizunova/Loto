import random
a = 0
while a < 1:
    a = int(input('Введите количество бочонков: '))
    if (a < 1):
        print('Введите число еще раз')
    if (a > 1):
        break

print('Последовательность вытянутых бочонков')
spisok = []

for i in range(1, a + 1):
    spisok.append(i)
    
for i in range(len(spisok)): 
    A = random.choice(spisok) 
    spisok.remove(A) 
    print(A)    
    


