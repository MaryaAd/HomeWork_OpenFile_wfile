import os
current = os.getcwd()
folder = 'primer_file'
full_path = os.path.join(current, folder)
files = os.listdir(full_path)

file_dict = {}
for f in files:
    every_path = os.path.join(full_path, f)
    with open(every_path, encoding='utf-8') as file:
        lines = file.readlines()
        len_lines = len(lines)
        text = []
        for line in lines:
            text.append(line.strip())
        file_dict[f] = (len_lines, text)

sorted_dict = {}
for i in sorted(file_dict.values()):
    for k in file_dict.keys():
        if file_dict[k] == i:
            sorted_dict[k] = file_dict[k]
            break
with open('new_text.txt', 'w', encoding='utf-8') as file:
    for key, value in sorted_dict.items():
        file.write(f'{key}\n')
        file.write(f'{value[0]}\n')
        for val in value[1]:
            file.write(f'{val}\n')