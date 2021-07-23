def gender_converter(gender: str):
    gender = gender.upper()
    if gender == 'M':
        return 'MALE'
    elif gender == 'F':
        return 'FEMALE'
    else:
        return 'UNKNOWN'