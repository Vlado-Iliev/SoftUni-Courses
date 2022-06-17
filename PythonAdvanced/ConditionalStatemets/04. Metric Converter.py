number = float(input())
metric = input()
conv_metric = input()
output_number = 0
if metric == "m":
    if conv_metric == "cm":
        output_number = number * 100

    elif conv_metric == "mm":
        output_number = number * 1000
elif metric == "cm":
    if conv_metric == "mm":
        output_number = number * 10
    elif conv_metric == "m":
        output_number = number / 100
elif metric == "mm":
    if conv_metric == "cm":
        output_number = number / 10
    elif conv_metric == "m":
        output_number = number / 1000

print(f'{output_number:.3f}')
