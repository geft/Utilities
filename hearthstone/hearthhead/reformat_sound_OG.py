card_set = 'OG_'
extension = '.mp3'


def reformat(file_name):
    print('INPUT: ' + file_name)

    file_name = remove_strings(file_name)
    file_name = remove_prefix(file_name)
    file_name = remove_middle(file_name)

    print('OUTPUT: ' + file_name)

    return file_name


def remove_middle(file_name):
    start_index = get_middle_start_index(file_name)
    end_index = get_middle_end_index(file_name)

    if start_index is not -1 \
            and end_index is not -1 \
            and start_index is not end_index:
        print("MIDDLE: " + file_name +
              ' [' + str(start_index) + ', ' + str(end_index) + ']')

        file_name = file_name[:start_index] + file_name[end_index:]

    return file_name


def get_middle_end_index(file_name):
    suffix = ['Attack', 'Death', 'Play', 'Trigger', 'InPlay']
    end_index = -1
    for suffix_string in suffix:
        end_index = str.find(file_name, '_' + suffix_string + extension)

        if end_index is not -1:
            break
    return end_index


def get_middle_start_index(file_name):
    set_char = len(card_set) - 1

    if file_name[set_char] is '_' and file_name[set_char + 4] is '_':
        start_index = set_char + 4
    elif file_name[set_char] is '_' and file_name[set_char + 5] is '_':
        start_index = set_char + 5
    else:
        start_index = -1
    return start_index


def remove_prefix(file_name):
    start_index = find_start_index(file_name)
    file_name = file_name[start_index:]
    return file_name


def remove_strings(file_name):
    file_name = str.replace(file_name, 'VO_', '')
    file_name = str.replace(file_name, 'Male_OldGod_', '')

    digit = file_name[-6:-4]
    if digit.isnumeric() and 'InPlay' not in file_name:
        file_name = file_name[:-7] + file_name[-4:]

    return file_name


def find_start_index(file_name):
    return str.find(file_name, card_set)
