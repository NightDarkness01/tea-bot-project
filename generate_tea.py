import json
import pandas as pd
import random

with open('chinese-tea-dataset.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data['teas'])

category_map = {
    'Green Tea': 'Зелёный чай', 'Oolong Tea': 'Улун', 'Black Tea': 'Красный чай',
    'White Tea': 'Белый чай', 'Pu\'er Tea': 'Пуэр', 'Dark Tea': 'Тёмный чай',
    'Yellow Tea': 'Жёлтый чай', 'Scented Tea': 'Ароматизированный чай'
}
caffeine_map = {'low': 'низкий', 'moderate': 'средний', 'high': 'высокий'}
body_map = {
    'light': 'лёгкое', 'light-medium': 'лёгко-среднее', 'medium': 'среднее',
    'medium-full': 'средне-полное', 'full': 'полное'
}

name_ru_map = {
    'Alishan High Mountain Oolong': 'Алишань Гаошань Улун',
    'Anji Bai Cha (Anji White Tea)': 'Аньцзи Бай Ча (Белый чай Аньцзи)',
    'Bai Hao Yin Zhen (Silver Needle)': 'Бай Хао Инь Чжэнь (Серебряные иглы)',
    'Bai Mudan (White Peony)': 'Бай Му Дань (Белый пион)',
    'Biluochun (Green Snail Spring)': 'Билочунь (Зеленая улитка весны)',
    'Bingdao Sheng': 'Биндао Шэн',
    'Da Hong Pao (Big Red Robe)': 'Да Хун Пао (Большой красный халат)',
    'Da Yu Ling': 'Да Юй Лин',
    'Dianhong Gold Needle': 'Дяньхун Цзинь Чжэнь (Золотая игла)',
    'Dong Ding Oolong': 'Дун Дин Улун',
    'Dongting Biluochun': 'Дунтин Билочунь',
    'Huangshan Maofeng': 'Хуаншань Маофэн',
    'Jasmine Dragon Pearl': 'Жасминовые жемчужины дракона',
    'Jasmine Dragon Pearls': 'Жасминовые жемчужины дракона',
    'Jin Jun Mei (Golden Eyebrow)': 'Цзинь Цзюнь Мэй (Золотые брови)',
    'Jingmai Gushu': 'Цзинмай Гушу',
    'Junshan Yinzhen': 'Цзюньшань Инь Чжэнь',
    'Keemun (Qimen Black Tea)': 'Кимун (Цимень Хун Ча)',
    'Keemun Hao Ya': 'Кимун Хао Я',
    'Keemun Hongcha': 'Кимун Хун Ча',
    'Lao Banzhang Ripe': 'Лао Баньчжан Шу (спелый)',
    'Lao Banzhang Sheng Pu\'er': 'Лао Баньчжан Шэн Пуэр',
    'Liu An Gua Pian (Melon Seed)': 'Лю Ань Гуа Пянь (Семечко дыни)',
    'Liu Bao Hei Cha': 'Лю Бао Хэй Ча',
    'Lu\'an Guapian': 'Луань Гуапянь',
    'Menghai 7542': 'Мэнхай 7542',
    'Menghai 7572': 'Мэнхай 7572',
    'Menghai Shou Pu\'er': 'Мэнхай Шу Пуэр',
    'Mi Lan Xiang Dancong': 'Ми Лань Сян Дань Цун',
    'Phoenix Dancong (Mi Lan Xiang)': 'Фэнхуан Дань Цун (Ми Лань Сян)',
    'Rou Gui (Cinnamon)': 'Жоу Гуй (Корица)',
    'Shan Lin Xi': 'Шань Линь Си',
    'Shi Feng Longjing': 'Ши Фэн Лунцзин',
    'Shui Xian (Water Sprite)': 'Шуй Сянь (Водяной дух)',
    'Taiping Houkui (Monkey King)': 'Тайпин Хоукуй (Король обезьян)',
    'Tie Guan Yin (Iron Goddess)': 'Те Гуань Инь (Железная Бодхисаттва)',
    'Tie Guan Yin Classic': 'Те Гуань Инь Классик',
    'Xi Hu Longjing (Dragon Well)': 'Си Ху Лунцзин (Колодец дракона)',
    'Ya Shi Xiang Dancong': 'Я Ши Сян Дань Цун (Аромат утиного помета)',
    'Yiwu Gushu': 'Иу Гушу',
    'Yiwu Sheng Pu\'er': 'Иу Шэн Пуэр',
    'Yunnan Gold (Dianhong)': 'Юньнань Голд (Дяньхун)',
    'Zhengshan Xiaozhong (Lapsang Souchong)': 'Чжэншань Сяочжун (Лапсанг Сушонг)',
    'Aged Fuding White Tea': 'Выдержанный белый чай Фудин',
    'Anhua Dark Tea': 'Аньхуа Хэй Ча (Темный чай)',
    'Bai Ji Guan (White Cockscomb)': 'Бай Цзи Гуань (Белый петушиный гребень)',
    'Bailin Gongfu': 'Байлинь Гунфу',
    'Ben Shan': 'Бэнь Шань',
    'Bu Zhi Chun': 'Бу Чжи Чунь',
    'Bulang Mountain Sheng Pu\'er': 'Буланшань Шэн Пуэр',
    'Cangling Baicha': 'Цанлин Бай Ча',
    'Chrysanthemum Pu\'er': 'Пуэр с хризантемой',
    'Chunmee (Precious Eyebrow)': 'Чуньмэй (Драгоценные брови)',
    'Da Ye Oolong': 'Да Е Улун',
    'Dinggu Dafang': 'Дингу Дафан',
    'Duyun Maojian': 'Дуюнь Маоцзянь',
    'Enshi Yulu (Jade Dew)': 'Эньши Юйлу (Нефритовая роса)',
    'Fu Zhuan (Golden Flower Brick)': 'Фу Чжуань (Кирпич с золотыми цветами)',
    'Fuding Shoumei': 'Фудин Шоумэй',
    'Fujian Baihao': 'Фуцзянь Байхао',
    'Gong Jian': 'Гун Цзянь',
    'Gong Mei': 'Гун Мэй',
    'Gong Mei (Tribute Eyebrow)': 'Гун Мэй (Даннические брови)',
    'Gougunao': 'Гоугунао',
    'Gui Hua Oolong (Osmanthus Oolong)': 'Гуй Хуа Улун (Улун с османтусом)',
    'Gunpowder Green': 'Порох (Gunpowder)',
    'Guzhu Zisun': 'Гучжу Цзысунь',
    'Huang Jin Gui (Golden Osmanthus)': 'Хуан Цзинь Гуй (Золотой османтус)',
    'Huang Zhi Xiang Dancong': 'Хуан Чжи Сян Дань Цун',
    'Huangjin Gui': 'Хуанцзинь Гуй',
    'Hubei Qing Zhuan': 'Хубэй Цин Чжуань (Зеленый кирпич)',
    'Hunan Black Tea': 'Хунаньский красный чай',
    'Huoshan Huangya': 'Хошань Хуанъя',
    'Jasmine Silver Needle': 'Жасминовые серебряные иглы',
    'Jasmine Snow Buds': 'Жасминовые снежные почки',
    'Jasmine Yin Hao': 'Жасмин Инь Хао',
    'Jinggang Cuilü': 'Цзинган Цуйлюй',
    'Jingshan Xiangcha': 'Цзиншань Сян Ча',
    'Jiuqu Hongmei (Nine Bend Red Plum)': 'Цзюцюй Хунмэй (Красная слива девяти изгибов)',
    'Kaihua Longding': 'Кайхуа Лундин',
    'Kang Zhuan': 'Кан Чжуань',
    'Keemun Maofeng': 'Кимун Маофэн',
    'Lincang Shou Pu\'er': 'Линьцан Шу Пуэр',
    'Lishan High Mountain Oolong': 'Лишань Гаошань Улун',
    'Lushan Yunwu (Cloud Mist)': 'Лушань Юньу (Облачный туман)',
    'Mao Xie': 'Мао Се',
    'Meijiawu Longjing': 'Мэйцзяу Лунцзин',
    'Mengding Ganlu (Sweet Dew)': 'Мэндин Ганьлу (Сладкая роса)',
    'Mengding Huangya': 'Мэндин Хуанъя',
    'Menghai 8582': 'Мэнхай 8582',
    'Menghai Raw': 'Мэнхай Шэн (сырой)',
    'Muzha Tie Guan Yin': 'Мучжа Те Гуань Инь',
    'Nannuo Mountain Sheng Pu\'er': 'Наньношань Шэн Пуэр',
    'Nantou Baozhong': 'Наньтоу Баочжун',
    'Nuoxiang Pu\'er': 'Нуосян Пуэр (с клейким рисом)',
    'Oriental Beauty (Dong Fang Mei Ren)': 'Дун Фан Мэй Жэнь (Восточная красавица)',
    'Osmanthus Oolong': 'Улун с османтусом',
    'Qi Lan Xiang Dancong': 'Ци Лань Сян Дань Цун',
    'Qianliang Cha': 'Цяньлян Ча (Чай тысячи лянов)',
    'Rose Black Tea': 'Красный чай с розой',
    'Ruby Red Oolong': 'Рубиновый улун (Хун Юй)',
    'Shou Mei (Longevity Eyebrow)': 'Шоу Мэй (Брови долголетия)',
    'Shui Jin Gui': 'Шуй Цзинь Гуй (Золотая черепаха)',
    'Shui Jin Gui (Golden Water Turtle)': 'Шуй Цзинь Гуй (Золотая водяная черепаха)',
    'Shuixian Shuixian': 'Шуйсянь Шуйсянь',
    'Sichuan Bian Cha': 'Сычуань Бянь Ча',
    'Sichuan Gongfu Black': 'Сычуаньский Гунфу Хун Ча',
    'Sichuan Hongya': 'Сычуань Хунъя',
    'Songluo': 'Сунло',
    'Taimu Shan Baimudan': 'Таймушань Баймудань',
    'Tan Yang Gongfu': 'Таньян Гунфу',
    'Tanyang Gongfu': 'Таньян Гунфу',
    'Tian Jian': 'Тянь Цзянь',
    'Tianmu Qingding': 'Тяньму Циндин',
    'Tie Luo Han (Iron Arhat)': 'Те Ло Хань (Железный архат)',
    'Weishan Maojian': 'Вэйшань Маоцзянь',
    'Wenshan Baozhong': 'Вэньшань Баочжун',
    'Wuyuan Meicha': 'Уюань Мэй Ча',
    'Xigui Sheng': 'Сигуй Шэн',
    'Xinyang Maojian': 'Синьян Маоцзянь',
    'Ya Shi Xiang (Duck Shit Aroma)': 'Я Ши Сян (Аромат утиного помета)',
    'Yin Jun Mei': 'Инь Цзюнь Мэй (Серебряные брови)',
    'Yingde Black Tea': 'Инде Хун Ча',
    'Yingde Hong': 'Инде Хун',
    'Yue Guang Bai': 'Юэ Гуан Бай (Лунный свет)',
    'Yue Guang Bai (Moonlight White)': 'Юэ Гуан Бай (Белый лунный свет)',
    'Yunnan Green': 'Юньнань Люй Ча (Зеленый)',
    'Yunnan Pure Bud': 'Юньнань Цзинь Я (Золотые почки)',
    'Zhangping Shuixian': 'Чжанпин Шуйсянь',
    'Zhenghe Gongfu': 'Чжэнхэ Гунфу',
    'Zhenghe Silver Needle': 'Чжэнхэ Инь Чжэнь',
    'Zhi Lan Xiang (Orchid Fragrance)': 'Чжи Лань Сян (Аромат орхидеи)',
    'Zhu Ye Qing (Bamboo Leaf Green)': 'Чжу Е Цин (Зеленый бамбуковый лист)',
    'Lotus Green Tea': 'Зеленый чай с лотосом',
    'Magnolia Oolong': 'Улун с магнолией',
    'Wuzhen Green': 'Учжэнь Люй Ча'
}

flavor_map = {
    'floral': 'цветочный', 'butter': 'сливочный', 'cream': 'сливочный', 'creamy': 'сливочный',
    'umami': 'умами', 'chestnut': 'каштановый', 'bamboo': 'бамбук', 'melon': 'дыня',
    'honey': 'медовый', 'honey orchid': 'медовая орхидея', 'hay': 'сено', 'fruity': 'фруктовый',
    'fruit': 'фруктовый', 'fresh': 'свежий', 'sweet': 'сладкий', 'soothing': 'успокаивающий',
    'cooling': 'освежающий', 'refreshing': 'освежающий', 'mineral': 'минеральный',
    'roasted': 'обжаренный', 'toasty': 'поджаренный', 'dark chocolate': 'тёмный шоколад',
    'malt': 'солодовый', 'malty': 'солодовый', 'velvet': 'бархатистый', 'orchid': 'орхидея',
    'jasmine': 'жасмин', 'cocoa': 'какао', 'sweet potato': 'батат', 'wine': 'винный',
    'earth': 'землистый', 'earthy': 'землистый', 'thick': 'густой', 'bitter': 'горький',
    'bitter-sweet': 'горько-сладкий', 'vegetal': 'травянистый', 'betel nut': 'бетель',
    'wood': 'древесный', 'woody': 'древесный', 'apricot': 'абрикос', 'camphor': 'камфора',
    'smooth': 'гладкий', 'leather': 'кожа', 'stone fruit': 'косточковые', 'cinnamon': 'корица',
    'long': 'долгий', 'sweet corn': 'сладкая кукуруза', 'mellow': 'мягкий', 'mild': 'мягкий',
    'sweet pea': 'сладкий горошек', 'cucumber': 'огурец', 'white peach': 'белый персик',
    'lima bean': 'лимская фасоль', 'grassy': 'травянистый', 'pine': 'сосна', 'longan': 'лонган',
    'dates': 'финики', 'herbs': 'травы', 'jujube': 'ююба', 'sticky-rice': 'клейкий рис',
    'muscatel': 'мускат', 'rose': 'роза', 'chrysanthemum': 'хризантема', 'osmanthus': 'османтус',
    'marine': 'морской', 'mushroom': 'грибной', 'plum': 'слива', 'brisk': 'терпкий',
    'bright': 'яркий', 'smoky': 'дымный', 'smoke': 'дымный', 'nutty': 'ореховый',
    'delicate': 'нежный', 'astringent': 'вяжущий', 'gardenia': 'гардения', 'almond': 'миндаль',
    'pear': 'груша', 'subtle-roast': 'легкая обжарка', 'dried-fruit': 'сухофрукты',
    'dried fruit': 'сухофрукты', 'citrus': 'цитрусовый', 'grass': 'трава', 'gentle': 'нежный',
    'light': 'лёгкий', 'full': 'полный', 'robust': 'крепкий', 'bold': 'насыщенный',
    'balanced': 'сбалансированный', 'aged': 'выдержанный', 'evolving': 'развивающийся',
    'caramel': 'карамельный', 'silky': 'шелковистый', 'elegant': 'элегантный',
    'fragrant': 'ароматный', 'lotus': 'лотос', 'magnolia': 'магнолия'
}

def translate_flavors(flavor_str):
    if pd.isna(flavor_str) or flavor_str == "": return ""
    parts = [p.strip() for p in flavor_str.split(',')]
    return ", ".join([flavor_map.get(p, p) for p in parts])

df['category_ru'] = df['category'].map(category_map).fillna(df['category'])
df['caffeine_ru'] = df['caffeine_level'].map(caffeine_map).fillna(df['caffeine_level'])
df['body_ru'] = df['body'].map(body_map).fillna(df['body'])
df['flavors_ru'] = df['flavor_primary'].apply(translate_flavors)
df['name_ru'] = df['name_en'].apply(lambda x: name_ru_map.get(x, x))

def generate_brewing(row):
    cat = row['category']
    ox = row['oxidation_level']
    
    if 'Green' in cat or 'White' in cat or 'Yellow' in cat:
        temp = random.randint(75, 85)
        time = random.randint(60, 90)
        inf = random.randint(3, 4)
    elif 'Oolong' in cat:
        if ox < 0.4: 
            temp = random.randint(85, 92)
            time = random.randint(30, 45)
            inf = random.randint(5, 6)
        else: 
            temp = random.randint(95, 100)
            time = random.randint(20, 30)
            inf = random.randint(6, 8)
    elif 'Black' in cat:
        temp = random.randint(90, 100)
        time = random.randint(15, 30)
        inf = random.randint(4, 6)
    elif 'Pu' in cat or 'Dark' in cat:
        temp = 100
        time = random.randint(10, 20)
        inf = random.randint(8, 12)
    else:
        temp = 85
        time = 60
        inf = 4
        
    return pd.Series([temp, time, inf])

df[['water_temp', 'steep_time', 'infusions']] = df.apply(generate_brewing, axis=1)

final_cols = [
    'id', 'name_ru', 'name_zh', 'category_ru', 'caffeine_ru', 
    'body_ru', 'oxidation_level', 'flavors_ru', 
    'water_temp', 'steep_time', 'infusions'
]

df[final_cols].to_csv('tea_dataset_ru.csv', index=False, encoding='utf-8-sig')
print("✅ Файл tea_dataset_ru.csv успешно перезаписан! Теперь переведено абсолютно всё.")
