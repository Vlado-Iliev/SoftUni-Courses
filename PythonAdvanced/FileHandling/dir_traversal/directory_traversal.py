from os import listdir
from os.path import isdir, join


def dir_traversal(path, dir_dict):
    files = listdir(path)
    for file in files:
        if isdir(join(path, file)):
            dir_traversal(join(path, file), dir_dict)
        else:
            file_extension = file.split('.')[-1]
            if file_extension not in dir_dict:
                dir_dict[file_extension] = []
            dir_dict[file_extension].append(file)


dir_dict = {}
dir_traversal('./', dir_dict)

for key, value in dir_dict.items():
    dir_dict[key] = sorted(value)

sorted_dict = dict(sorted(dir_dict.items(), key=lambda item: item[1]))

with open('./report.names.txt','w') as file:

    for key,value in sorted_dict.items():
        file.write(f'.{key}\n')
        for v in value:
                file.write(f'- - - {v}\n')