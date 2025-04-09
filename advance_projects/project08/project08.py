## Project 8: QR code encoder/decoder Python Project
from datetime import datetime
import qrcode

from pyzbar.pyzbar import decode
from PIL import Image

def main():
    timestamp = int(datetime.now().timestamp())
    data = 'Don\'t Give Up, Keep Learning and Growing!'

    # simple_qr_code_generator(data, timestamp)
    # colorful_qr_code_generator(data, timestamp)
    qr_code_decoder()

def simple_qr_code_generator(data, timestamp):
    img = qrcode.make(data)
    img.save(f"C:/Users/Fahad/Desktop/Practice/python/GSIT/Assignments/advance_projects/qrimage/qr-{timestamp}.png")

def colorful_qr_code_generator(data, timestamp):
    qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color = 'red', back_color = 'white')
    img.save(f"C:/Users/Fahad/Desktop/Practice/python/GSIT/Assignments/advance_projects/qrimage/colorful-qr-{timestamp}.png")

def qr_code_decoder():
    img = Image.open(f"C:/Users/Fahad/Desktop/Practice/python/GSIT/Assignments/advance_projects/qrimage/qr-1744140164.png")
    result = decode(img)
    print("...result...", result)

if __name__ == '__main__':
    main()