
def find_max_character(string: str):
    count_char = 0

    list_char = []
    for i in string:
        list_char.append(i)
    set_char = set(list_char)
    
    for char in set_char:
        if string.count(char) > count_char:
            count_char = string.count(char)
            max_char = char
            

    return count_char, max_char

if __name__=="__main__":
    input_string = input("Enter a string: ")
    count_char, max_char = find_max_character(input_string)
    print(f"ki tu xuat hien nhieu nhat la: {max_char} voi: {count_char} ki tu")

