for i in range(1, 51):
    if i == 42:
        break

    if i % 5 == 0:
        continue

    if i % 3 == 0:
        print(i)