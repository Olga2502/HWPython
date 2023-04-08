#Вы пользуетесь общественным транспортом? Вероятно, вы
#расплачивались за проезд и получали билет с номером. Счастливым
#билетом называют такой билет с шестизначным номером, где сумма
#первых трех цифр равна сумме последних трех. Т.е. билет с номером
#385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
#программу, которая проверяет счастливость билета

ticket = int(input('Введите шестизначный номер билета:'))
if ticket % 6 == 0  and ticket >= 0:
    a = ticket // 1000
    sum1 = a //100 + a % 100 // 10 + a % 10
    b = ticket % 1000
    sum2 = b //100 + b % 100 // 10 + b % 10
    if sum1 == sum2:
        print("Вам повезло, у Вас счастливый билет ", ticket, " так как сумма первых трех цифр  ", sum1, " равна сумме трех последних цифр ", sum2)
    else:
        print("У Вас обычный билет")
else:
   print("Вы ошиблись при вводе номера билета")


