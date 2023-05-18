from pyfiglet import figlet_format


def print_func(text):
    art = figlet_format(text)
    return art


print(print_func("Simeon"))
