def electron_distribution(x):
    full_shells = list()
    electrons_remaining = x
    current_shell = 1
    while electrons_remaining > 0:
        shell_capacity = 2 * (current_shell ** 2)
        if shell_capacity < electrons_remaining:
            full_shells.append(shell_capacity)
            electrons_remaining -= shell_capacity
        else:
            full_shells.append(electrons_remaining)
            electrons_remaining = 0
            break
        current_shell += 1

    return full_shells

number_of_electrons = int(input())
print(electron_distribution(number_of_electrons))
