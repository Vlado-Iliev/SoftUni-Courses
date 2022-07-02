symbols = {"-", ",", ".", "!", "?"}
with open('./text.txt', 'r') as file:
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            result = ' '.join(line.strip().split()[::-1])
            for sym in symbols:
                result = result.replace(sym, '@')

            print(result)
