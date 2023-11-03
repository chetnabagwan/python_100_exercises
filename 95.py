line=input("Enter comma separated values: ")
line_list=line.split(",")
with open ("user_data_commmas.txt","a+") as file:
    for i in line_list:
        file.write(i+"\n")
