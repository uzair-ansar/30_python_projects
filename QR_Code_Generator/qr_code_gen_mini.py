import qrcode

class MyQR:
    def __init__(self, size, padding):
        self.qr = qrcode.QRCode(size, padding)

    def create_qr(self, file_name, fg, bg):
        user_input = input("Enter text to generate QR code: ")

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fillcolor=fg, back_color=bg)
            qr_image.save(file_name)
            print(f"QR generated successfully: ({file_name})")
        except Exception as e:
            print(f"Error {e}")

def main():
    myqr = MyQR(30, 2)
    myqr.create_qr('sample.png', 'black', 'green')

if __name__ == '__main__':
    main()
