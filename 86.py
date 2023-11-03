checklist = ["Portugal", "Germany", "Munster", "Spain"]
 
with open(r"C:\\Users\\cbagwan\Downloads\\countries_clean.txt", "r") as file:
    content = file.readlines()
 
content = [i.rstrip('\n') for i in content]
checked = [i for i in content if i in checklist]
 
print(checked)