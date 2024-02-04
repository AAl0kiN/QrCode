import qrcode

# link to make code
def makeQr():
    address = input("Enter web address:")

    qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                     box_size=10,
                     border = 4,
                  )

    qr.add_data(address)
    qr.make(fit = True)

    codeBox = qr.make_image(fill_color = "black", back_color = "white")

    nameQr = input("Insert a name of your QR:"
    nameCode = nameQr + ".png"
    codeBox.save(nameCode)

    print("QR code generated successfully!")

if __name__ == "__main__":
    makeQr()

#NiCo

