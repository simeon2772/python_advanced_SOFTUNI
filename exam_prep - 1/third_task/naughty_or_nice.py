def naughty_or_nice_list(kids_list, *args, **kwargs):
    nice_list = []
    naughty_list = []
    not_found_list = []
    for kid in kids_list:
        if isinstance(kid, tuple) and len(kid) == 2 and isinstance(kid[0], int) and isinstance(kid[1], str):
            found = False
            for arg in args:
                if isinstance(arg, str) and '-' in arg:
                    count, status = arg.split('-')
                    if status.lower() == 'nice' and int(count) == kid[0]:
                        if kids_list.count(kid) == 1:
                            nice_list.append(kid[1])
                            kids_list.remove(kid)
                            found = True
                    elif status.lower() == 'naughty' and int(count) == kid[0]:
                        if kids_list.count(kid) == 1:
                            naughty_list.append(kid[1])
                            kids_list.remove(kid)
                            found = True
            for key, value in kwargs.items():
                if isinstance(key, str) and isinstance(value, str) and key == kid[1]:
                    if kids_list.count(kid) == 1:
                        if value.lower() == 'nice':
                            nice_list.append(kid[1])
                            kids_list.remove(kid)
                            found = True
                        elif value.lower() == 'naughty':
                            naughty_list.append(kid[1])
                            kids_list.remove(kid)
                            found = True
            if not found:
                not_found_list.append(kid[1])
    return '\n'.join(['Nice: ' + ', '.join(nice_list), 'Naughty: ' + ', '.join(naughty_list),
                      'Not found: ' + ', '.join(not_found_list)])


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
