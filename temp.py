import json, os, re
from flask import Flask, render_template, request, url_for, redirect


english_json_url = os.path.join("static", "test.json")
english_data = json.load(open(english_json_url, encoding="utf8"))
print(type(english_data))
# str_english_data = str(english_data)
# print(type(str_english_data))
# print(str_english_data)

def clean_english_value(value):
    value = value.replace("\n\n", "<br>")
    value = value.replace("\n", "<br>")
    match = re.findall(r'(\d+\.)', value)
    for i in range(len(match)):
        replace_str = "</li><li>"
        if i == 0:
            replace_str = "<ol><li>"
        if i == (len(match) - 1):
            replace_str = "</li></ol>"
        elif int(match[i][:-1]) < int(match[i-1][:-1]):
            replace_str = "</li></ol><ol><li>"
        value = value.replace(match[i], replace_str, 1)
    return value


def fetch_word(input_word):
    word = input_word.strip()
    if word == '':
        return '<i> Xin mời nhập từ hoặc cụm từ cần tìm... </i>'
    else:
        word_lower = word.lower()
        # bangla_value = ''
        english_value = '' 
        if word_lower in english_data:
            print()
            english_value = clean_english_value(english_data[word_lower])
            # english_value = english_data[word_lower]
            # if word_lower in bangla_data:
            #     bangla_value = clean_bangla_value(bangla_data[word_lower])
            return '<p><font color="#7a00cc">' + english_value + '</font></p>' #+ bangla_value
        else:
            keys_list = [k for k, v in english_data.items() if word_lower in v]
            for i in keys_list:
                english_value = clean_english_value(english_data[i])
            return i + '<p><font color="#7a00cc">' + english_value + '</font></p>' #+ bangla_value



# print(fetch_word("face"))
print(fetch_word("viết gọn"))