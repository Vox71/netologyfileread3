import os


def files_size(file_list):
    content_list = []
    if file_list:
        for file in file_list:
            counter = 0
            content = ''
            with open(file, encoding='utf-8') as f:
                for line in f:
                    counter += 1
                    content += line
                content_list.append([f.name, counter, content])
        content_list.sort(key=lambda x: x[1])
        return content_list
    else:
        return None


def merge_files(sorted_list, file):
    with open(file, 'w', encoding='utf-8', ) as i:
        for element in sorted_list:
            for line in element:
                i.write(str(line) + '\n')
    return None


def get_list(extension):
    file_list = []
    with os.scandir() as files:
        for file in files:
            if file.name.endswith(extension):
                file_list.append(file.name)
    return file_list if len(file_list) > 0 else None


txt_files = '.txt'
result = 'result.txt'
input_file_list = get_list(txt_files)
sorted_list = files_size(input_file_list)
merge_files(sorted_list, result)