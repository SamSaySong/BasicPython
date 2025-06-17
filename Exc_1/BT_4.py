
def find_character(string: str):
    count_char = []
    list_char = []
    
    for i in string:
        list_char.append(i)
    set_char = set(list_char)
    
    for char in set_char:
        count_char.append([char, string.count(char)])
        
    return count_char

if __name__=="__main__":
    input_string = input("Enter a string: ")
    count_char = find_character(input_string)
    for char, count in count_char:
      
        print(f"ki tu: {char} xuat hien voi: {count} ki tu")
            
