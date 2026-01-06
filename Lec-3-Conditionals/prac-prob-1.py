device_status = input("Enter Device Status: ").lower()
temperature = int(input("Enter the temperature:"))

if device_status == "active":
    if temperature > 35:
        print("Warn: High Temperature")
    else:
        print("Temperature normal")
else:
    print("Device is offline")