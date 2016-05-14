import json_parser

json_parser.reader.remove_sql_data()

json_data = json_parser.reader.get_json_data()
sql_connection = json_parser.reader.get_sql_connection()

json_parser.writer.create_database(sql_connection)
json_parser.writer.write_database(json_data, sql_connection)

json_parser.writer.close_sql(sql_connection)
