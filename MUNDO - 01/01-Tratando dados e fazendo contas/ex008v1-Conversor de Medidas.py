dis = float(input("Distância em metros: "))
print(f"{dis}m corresponde a: ")
print(f"{dis/1000:.3f}km"
      f"\n{dis/100:.2f}hm"
      f"\n{dis/10:.1f}dam"
      f"\n{dis*10:.0f}dm"
      f"\n{dis*100:.0f}cm"
      f"\n{dis*1000:.0f}mm")
