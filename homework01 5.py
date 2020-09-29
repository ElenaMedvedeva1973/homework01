# Задание 5

proceed = int(input("Введите выручку: "))
outlay = int(input("Введите издержки: "))
if proceed > outlay:
    profitability = proceed - outlay
    rent = profitability / proceed
    print(f"Вы имеете  {profitability} profitability")
    worker = int(input("Сколько человек у вас работает: "))
    print(f"{profitability / worker} for one worker")
elif proceed == outlay:
    print("Это не плохо")

else:
    print("Удачи")
