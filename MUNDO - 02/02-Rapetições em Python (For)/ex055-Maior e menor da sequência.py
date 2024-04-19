mape = mepe = 0
for c in range(1, 6):
    peso = float(input(f"Peso da {c}° pessoa:"))
    if c == 1:
        mape = peso
        mepe = peso
    elif peso > mape:
        mape = peso
    elif peso < mepe:
        mepe = peso
print(f"O maior peso informado é {mape:.1f}Kg"
      f"\nO menor peso informado é {mepe:.1f}Kg")
