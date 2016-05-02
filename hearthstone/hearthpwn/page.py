def modify_display_type(url):
    display_modifier = 'display='

    if display_modifier in url:
        index = url.find(display_modifier) + len(display_modifier)
        url = url[:index] + '1' + url[index + 1:]
    else:
        print('Display qualifier not found')
        exit()

    return url


def modify_start_index(site_url, page_index_start):
    page_modifier = '&page='
    if page_modifier in site_url:
        index = site_url.find(page_modifier) + len(page_modifier)

        if site_url[index:index + 1].isdigit():
            page_index_start = site_url[index:index + 1]
        elif site_url[index].isdigit():
            page_index_start = site_url[index]

    return page_index_start


def modify_page(url, page_index, page_index_end):
    page_modifier = "&page="
    if page_index_end > 1 and page_modifier not in url:
        url += page_modifier + str(page_index)
    if page_modifier + str(page_index - 1) in url:
        url = str.replace(
            url,
            page_modifier + str(page_index - 1),
            page_modifier + str(page_index))

    return url
