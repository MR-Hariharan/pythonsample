# Name: Hariharan K
# Roll Number: 720722115025
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
min = temperatures[0]
max = temperatures[0]
for temp in temperatures:
    if temp > max:
        max = temp
    if temp < min:
        min = temp
print(f"Maximum temperatures: {max}°C")
print(f"Minimum temperatures: {min}°C")            

print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
count = 0
max = temperatures[0]
for temp in temperatures:
    if temp > 30:
        count +=1
print(f"Hot Days (>30°C): {count}")        

print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
for temp in temperatures:
    if temp > 35:
        print(f"Alert! Extreme temperature: {temp}°C detected")
