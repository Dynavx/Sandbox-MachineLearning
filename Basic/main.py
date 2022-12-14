harga_apel = 5000
uang = 100000
input_jumlah = input('Mau berapa apel?: ')
jumlah = int(input_jumlah)
total_harga = harga_apel * jumlah

print('Anda akan membeli ' + str(jumlah) + ' apel')
print('Harga total adalah Rp. ' + str(total_harga))

if uang > total_harga:
    print('Anda telah membeli ' + str(jumlah) + ' apel')
    print('Uang Anda tinggal Rp. ' + str(uang - total_harga))
elif uang == total_harga:
    print('Anda telah membeli ' + str(jumlah) + ' apel')
    print('Dompet Anda sekarang kosong')
else:
    print('Uang Anda tidak mencukupi')
    print('Anda tidak dapat membeli apel sebanyak itu')