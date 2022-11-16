import re

js, csv = open("timetable.json", 'r', encoding="utf-8"), open("timetable.csv", 'w', encoding="utf-8")
s = js.read().split('\n')

for i in range(7, 14):
    # находим все слова в кавычках, которые будут в шапке таблицы
    tmp = re.search(r"\"\w*\"", s[i])
    # убираем кавычки
    if tmp:
        final = tmp[0].replace("\"", "")
        csv.write(final)
    # ставим запятые после каждого слова, кроме самого последнего (иначе переходим к следующей строке)
    if i < 13:
        csv.write(", ")
    else:
        csv.write("\n")

# цикл до строчек с }
for i in range(5, len(s) - 4):
    # ищем фразы в кавычках, идущие после двоеточий, не включая запятую в конце
    tmp = re.search(r"\: \"(?:\w+\W*\s*)*\"", s[i])
    if tmp:
        # если в !самой фразе есть запятая, то мы оставляем кавычки, иначе их можно убрать
        if ", " not in s[i]:
            new = tmp[0].replace(": ", "").replace("\"","")
        else:
            new = tmp[0].replace(": ", "")
        csv.write(new)
        # если следующая строка не }, то значит данное слово не последнее и нужно поставить запятую
        if "}" not in s[i + 1]:
            csv.write(",")
    # если в строчке "}," то переходим на новую строку
    if "}," in s[i]:
        csv.write("\n")

