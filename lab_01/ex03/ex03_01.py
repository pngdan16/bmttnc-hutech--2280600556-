def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong



input_list = input("nhập ds các só cắt nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))



print("number", numbers)
tong_chan = tinh_tong_so_chan(numbers)
print("tổng các só chẵn trong list là: ", tong_chan)  
