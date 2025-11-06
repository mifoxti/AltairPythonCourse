def validate_email(email):
    errors = []

    if len(email) < 6:
        errors.append("Email должен содержать не менее 6 символов")

    if "@" not in email:
        errors.append("Email не может не содержать символ @")
    else:
        parts = email.split("@")
        if len(parts) != 2:
            errors.append("Некорректный формат email")
        else:
            domain = parts[1]
            if "." not in domain:
                errors.append("Доменная часть должна содержать точку")

    if " " in email:
        errors.append("Email не должен содержать пробелы")

    if len(errors) == 0:
        return True, ["Email корректен"]
    else:
        return False, errors


emails = [
    "user@example.com",
    'short@a',
    "ivalid-email",
    "user@domain",
    "email with space@example.com"
]

for email in emails:
    is_valid, message = validate_email(email)
    status = "👌" if is_valid else "😢"
    print(f"{status} {email}: {message}")
