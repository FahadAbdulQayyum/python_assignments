## Project 8: QR code encoder/decoder Python Project

def main():
    from datetime import datetime
    print('timestamp..', int(datetime.now().timestamp()))
    import qrcode
    data = 'Don\'t Give Up, Keep Learning and Growing!'

    img = qrcode.make(data)

    img.save(f"C:/Users/Fahad/Desktop/Practice/python/GSIT/Assignments/advance_projects/qrimage/qr-{int(datetime.now().timestamp())}.png")

if __name__ == '__main__':
    main()