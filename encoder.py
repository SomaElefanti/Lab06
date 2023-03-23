# Soma Elefánti

def print_menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
def encode(password):
    password_list = [i for i in password]
    for j in range(len(password_list)):
        if 0 <= password_list[j] <= 6:
            password_list[j] = str(int(password_list[j]) + 3)
        elif password_list[j] == 7:
            password_list[j] = '0'
        elif password_list[j] == 8:
            password_list[j] = '1'
        elif password_list[j] == 9:
            password_list[j] = '2'
    password_new = ''.join(password_list)
    return password_new


if __name__ == '__main__':
    continuing = True
    while continuing:
        print_menu()
        option = int(input("Please enter an option:"))
        if option == 1:
            password = str(input("Please enter your password to encode:"))
            password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            pass
        elif option == 3:
            continuing = False


