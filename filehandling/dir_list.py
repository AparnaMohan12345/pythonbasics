import os
dir_path = r'C:\Users\user\PycharmProjects\Class1\filehandling'

count =0
def list_files(dir_path):
    file=os.listdir(dir_path)
    return file
file_list = list_files(dir_path)
for i in file_list:
    print(i)
    count+=1
print(count)