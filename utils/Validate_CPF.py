import re


def validate_cpf(cpf):
    """Validates if a CPF is valid"""
    cpf = re.sub(r'\D', '', cpf)  # Remove all non-numeric characters

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # First check digit calculation
    total = sum(int(cpf[i]) * (10 - i) for i in range(9))
    check_digit1 = (total * 10 % 11) % 10

    # Second check digit calculation
    total = sum(int(cpf[i]) * (11 - i) for i in range(10))
    check_digit2 = (total * 10 % 11) % 10

    return check_digit1 == int(cpf[9]) and check_digit2 == int(cpf[10])