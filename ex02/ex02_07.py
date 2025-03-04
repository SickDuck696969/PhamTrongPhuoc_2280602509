print("Nhap cac dong van ban (Nhap 'done' de ket thuc):")
lines = []
while True:
    line = input()
    if line == "done":
        break
    lines.append(line)
print("\nCac dong sau khi duoc in hoa:")
for line in lines:
    print(line.upper())