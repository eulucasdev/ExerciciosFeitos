dis = float(input("Distância em metros: "))
km = dis / 1000
hm = dis / 100
dam = dis / 10
dm = dis * 10
cm = dis * 100
mm = dis * 1000
print(f"A medida de {dis:.1f}m corresponde a:")
print(f"{km:.3f}km\n{hm:.2f}hm\n{dam:.1f}dam\n{dm:.0f}dm\n{cm:.0f}cm\n{mm:.0f}mm")
