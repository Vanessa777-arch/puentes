import qrcode

# URL de tu aplicación Streamlit
url = "http://localhost:8501/"

# Generar el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Crear imagen del QR
img = qr.make_image(fill_color="black", back_color="white")
img.save("streamlit_qr.png")

print("Código QR generado y guardado como 'streamlit_qr.png'.")
