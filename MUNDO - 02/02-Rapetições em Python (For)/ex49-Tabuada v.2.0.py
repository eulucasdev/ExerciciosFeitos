print("*"*30)
print(f"{"TABUADA":^30}")
print(f"*"*30)
n = int(input("\nQuer saber a tabúada de qual número: "))
print("=-"*15)
for c in range(1, 11):
    print(f"{n:<2} x {c:>2} = {n*c:>3}")
print("-="*15)
print("FIM!")
