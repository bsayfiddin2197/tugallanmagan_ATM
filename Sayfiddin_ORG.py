atm = int(input("parol kiriting: "))
balans = 1000000
parol = 2197


if atm == parol:
    print("manyu")
    print("1. pul ol")
    print("2. balans")
    menyu = int(input("kerak ishni tanla 1/2: "))
    if manyu == 1:
        print("1. 50000")
        print("2. 100000")
        print("3. 500000")
        print("4. 1000000")
        boshqa_summa = int(input("boshqa summa kiriting: "))
        print(f"5. boshqa summa: {boshqa_summa}")
    elif menyu == 2:
        print(f"balans: {balans}")
    else:
        print(f"xato yomalish: {manyu}")
elif atm != parol:
    print(f"XATO PAROL: {atm}")

