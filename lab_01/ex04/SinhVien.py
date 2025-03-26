class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocLuc = ""

    def xepLoaiHocLuc(self):
        if self._diemTB >= 8:
            self._hocLuc = "Gioi"
        elif self._diemTB >= 6.5:
            self._hocLuc = "Trung binh"
        else:
            self._hocLuc = "Yeu"
    
    def getID(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getSex(self):
        return self._sex
    
    def getMajor(self):
        return self._major
    
    def getDiemTB(self):
        return self._diemTB
    
    def getHocLuc(self):
        return self._hocLuc