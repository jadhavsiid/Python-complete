"""
You want to simulate tea heating.
It starts with 40°C and boils at 100°C.
Task:
- Use a while loop
- Increase temperature by 15 untill it reaches or exceeds 100°C.
- Print each temperature step
"""
temp = 40
while temp < 100:
    print(f"Current Temp: {temp}")
    temp += 15

print("Tea is ready to boil")