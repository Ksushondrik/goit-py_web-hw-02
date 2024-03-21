import functions as fu


def main():
    book = fu.load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = fu.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "help":
            print(fu.help_command())
        elif command == "add":
            print(fu.add_contact(args, book))
        elif command == "change":
            print(fu.change_contact(args, book))
        elif command == "phone":
            print(fu.show_phone(args, book))
        elif command == "all":
            print(fu.show_all(book))
        elif command == "add-birthday":
            print(fu.add_birthday(args, book))
        elif command == "show-birthday":
            print(fu.show_birthday(args, book))
        elif command == "birthdays":
            print(fu.soon_birthdays(book))
        elif command == "del-phone":
            print(fu.delete_phone(args, book))
        elif command == "del-contact":
            print(fu.delete_contact(args, book))
        else:
            print("Invalid command. Enter 'help' for help)")
    fu.save_data(book)


if __name__ == "__main__":
    main()
