import os
folder_name="lab_Programs"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

file1_path=os.path.join("file1.txt")
file2_path=os.path.join("file2.txt")
file3_path=os.path.join("file3.txt")

with open(file1_path,"w")as file1:
    file1.write("VTU")
with open(file2_path,"w")as file2:
    file2.write("UNIVERSITY")

with open(file1_path,"r")as file1, open(file2_path,"r")as file2:
    merged_content=file1.read()+" "+file2.read()

with open(file3_path,"w")as file3:
    file3.write(merged_content)

print("Files created and merged successfully")