def file_extractor(data):
    file = data[-1].split('.')
    name = file[0]
    extension = file[1]
    print(f'File name: {name} \nFile extension: {extension}')


data = input().split("\\")
file_extractor(data)