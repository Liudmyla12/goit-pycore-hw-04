from typing import Tuple, List, Dict

# -------- Парсер вводу --------
def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """
    Парсить рядок користувача на команду та аргументи.
    Повертає: (command, args_list)
    """
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.strip().lower(), args

# -------- Обробники команд (повертають повідомлення як str) --------
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        return "Usage: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        return "Usage: change <name> <new_phone>"
    name, new_phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = new_phone
    return "Contact updated."

def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 1:
        return "Usage: phone <name>"
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]

def show_all(_: List[str], contacts: Dict[str, str]) -> str:
    if not contacts:
        return "No contacts."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)

# -------- Головний цикл --------
def main() -> None:
    contacts: Dict[str, str] = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
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
            print(show_all(args, contacts))
        elif command == "":
            continue
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
