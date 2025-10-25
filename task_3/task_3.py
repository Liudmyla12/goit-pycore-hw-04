import sys
from pathlib import Path
from colorama import init, Fore, Style

ICON_DIR = "📂"
ICON_FILE = "📜"

def print_directory_structure(path: Path, prefix: str = "") -> None:
    """
    Рекурсивно друкує структуру папки:
    - Папки — іншим кольором
    - Файли — іншим кольором
    """
    try:
        items = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    except PermissionError:
        print(prefix + Fore.RED + "⛔ Доступ заборонено" + Style.RESET_ALL)
        return
    except OSError as e:
        print(prefix + Fore.RED + f"⚠️ Помилка читання: {e}" + Style.RESET_ALL)
        return

    last_index = len(items) - 1
    for idx, item in enumerate(items):
        is_last = idx == last_index
        connector = "┗━ " if is_last else "┣━ "
        next_prefix = prefix + ("   " if is_last else "┃  ")

        if item.is_dir():
            print(prefix + Fore.GREEN + connector + ICON_DIR + " " + item.name + Style.RESET_ALL)
            print_directory_structure(item, next_prefix)
        else:
            print(prefix + Fore.BLUE + connector + ICON_FILE + " " + item.name + Style.RESET_ALL)

def main() -> None:
    init(autoreset=True)

    if len(sys.argv) != 2:
        print(
            Fore.RED + """Помилка: вкажіть шлях до директорії.
Приклад: python task_3.py C:\\Users\\User\\Desktop
Або:     python task_3.py .""" + Style.RESET_ALL
        )
        return

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + "Вказаний шлях не існує." + Style.RESET_ALL)
        return
    if not dir_path.is_dir():
        print(Fore.RED + "Вказаний шлях не веде до директорії." + Style.RESET_ALL)
        return

    # Корінь
    print(Fore.MAGENTA + f"📦 {dir_path.resolve().name}" + Style.RESET_ALL)
    print_directory_structure(dir_path)

if __name__ == "__main__":
    main()







