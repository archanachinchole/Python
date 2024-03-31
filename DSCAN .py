import qrcode

# Original URL to encode in the QR code
original_url = "https://openai.com/"

# Generate QR code
qr = qrcode.make(original_url)

# Save the QR code image
qr.save("openai_qr_code.png")

print("QR code generated successfully for OpenAI's website!")
