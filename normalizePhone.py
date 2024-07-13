import re


def normalize_phone(phone_number):
    pattern = r"[^\d]"
    modified_number = re.sub(pattern, "", str(phone_number)).removeprefix('38')

    result = "+38" + modified_number

    if len(result) != 13:
        return "It is not correct length number"

    return result
