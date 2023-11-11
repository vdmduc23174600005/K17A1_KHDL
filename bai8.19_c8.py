def dao_nguoc_va_loai_bo_so_chan(danh_sach):
    danh_sach_dao_nguoc = danh_sach[::-1]  # Đảo ngược danh sách
    danh_sach_le = [x for x in danh_sach_dao_nguoc if x % 2 != 0]  # Loại bỏ các số chẵn
    return danh_sach_le

danh_sach_so = []
while True:
    so = input("Nhập số (Enter để kết thúc): ")
    if so == "":
        break
    so = int(so)
    danh_sach_so.append(so)

ket_qua = dao_nguoc_va_loai_bo_so_chan(danh_sach_so)
print("Dãy số lẻ đảo ngược:", ket_qua)