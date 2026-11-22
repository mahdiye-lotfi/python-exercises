salary = int(input("حقوق ماهیانه را وارد کنید: "))

tax = salary * 0.10
net = salary - tax

print("مالیات:", tax)
print("حقوق خالص:", net)