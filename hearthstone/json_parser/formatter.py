import re


def get_key_value(entry, field):
    if field == "cardSet":
        field = "set"

    try:
        value = entry[field]
    except KeyError:
        return "NULL"

    if field == 'text':
        value = get_formatted_text(value)
    elif isinstance(value, list):
        value = flatten_array(value)

    return value


def get_formatted_text(value):
    return re.sub(r'(<b>|</b>|<i>|</i>)|[$,.:#]', '', value)


def flatten_array(value):
    separator = ','
    return separator.join(str(element) for element in value)
