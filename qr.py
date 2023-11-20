import qrcode

table=2
order="pasta"
img=qrcode.make(table)
img.save('order2.png')