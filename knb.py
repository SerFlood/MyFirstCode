result = "Вы ввели: "
knb = input()
rock, scissors, paper = "Камень", "Ножницы", "Бумага"

if knb == rock:
    print(result, knb)
    print(knb, "-", knb, "= Ничья")
    print(knb, "-", scissors, "= Победа")
    print(knb, "-", paper, "= Поражение")
if knb == scissors:
    print(result, knb)
    print(knb, "-", rock, "= Поражение")
    print(knb, "-", knb, "= Ничья")
    print(knb, "-", paper, "= Победа")
if knb == paper:
    print(result, knb)
    print(knb, "-", rock, "= Победа")
    print(knb, "-", scissors, "= Поражение")
    print(knb, "-", knb, "= Ничья")
if (knb != rock and knb != scissors and knb != paper):
    print("Вы ввели", knb, "Прошу вас ввести Камень Ножницы или Бумагу!!!")