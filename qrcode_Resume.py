import qrcode

# URL of your resume on Google Drive
resume_url = "https://www.linkedin.com/in/archana-chinchole-04208b269"

# Generate QR code
qr = qrcode.make(resume_url)

# Save QR code image
qr.save("resume_qr_code.png")

print("QR code for your resume generated successfully!")
