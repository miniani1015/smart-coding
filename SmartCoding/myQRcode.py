import qrcode

file_path = r'QRCODE\\qrlist.txt'
f = open(file_path, 'rt', encoding='UTF8')
lines = f.readlines()

for line in lines :
    line = line.strip()
    qr_img = qrcode.make(line)
    save_path = '.\\QRCODE\\' + line + '.png'
    qr_img.save(save_path)
    
f.close()