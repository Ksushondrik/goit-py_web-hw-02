import pickle

import decor as de
from classes import AddressBook, Record


def parse_input(user_input):  # виділення команди
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@de.input_error
def add_contact(args, book: AddressBook):  # додавання контакту в AddressBook
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@de.input_error
def change_contact(args, book: AddressBook):  # зміна номера телефону контакта
    name, phone, new_phone, *_ = args
    record = book.find(name)
    if isinstance(record, Record):
        record.edit_phone(phone, new_phone)
        return "Contact updated."
    else:
        raise Exception("Not found!")


@de.input_error
def show_phone(args, book: AddressBook):  # показати телефон певного контакта
    name, *_ = args
    record = book.find(name)
    if isinstance(record, Record):
        return f"Contact name: {record.name},\t phones: {'; '.join(phone.value for phone in record.phones)}"
    else:
        raise Exception("Not found!")


@de.input_error
def show_all(book: AddressBook):  # показати всі контакти з книги
    if len(book) > 0:
        for name, record in book.data.items():
            print(record)
        return f"It's all"
    else:
        raise Exception("No mach to show!")


@de.input_error
def add_birthday(args, book: AddressBook):  # додати дату народження
    name, date, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if isinstance(record, Record):
        record.add_birthday(date)
        return message
    else:
        raise Exception("Not found!")


@de.input_error
def show_birthday(args, book: AddressBook):  # показати дату народження певного контакту
    name, *_ = args
    record = book.find(name)
    if isinstance(record, Record):
        return f"Contact name: {record.name},\t birthday: {record.birthday}."
    else:
        raise Exception("Not found!")


@de.input_error
def soon_birthdays(book: AddressBook):  # список днів народження контактів, що припадають на найближчий тиждень
    congratulation_list = book.get_upcoming_birthdays()
    if not congratulation_list:
        return f"There are no birthday parties this week"
    else:
        print("List of greetings for the current week:")
        a = "Name"
        b = "Birthday"
        c = "Day_for_greetings"
        s = f"|| {a:>15} | {b:>20} | {c:>20} ||"
        print(s)
        for line in congratulation_list:
            a = line["Name"]
            b = line["Birthday"]
            c = line["Day_for_greetings"]
            s = f"|| {a:>15} | {b:>20} | {c:>20} ||"
            print(s)
        return f"It's all!"


def save_data(book, filename="addressbook.pkl"):  # збереження телефонної книги
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename="addressbook.pkl"):  # завантаження раніше збереженої телефонної книги
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено


def help_command():  # виведення списку команд з якими працює бот
    return """
    I understand these commands:
    "hello"
    "add [name] [phone]"
    "change [name] [old_phone] [new_phone]"
    "phone [name]"
    "all"
    "add-birthday [name] [birthday]"
    "show-birthday [name]"
    "birthdays"
    "del-phone [name] [phone]"
    "del-contact [name]"
    "exit/close"
    """


@de.input_error
def delete_phone(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    if isinstance(record, Record):
        record.remove_phone(phone)
        return "Contact updated."
    else:
        raise Exception("Not found!")


@de.input_error
def delete_contact(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if isinstance(record, Record):
        book.delete(name)
        return "Contact removed."
    else:
        raise Exception("Not found!")
