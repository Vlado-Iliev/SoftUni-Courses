from pyfiglet import figlet_format


def message_art(msg):
    asci_art = figlet_format(msg)
    return asci_art


print(message_art(input()))
