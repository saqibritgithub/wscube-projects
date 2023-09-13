import pyqrcode
content="thes is my content"
url=pyqrcode.create(content)
url.png("myqr.png",scale=5)
print("qr code is successfuly generated")