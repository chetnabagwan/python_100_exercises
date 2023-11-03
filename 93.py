import glob
 
file_list = glob.glob(r"C:\\Users\\cbagwan\Downloads\subdirs/**/*.py", recursive=True)
print(len(file_list))
