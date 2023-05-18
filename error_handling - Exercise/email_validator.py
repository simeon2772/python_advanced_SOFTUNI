from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


VALID_DOMAINS = ['.com', '.bg', '.net', '.org']
MIN_LENGTH = 4
pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'

email = input()

while email != 'End':
    try:
        if email.count('@') > 1:
            raise MoreThanOneAtSymbolError('Email should contain only one AtSymbol')
        if len(email.split('@')[0]) <= MIN_LENGTH:
            raise NameTooShortError(f'Name must be more than {MIN_LENGTH} characters')
        if findall(pattern_name, email)[0] != email.split('@'):
            raise InvalidNameError('Name can only contain ....')
        if '@' not in email:
            raise MustContainAtSymbolError('Email must contain @')
        if findall(pattern_domain, email)[-1] not in VALID_DOMAINS:
            raise InvalidDomainError(f'Domain must be one of the following: {", ".join(VALID_DOMAINS)}')

    except IndexError:
        print("Invalid email!")
    else:
        print('Email is valid!')

    email = input()
