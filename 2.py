from PIL import Image

a=input("К какому празднику нужна открытка? ")
dictionary = {"Новый год": "нг.jpg", "8 марта": "8.jpg","Пасха": "пасха.jpg"}

if a in dictionary:
    b = dictionary[a]
    dictionary = Image.open(b)
    dictionary.show()
else:
    print("Извините, открытки для данного праздника не найдено.")