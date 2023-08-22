import os
dir_path = r'C:\Users\user\PycharmProjects\Class1\filehandling'
def txt_file(dir_path):
    text_file_count=[file for file in os.listdir(dir_path) if file.endswith('.txt')]
    print(text_file_count)

file_list=txt_file(dir_path)