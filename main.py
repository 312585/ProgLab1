import re

fname = "steam_description_data.csv"

num_words = 0
num_chars = 0
num_chars_without_space = 0
num_chars_without_comma = 0
num_sent = 0

with open(fname, 'r', encoding="utf-8") as f:
    for line in f:
        words = line.split()
        num_words += len(words)
        num_chars += len(line)
        num_sent += line.count(".")
        num_chars_without_space += len(line.replace(" ", ""))
        num_chars_without_comma += len(re.sub("[^\w]", "", line.replace(" ", "_")))
print("общее количество символов в файле "+num_chars.__str__()+"\n")
print("общее количесто символов без пробелов "+num_chars_without_space.__str__()+"\n")
print("количество символов без знаков препинания "+num_chars_without_comma.__str__()+"\n")
print("количество слов в файле "+num_words.__str__()+"\n")
print("количество предложений "+num_sent.__str__()+"\n")
