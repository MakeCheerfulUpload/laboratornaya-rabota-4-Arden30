import re

def json_to_yaml_reg():
    js, ym = open("timetable.json", 'r', encoding="utf-8"), open("timetable_reg.yaml", 'w', encoding="utf-8")
    s = js.read().split('\n')
    del s[0]

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
        tmp = s[i].strip()
        tmp = re.sub(r"[\"{}\[\]]", r"", s[i]).strip()
        final = re.sub(r",$", r"", tmp)
        if final != (" " * len(final)) and ( ("[" in s[i-2]) or ("}," in s[i-2]) ):
            ym.write((cnt - k) * " " + "- " + final + "\n")
        elif final != (" " * len(final)):
            ym.write(cnt * " " + final + "\n")
json_to_yaml_reg()