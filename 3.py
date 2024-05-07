from PIL import Image, ImageDraw, ImageFont

dictionary = {
    "Новый год": "нг.jpg",
    "Пасха": "пасха.jpg",
    "8 марта": "8.jpg"
}

a = input("К какому празднику вам нужна открытка? ")
имя = input("Кого вы хотите поздравить? ")

if a in dictionary:
    b = dictionary[a]
    открытка = Image.open(b)

    draw = ImageDraw.Draw(открытка)
    шрифт = ImageFont.truetype("Intro.ttf", 30)
    текст = f"{имя}, поздравляю!"
    draw.text((100, 50), текст, fill="black", font=шрифт)

    newf = "new.png"
    открытка.save(newf)

    print(f"Открытка с текстом сохранена в файле: {newf}")
else:
    print("Извините, открытки для данного праздника не найдено.")