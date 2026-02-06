import qrcode
user=input("enter a text or url:")
my_qr=qrcode.make(user)
my_qr.save("my_qr.png")