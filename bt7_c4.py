def tinh_tong_chu_so(N):
    chuoi_so = str(N)
    tong = 0
    for chu_so in chuoi_so:
        tong += int(chu_so)
    return tong
so_N = 2022
tong_chu_so = tinh_tong_chu_so(so_N)
print(f"Tổng các chữ số của số {so_N} là: {tong_chu_so}")