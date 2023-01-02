import mysql.connector
druid_host = "localhost"
druid_port = 8888
druid_path = "/druid/v2/sql"
druid_scheme = "http"
druid_query = """SELECT * FROM wikipedia LIMIT 10"""    
druid_connection = mysql.connector.connect(host=druid_host, port=druid_port)
if druid_connection.is_connected():
    print("connected")
# print(druid_connection)
# druid_cursor= druid_connection.cursor()
# df = pd.DataFrame(druid_cursor.execute(druid_query))