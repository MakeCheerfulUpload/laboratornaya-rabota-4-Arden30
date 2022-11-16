def json_to_yaml():
    js, ym = open("timetable.json", 'r', encoding="utf-8"), open("timetable.yaml", 'w', encoding="utf-8")
    s = js.read().split('\n')
    del s[0]

    # счетчик пробелов cnt, old_cnt нужен для правильного числа пробелов в текущей строчке, где была найдена {
    cnt, old_cnt = 0, 0
    k = 4

    for i in range(len(s)):
        if k == 2:
            k += 2
        if i > 10 and "day" in s[i]:
            k -= 2
        if "[" in s[i-1] or ("{" in s[i] and ":" in s[i]):
            cnt += 2
        if "}," in s[i]:
            cnt -= 2
        # убираем все пробелы перед строкой
        tmp = s[i].strip()
        #в начале ставятся пробелы (old_cnt штук), потом первый, второй и третиц replace убирают фигурные скобки,
        #четвертый убирает кавычку с запятой, пятый убирает просто кавычки
        final = tmp.replace('{', '').replace("},", '').replace('}', '').replace("\",", '').replace('\"', '').replace("[", '').replace("]", '')
        # передаем новое количество пробелов в переменную, которая отвечает за их расстановку в новой строке
        if final != (" " * len(final)) and ( ("[" in s[i-2]) or ("}," in s[i-2]) ):
            ym.write((cnt - k) * " " + "- " + final + "\n")
        elif final != (" " * len(final)):
            ym.write(cnt * " " + final + "\n")
json_to_yaml()
