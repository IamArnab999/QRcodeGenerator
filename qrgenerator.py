import qrcode as qr
img = qr.make("https://www.linkedin.com/in/arnab-kanti-das-61b164259/")
img.save("my_linkedin_profile.png")