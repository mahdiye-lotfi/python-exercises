
salary = int(input("حقوق کارمند را وارد کنید: "))
child = input("آیا کارمند فرزند دارد؟ (بله/خیر): ")

if salary <= 10000000:
    tax = 0

elif salary <= 25000000:
    tax = (salary - 10000000) * 0.10

else:
    tax = (15000000 * 0.10) + (salary - 25000000) * 0.20

if child == "بله":
    tax = tax - 500000

if tax < 0:
    tax = 0

print("مالیات نهایی:", tax, "تومان")
