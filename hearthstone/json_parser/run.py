import hearthstone.json_parser.directory as directory

data_root = directory.data_root


def get_json_file(file_name):
    return data_root + file_name + '.json'


def get_sql_file(file_name):
    return data_root + file_name + '.db'


def run(file_name):
    import hearthstone.json_parser as parser

    reader = parser.reader
    writer = parser.writer

    json_file = get_json_file(file_name)
    sql_file = get_sql_file(file_name)

    reader.remove_sql_data(sql_file)

    json_data = reader.get_json_data(json_file)
    sql_connection = reader.get_sql_connection(sql_file)

    writer.create_database(sql_connection)
    writer.write_database(json_data, sql_connection)

    writer.close_sql(sql_connection)


run(directory.file_name)
run(directory.file_name_collectible)
