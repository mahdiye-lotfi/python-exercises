password = "1234"
count = 3

for i in range(3):
    user = input("رمز را وارد کنید: ")

    if user == password:
        print("ورود موفق")
        break
    else:
        count = count - 1
        print("رمز اشتباه است")
        print("تعداد تلاش باقی مانده:", count)