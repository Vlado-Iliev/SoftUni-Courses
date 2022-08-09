def reverse_text(text):
    current_index = len(text) - 1

    while current_index > -1:
        symbol_to_return = text[current_index]
        yield symbol_to_return
        current_index -= 1



for char in reverse_text("step"):
    print(char, end='')