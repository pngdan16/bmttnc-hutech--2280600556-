from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("************************MENU************************")
    print("1. Them sinh vien.")
    print("2. Cap nhat thong tin sinh vien boi ID.")
    print("3. Xoa sinh vien boi ID.")
    print("4. Tim kiem sinh vien theo ten.")
    print("5. Sap xep sinh vien theo diem trung binh (GPA).")
    print("6. Sap xep sinh vien theo ten chuyen nganh.")
    print("7. Hien thi danh sach sinh vien.")
    print("8. Thoat")
    print("*****************************************************")
    
    key = int(input("Nhap tuy chon: "))
    
    if key == 1:
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")

    elif key == 2:
        if qlsv.soLuongSinhVien() > 0:
            print("\n2. Cap nhat thong tin sinh vien boi ID.")
            ID = int(input("Nhap ID: "))
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 3:
        if qlsv.soLuongSinhVien() > 0:
            print("\n3. Xoa sinh vien.")
            ID = int(input("Nhap ID: "))
            qlsv.deleteSinhVien(ID)
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 4:
        if qlsv.soLuongSinhVien() > 0:
            print("\n4. Tim kiem sinh vien theo ten.")
            name = input("\nNhap ten de tim kiem: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 5:
        if qlsv.soLuongSinhVien() > 0:
            print("\n5. Sap xep sinh vien theo diem trung binh.")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 6:
        if qlsv.soLuongSinhVien() > 0:
            print("\n6. Sap xep sinh vien theo ten chuyen nganh.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 8:
        print("\nThoat chuong trinh!")
        break