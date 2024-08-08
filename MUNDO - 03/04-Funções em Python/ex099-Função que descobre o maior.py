from time import sleep


def maior(*num):
    print("-=" * 25)
    print("== Analisando valores informados ==")
    n = 0
    for c in num:
        if c > n:
            n = c
        print(c, end=" ")
        sleep(0.5)
    print(f"Foram recebidos {len(num)} valores")
    print(f"O maior valor foi: {n}")


maior(8, 3, 1, 12, 4, 0, 2)
maior(6, 8, 3)
maior(85, 0, 23, 5)
maior(6)
maior(1, 2)
maior(90, 45, 38, 31, 100, 85, 402, 65, 356)
maior()

