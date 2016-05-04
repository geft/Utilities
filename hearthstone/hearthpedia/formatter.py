import re

site_pattern = r'src="(.*?)\/200px'
name_pattern = r'\/([A-z]+[-_]*[A-z]+)\%'


def get_image_list(site):
    match = re.findall(site_pattern, site)

    if len(match) == 0:
        print('No match found')
        exit()

    return match


def get_formatted_url_list(url_list):
    for i, url in enumerate(url_list):
        url_list[i] = str.replace(url, '/thumb/', '/')

    return url_list


def get_name(url):
    match = re.findall(name_pattern, url)

    name = 'None'
    if len(match) != 0:
        name = match[0]
    else:
        print('Unable to find name for ' + url)

    name = str.lower(name)
    name = str.replace(name, '_', '-')

    return name
