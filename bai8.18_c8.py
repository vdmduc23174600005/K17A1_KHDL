def kiem_tra_so_hoan_hao(n):
    tong_uoc_so = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc_so += i
    return tong_uoc_so == n

# Kiểm tra số hoàn hảo
so_can_kiem_tra = int(input("Nhập số kiểm tra xem hoàn hảo hay không:"))
if kiem_tra_so_hoan_hao(so_can_kiem_tra):
    print(so_can_kiem_tra, "là số hoàn hảo.")
else:
    print(so_can_kiem_tra, "không phải là số hoàn hảo.")