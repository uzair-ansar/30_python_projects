import qrcode

class MyQR:
    def __init__(self, size, padding):
        self.qr = qrcode.QRCode(size, padding)

    def create_qr(self):
        while True:
            user_input = input("Enter text to generate QR code (or type 'exit' to quit): ")

            if user_input.lower() == 'exit':
                print("Exiting...")
                break

            try:
                self.qr.clear()
                self.qr.add_data(user_input)
                self.qr.make(fit=True)

                # Generate filename from the first 4 characters of the user input
                filename = user_input[:4].replace(' ', '_') + '_qr.png'

                # Create an image with specified colors
                qr_image = self.qr.make_image(fill_color='black', back_color='white')
                qr_image.save(filename)

                print(f"QR generated successfully: {filename}")

                generate_another = input("Do you want to generate another QR code? (y/n): ")
                if generate_another.lower() != 'y':
                    print("Exiting...")
                    break

            except Exception as e:
                print(f"Error {e}")

def main():
    myqr = MyQR(30, 2)
    myqr.create_qr()

if __name__ == '__main__':
    main()
