def next_version(version):
    version = int(''.join(version))
    new_version = version + 1
    return '.'.join(str(new_version))

current_version = input().split('.')
print(next_version(current_version))

