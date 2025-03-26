from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if len(self.listSinhVien) > 0:
            maxId = self.listSinhVien[-1]._id
            maxId = maxId + 1
        return maxId

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        sv.xepLoaiHocLuc()
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv != None:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            sv.xepLoaiHocLuc()

    def deleteSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv != None:
            self.listSinhVien.remove(sv)

    def findByID(self, ID):
        searchResult = None
        for sv in self.listSinhVien:
            if sv.getID() == ID:
                searchResult = sv
                break
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        for sv in self.listSinhVien:
            if keyword.upper() in sv.getName().upper():
                listSV.append(sv)
        return listSV

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    def showSinhVien(self, listSV):
        if len(listSV) == 0:
            print("Danh sach sinh vien trong!")
        else:
            print(f"{'ID':<8} {'Name':<18} {'Sex':<8} {'Major':<20} {'Diem TB':<10} {'Hoc Luc':<8}")
            for sv in listSV:
                print(f"{sv.getID():<8} {sv.getName():<18} {sv.getSex():<8} {sv.getMajor():<20} {sv.getDiemTB():<10} {sv.getHocLuc():<8}")

    def getListSinhVien(self):
        return self.listSinhVien