try:
    initial_amount=float(input("Введіть початкову суму депозиту: "))
    if initial_amount <= 0:
       print("Початкова сума депозиту не може бути нуля")
       print("Для подальшої роботи перезавантажте програму")
       exit()
    annual_rate=float(input("Введіть річну відсоткову ставку: "))
    if annual_rate <=0 or annual_rate >=100:
       print("Річна відсоткова ставка не може бути менше 0% або більше 100%")
       print("Для подальшої роботи перезавантажте програму")
       exit()
    time=int(input("Введіть кількість місяців: "))
    if time <=0:
       print("Кількість місяців має бути цілим додатнім числом")
       print("Для подальшої роботи перезавантажте програму")
       exit()
    mpercent = annual_rate / 12 / 100
    for t in range(1, time +1):
       mprofit = initial_amount * mpercent
       initial_amount += mprofit
       print(f"Місяць {t}, Кінцева сума депозиту: {initial_amount:.2f}, Відсотки за місяць: {mprofit:.2f}")
except ValueError:
   print("Помилковий тип даних")
   
