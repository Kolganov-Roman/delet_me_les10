#
# my_skills = {"python", "flask", "критическое мышление", "планирование", "переговоры", "html"}
# backend_skills = {"linux", "terminal", "python", "flask", "django", "restapi"}
# frontend_skills = {"html", "css", "javascript"}
# soft_skills = {"презентация", "планирование", "переговоры", "лидерство", "критическое мышление"}
#
# print(frontend_skills.difference(my_skills))
# print(my_skills.intersection(backend_skills))
# print(my_skills.difference(backend_skills.union(frontend_skills)))
# print(soft_skills.issubset(my_skills))
# print(backend_skills.union(frontend_skills))

# words = [
#     "разработчики", "сервисов", "ориентируются", "на", "скорость"
# ]
#
# words_with_letter = []
#
# for word in words:
#     if "р" in word:
#         words_with_letter.append(word)
#
# words_with_letter.sort()
#
# print(words_with_letter)


# store = {
#     "apples": {"name": "Яблоки", "price": "100", "available": 40},
#     "oranges": {"name": "Апельсины", "price": "200", "available": 20},
#     "pomegranate": {"name": "Гранаты", "price": "400", "available": 5},
# }
#
# stocktaking = {}
#
# for key, value in store.items():
#     stocktaking[key] = value['available']
#
# print(stocktaking)


coder_info = {
    "name": "Алексей",
    "languages": {
        "java": "beginner",
        "php": "middle",
        "python": "senior",
        "go": "none",
    }
}

coder_info_short = {
    "name": coder_info["name"],
    "languages": [],
}

for language, level in coder_info['languages'].items():
    if level in ("middle", "senior"):
        coder_info_short["languages"].append(language)

print(coder_info_short)

# import requests
#
# for x in range(3):
#     response = requests.get('https://catfact.ninja/fact')
#     fact = response.json()
#     print(f"{x + 1} - {fact['fact']}")



