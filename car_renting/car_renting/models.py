from django.db import connections
from django.db import models

class DonThueXe(models.Model):
    dId = models.CharField(max_length=20)
    dId = models.CharField(max_length=50)
    dId = models.CharField(max_length=50)
    dNgaythue = models.DateField()
    dThoigian = models.IntegerField()
    dTrangthai = models.CharField(max_length=50)
    # Ket noi den bang "don_thue_xe" trong CSDL
    class Meta:
        db_table = 'don_thue_xe'

class HangXe(models.Model):
    hxId = models.CharField(max_length=20)
    hxTen = models.CharField(max_length=50)
    hxWebsite = models.CharField(max_length=50)
    # Ket noi den bang "hang_xe" trong CSDL
    class Meta:
        db_table = 'hang_xe'

class HopDongThueXe(models.Model):
    hdId = models.CharField(max_length=20)
    hdDonthue = models.CharField(max_length=50)
    hdKhachhang = models.CharField(max_length=50)
    hdMauxe = models.CharField(max_length=50)
    hdNgaythue = models.DateField()
    hdNgaytra = models.DateField()
    hdGia = models.IntegerField()
    hdTrangthai = models.CharField(max_length=50)
    hdQuanly = models.CharField(max_length=50)
    # Ket noi den bang "hop_dong_thue_xe" trong CSDL
    class Meta:
        db_table = 'hop_dong_thue_xe'

class KhachHang(models.Model):
    khId = models.CharField(max_length=20)
    khTen = models.CharField(max_length=50)
    khTaikhoan = models.CharField(max_length=50)
    khGioitinh = models.CharField(max_length=50)
    khNgaysinh = models.DateField()
    khSdt = models.CharField(max_length=15)
    diachiChitiet = models.CharField(max_length=50)
    diachiQuanHuyen = models.CharField(max_length=50)
    diachiTinhThanhpho = models.CharField(max_length=50)
    # Ket noi den bang "khach_hang" trong CSDL
    class Meta:
        db_table = 'khach_hang'

class MauXe(models.Model):
    mxId = models.CharField(max_length=20)
    mxTen = models.CharField(max_length=50)
    mxNam = models.IntegerField()
    hxLoai = models.CharField(max_length=20)
    hxSoghe = models.IntegerField()
    hxHang = models.CharField(max_length=20)
    hxBienso = models.CharField(max_length=20)
    hxNhacungcap = models.CharField(max_length=20)
    mxSoluong = models.IntegerField()
    # Ket noi den bang "mau_xe" trong CSDL
    class Meta:
        db_table = 'mau_xe'

class NhaCungCap(models.Model):
    nccId = models.CharField(max_length=20)
    nccTen = models.CharField(max_length=50)
    nccSdt = models.CharField(max_length=50)
    diachiChitiet = models.CharField(max_length=50)
    diachiQuanHuyen = models.CharField(max_length=50)
    diachiTinhThanhpho = models.CharField(max_length=50)
    # Ket noi den bang "nha_cung_cap" trong CSDL
    class Meta:
        db_table = 'nha_cung_cap'

class QuanLy(models.Model):
    qlId = models.CharField(max_length=20)
    qlTen = models.CharField(max_length=50)
    qlTaikhoan = models.CharField(max_length=50)
    qlGioitinh = models.CharField(max_length=50)
    qlNgaysinh = models.DateField()
    qlSdt = models.CharField(max_length=15)
    qlEmail = models.CharField(max_length=50)
    diachiChitiet = models.CharField(max_length=50)
    diachiQuanHuyen = models.CharField(max_length=50)
    diachiTinhThanhpho = models.CharField(max_length=50)
    # Ket noi den bang "quan_ly" trong CSDL
    class Meta:
        db_table = 'quan_ly'

class TaiKhoan(models.Model):
    tkId = models.CharField(max_length=20)
    tkLoai = models.CharField(max_length=50)
    tkTendangnhap = models.CharField(max_length=50)
    tkMatkhau = models.CharField(max_length=50)
    tkTrangthai = models.CharField(max_length=50)
    # Ket noi den bang "tai_khoan" trong CSDL
    class Meta:
        db_table = 'tai_khoan'