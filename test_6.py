#root 所指的是当前正在遍历的这个文件夹的本身的地址
#dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
#files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
import os
root_path = os.getcwd()  #获取当前根文件的路径
offset = len(root_path.split("\\"))
for root,dirs,files in os.walk(root_path):  # 遍历文件夹
	current_dir = root
	path_list = current_dir.split("\\")
	indent_level = len(path_list) - offset
	print("\t"*indent_level,"\\",path_list[-1])
	for f in files:
		file_name = os.path.splitext(f)[0]  #文件名 文件扩展名 分离
		print("\t"*(indent_level+1),file_name)
#print(root_path)
#offset = len(root_path.split("\\"))

#print(root_path.split("\\")[-1])  #获取当前文件的路径
#print(root_path)
#for root,files,dir in os.walk(root_path):
	#print(root)