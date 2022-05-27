import random

animals = ["Животно",["Котка","та","f"],["Куче","то","n"],["Жаба","та","f"],["Носорог","а","m"],["Хамстер","а","m"],["Пингвин","а","m"], ["Костенурка","та","f"],["Таралеж","а","m"],["Риба","та","f"],["Полевка","та","f"],["Мишка","та","f"],["Паун","а","m"]]
colors = ["Цвят","Червен", "Син", "Зелен","Лилав","Черн","Жълт","Оранжев","Сив","Кафяв","Рижав"]
places = ["Място",["Парк","а"],["Море","то"],["Океан","а"],["Планина","та"],["Река","та"],["Зала","та"],["Пързалка","та"]]
human = ["Човек",["Печатар","я"],["Печатар","я"],["Певец","а"],["Футболист","а"],["Репортер","а"],["Фермер","а"]]
verbs = [{"Животно":[["плува","на воля", "бързо", "непохватно"],["пие","вода", "жадно", "рядко"],["обитава","предимно", "високо", "под земята"],["дълбае","дупки", "тунели", "за храна"],["ходи","бавно", "на криво", "изправено"],["вие","продължително", "силно", "жално"],["спи","зимен сън", "през деня", "дълго"]]},{"Човек":[["плува","разстояние", "далеч", "на сухо"],["пие","течности", "алкохол", "вода"],["тича","слепешката", "задъхано", "скоростно"],["ходи","пеш", "рядко", "на два крака"],["простира","пране", "на голяма площ", "ръцете си"],["пише","грозно", "красиво", "рядко"],["чете","книги", "фейсбук", "читанка"],["спи","малко", "много", "непробудно"]]}]
gen = {"m":"ия","f":"ата","n":"ото"}
message = ""
while message.lower() != "не":
    being = random.choice([animals,human])
    # being = being[random.randrange(1,len(being) - 1)]
    color = colors[random.randrange(1,len(colors) - 1)]
    place = places[random.randrange(1,len(places) - 1)]
    verb = random.choice(verbs)
    # verb = verb[1][random.randrange(1,len(verb[1]) - 1)]
    gens = gen[random.choice(["m","f","n"])]
    # print(being, color, place, verb, gen)
    story = ""
    if being[0] == "Човек":
        being = being[random.randrange(1, len(being) - 1)]
        animal = animals[random.randrange(1,len(animals) - 1)]
        animal_type = animal[0]
        animal_article = animal[1]
        ver_animal = random.choice(verbs[0]["Животно"])
        how_animal = random.choice(ver_animal[1:])
        ver = ver_animal[0]
        gen_animal = gen[animal[2]]
        place2 = places[random.randrange(1,len(places) - 1)]
        story = f"{being[0]} отиде на {place[0].lower()}, там видя {color.lower() + gen_animal} {animal[0].lower()} да {ver} {how_animal} в {place2[0].lower() + place2[1]}."
    if being[0] == "Животно":
        being = being[random.randrange(1, len(being) - 1)]
        gen_animal = gen[being[2]]
        ver_animal = random.choice(verbs[0]["Животно"])
        how_animal = random.choice(ver_animal[1:])
        place1 = random.choice(places[1:])
        place2 = random.choice(places[1:])
        while place2[0] == place1[0]:
            place2 = random.choice(places[1:])
        story = f"{color + gen_animal} {being[0].lower()} живее в {place[0].lower() + place[1]}. Обича да {ver_animal[0]} {how_animal} из {place1[0].lower() + place1[1]} или {place2[0].lower() + place2[1]}."
    replace_worthy = {"Сино":"Синьо", "сино":"синьо","Сина":"Синя","сина":"синя"}
    for k,v in replace_worthy.items():
        story = story.replace(k,v)
    print(story)
    if "стига" in message.lower():
        break
    message = input("\nИскате ли да продължите с други произволно избрани любопитни факти? \n(да(Enter)/не/стига толкова):")
    print()
    if "стига" in message:
        print("Само още веднъж и приключваме:")
        continue




