money = 1000000

while True:
    print("1. برداشت وجه")
    print("2. واریز وجه")
    print("3. نمایش موجودی")
    print("4. خروج")

    choice = int(input("گزینه را انتخاب کنید: "))

    if choice == 1:
        amount = int(input("مبلغ برداشت: "))
        if amount <= money:
            money = money - amount
            print("برداشت موفق")
        else:
            print("موجودی کافی نیست")

    elif choice == 2:
        amount = int(input("مبلغ واریز: "))
        money = money + amount
        print("واریز موفق")

    elif choice == 3:
        print("موجودی:", money)

    elif choice == 4:
        print("خروج از برنامه")
        break

    else:
        print("گزینه نامعتبر")