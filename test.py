import os
root_path = os.getcwd()  #获取当前根文件的路径
#print(root_path)
offset = len(root_path.split("\\"))
for root,dirs,files in os.walk(root_path):  # 遍历文件夹
	#print(root)
	current_dir = root.split("\\")
	indent_level = len(current_dir) - offset
	print(indent_level*"\t",current_dir[-1])
#print(root_path)
#offset = len(root_path.split("\\"))

#print(root_path.split("\\")[-1])  #获取当前文件的路径
#print(root_path)
#for root,files,dir in os.walk(root_path):
	#print(root)