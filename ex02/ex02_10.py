def dao_nguoc_ch(chuoi):
    return chuoi[::-1]
input_string = input("Nhap chuoi can dao nguoc: ")
print("Chuoi sau khi dao nguoc:", dao_nguoc_ch(input_string))