import pyqrcode
content="https://youtube.com/shorts/wSp4e-lTBVw?si=pTwngo20C-Dgi8yj"
url=pyqrcode.create(content)
url.png("myqr.png",scale=5)
print("https://youtube.com/shorts/wSp4e-lTBVw?si=pTwngo20C-Dgi8yj")