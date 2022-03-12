# Подключаем модули
from PIL import Image
from IPython.display import display
import random
import json
import os


# Каждое изображение состоит из ряда черт
# Weightings - определяет редкость каждой черты и в сумме они должны быть 100%
# Если не упираться в максимум картинок, то можно меньше 100%

backgrounds = ["background_01", "background_02", "background_03"]
backgrounds_weights = [33, 33, 34]

bases = ["base_01", "base_02", "base_03", "base_04", "base_05"]
bases_weights = [20, 20, 20, 20, 20]

caps = ["cap_01", "cap_02", "cap_03", "cap_04"]
caps_weights = [25, 25, 25, 25]

flames = ["flame_01", "flame_02", "flame_03", "flame_04"]
flames_weights = [25, 25, 25, 25]

lines = ["lines_01", "lines_02", "lines_03", "lines_04", "lines_05"]
lines_weights = [20, 20, 20, 20, 20]

texts = ["text_01", "text_02", "text_03"]
texts_weights = [33, 33, 34]

shadow = ["shadow"]
shadow_weights = [100]


# Словарная переменная для каждого признака
# Каждая черта соответствует своему имени файла (первое имя мы задаем в коде сверху, а второе имя - это имя файла)

backgrounds_files = {
    "background_01": "background_01",
    "background_02": "background_02",
    "background_03": "background_03"
}

bases_files = {
    "base_01": "base_01",
    "base_02": "base_02",
    "base_03": "base_03",
    "base_04": "base_04",
    "base_05": "base_05"
}

caps_files = {
    "cap_01": "cap_01",
    "cap_02": "cap_02",
    "cap_03": "cap_03",
    "cap_04": "cap_04"
}

flames_files = {
    "flame_01": "flame_01",
    "flame_02": "flame_02",
    "flame_03": "flame_03",
    "flame_04": "flame_04"
}

lines_files = {
    "lines_01": "lines_01",
    "lines_02": "lines_02",
    "lines_03": "lines_03",
    "lines_04": "lines_04",
    "lines_05": "lines_05"
}

texts_files = {
    "text_01": "text_01",
    "text_02": "text_02",
    "text_03": "text_03"
}

shadow_files = {
    "shadow": "shadow_01"
}


# Генерируем черты

TOTAL_IMAGES = 100  # Число, отвечающее, за количество сгенерируемых картинок

all_images = []

# Рекурсивная функция для создания уникальных комбинаций изображений


def create_new_image():

    new_image = {}

    # Для каждой категории выбирает случайную черту по редкости weights
    new_image["Backgrounds"] = random.choices(
        backgrounds, backgrounds_weights)[0]
    new_image["Bases"] = random.choices(bases, bases_weights)[0]
    new_image["Caps"] = random.choices(caps, caps_weights)[0]
    new_image["Flames"] = random.choices(flames, flames_weights)[0]
    new_image["Lines"] = random.choices(lines, lines_weights)[0]
    new_image["Texts"] = random.choices(texts, texts_weights)[0]
    new_image["Shadow"] = random.choices(shadow, shadow_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


# Создаем уникальные комбинации черт
for i in range(TOTAL_IMAGES):

    new_trait_image = create_new_image()

    all_images.append(new_trait_image)

# Возвращает значение true, если все изображения уникальны


def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)


print("Are all images unique?", all_images_unique(all_images))
# Добовляем токен ID
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

print(all_images)


# Получаем количество черт

backgrounds_count = {}
for item in backgrounds:
    backgrounds_count[item] = 0

bases_count = {}
for item in bases:
    bases_count[item] = 0

caps_count = {}
for item in caps:
    caps_count[item] = 0

flames_count = {}
for item in flames:
    flames_count[item] = 0

lines_count = {}
for item in lines:
    lines_count[item] = 0

texts_count = {}
for item in texts:
    texts_count[item] = 0

shadow_count = {}
for item in texts:
    shadow_count[item] = 0

for image in all_images:
    backgrounds_count[image["Backgrounds"]] += 1
    bases_count[image["Bases"]] += 1
    caps_count[image["Caps"]] += 1
    flames_count[image["Flames"]] += 1
    lines_count[image["Lines"]] += 1
    texts_count[image["Texts"]] += 1

print(backgrounds_count)
print(bases_count)
print(caps_count)
print(flames_count)
print(lines_count)
print(texts_count)


# Генерируем изображения в папку, предварительно проверяем ее наличее

if not os.path.isdir(f'./finished_images'):
    os.mkdir(f'./finished_images')

for item in all_images:

    im1 = Image.open(
        f'./image/backgrounds/{backgrounds_files[item["Backgrounds"]]}.png').convert('RGBA')
    im2 = Image.open(
        f'./image/bases/{bases_files[item["Bases"]]}.png').convert('RGBA')
    im3 = Image.open(
        f'./image/caps/{caps_files[item["Caps"]]}.png').convert('RGBA')
    im4 = Image.open(
        f'./image/flames/{flames_files[item["Flames"]]}.png').convert('RGBA')
    im5 = Image.open(
        f'./image/lines/{lines_files[item["Lines"]]}.png').convert('RGBA')
    im6 = Image.open(
        f'./image/texts/{texts_files[item["Texts"]]}.png').convert('RGBA')
    im7 = Image.open(
        f'./image/shadow/{shadow_files[item["Shadow"]]}.png').convert('RGBA')

    # Наложение слоев друг на друга
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)
    com6 = Image.alpha_composite(com5, im7)

    # Конвертируем в RGB
    rgb_im = com5.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./finished_images/" + file_name)
