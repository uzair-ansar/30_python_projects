import os
import random
import string
import qrcode

class MyQR:
    def __init__(self, size, padding):
        self.qr = qrcode.QRCode(size, padding)

    def create_whatsapp_qr(self):
        while True:
            user_input = input("Enter phone number (or type 'exit' to quit): ")

            if user_input.lower() == 'exit':
                print("Exiting...")
                break

            try:
                # Ensure the user input is a valid phone number
                if not user_input.isdigit():
                    print("Invalid phone number. Please enter digits only.")
                    continue

                # Construct the WhatsApp URL
                whatsapp_url = f"wa.me/91{user_input}"

                self.qr.clear()
                self.qr.add_data(whatsapp_url)
                self.qr.make(fit=True)

                # Generate filename from the first 4 characters of the user input
                base_filename = user_input[:4] + '_whatsapp_qr.png'

                # Check if the file already exists
                filename = base_filename
                counter = 1
                while os.path.exists(filename):
                    # If file exists, append 4 random digits to the filename
                    random_digits = ''.join(random.choices(string.digits, k=4))
                    filename = f"{base_filename}_{random_digits}.png"
                    counter += 1

                # Create an image with specified colors
                qr_image = self.qr.make_image(fill_color='black', back_color='white')
                qr_image.save(filename)

                print(f"WhatsApp QR generated successfully: {filename}")

                generate_another = input("Do you want to generate another WhatsApp QR code? (y/n): ")
                if generate_another.lower() != 'y':
                    print("Exiting...")
                    break

            except Exception as e:
                print(f"Error {e}")

def main():
    myqr = MyQR(30, 2)
    myqr.create_whatsapp_qr()

if __name__ == '__main__':
    main()
