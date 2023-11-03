def count_words(filepath):
    with open(filepath, 'r') as file:
        str = file.read()
        str_list = str.split(" ")
        return len(str_list)

print(count_words(r"C:\\Users\\cbagwan\Downloads\words1.txt"))