# Декоратор для обробки помилок введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone, please."
        except IndexError:
            return "Not enough arguments. Try again."
    return inner

# Функція для обробки введеного рядка
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# Додавання контакту
@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError  # Викличе повідомлення "Give me name and phone, please."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Зміна існуючого контакту
@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError  # Викличе повідомлення "Give me name and phone, please."
    name, phone = args
    if name not in contacts:
        raise KeyError  # Викличе повідомлення "This contact does not exist."
    contacts[name] = phone
    return "Contact updated."

# Отримання номера контакту
@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    return contacts[name]

# Показати всі контакти
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
