from PIL import Image, ImageDraw, ImageFont
import pandas as tgnas
import os as o
#output folder path
o.makedirs("certificates", exist_ok=True)
names = tgnas.read_excel("names.xlsx")#input excel
font = ImageFont.truetype("LibreBaskerville-Regular.ttf", 40)
for name in names['Name']:
    img = Image.open("ss.png").convert("RGB")
    draw = ImageDraw.Draw(img)
    draw.text((835, 498), name, fill="black", font=font)
    img.save(f"certificates/{name}.png")
