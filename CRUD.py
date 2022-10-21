import sqlite3

def sqlite_execute(query,dbname='sqlite.db'):
    sqlite_connection = sqlite3.connect(dbname)
    cursor = sqlite_connection.cursor()
    count = cursor.execute(query)
    sqlite_connection.commit()
    cursor.close()
    
    
def add_row(keys,values,table_name):
    '''
        Description:
            adding a row into table_name
        syntax:
            keys = [key1,key2,...,keyn]
            
            values = [value1,value2,...,valuen]
            
            table_name = table name
    '''  
    if len(keys) != len(values):
        print("[!] Error: keys length not equal values length")
        return
    sqlite_insert_query = "INSERT INTO " + table_name + " ("
    for key in keys: sqlite_insert_query+=str(key)+", " if str(key)!=str(keys[-1]) else str(key)+") VALUES ("
    for value in values: 
        if type(value).__name__ == "int":sqlite_insert_query+=str(value)+", " if str(value)!=str(values[-1]) else str(value)+")"
        if type(value).__name__ == "str":sqlite_insert_query+='"'+str(value)+'", ' if str(value)!=str(values[-1]) else '"'+str(value)+'")'
    
    sqlite_execute(sqlite_insert_query)

# def get_last_match_id():
#     sqlite_connection = sqlite3.connect('sqlite.db')
#     cursor = sqlite_connection.cursor()

#     sqlite_select_query = '''SELECT * from matches'''
#     cursor.execute(sqlite_select_query)
    
#     records = cursor.fetchall()
#     cursor.close()
    
#     return len(records)


# def get_last_user_id():
#     sqlite_connection = sqlite3.connect('sqlite.db')
#     cursor = sqlite_connection.cursor()

#     sqlite_select_query = '''SELECT * from users'''
#     cursor.execute(sqlite_select_query)
    
#     records = cursor.fetchall()
#     cursor.close()
    
#     return len(records)


# def does_user_exist(uid):
#     sqlite_connection = sqlite3.connect('sqlite.db')
#     cursor = sqlite_connection.cursor()

#     sqlite_select_query = '''SELECT * from users'''
#     cursor.execute(sqlite_select_query)
#     records = cursor.fetchall()
#     cursor.close()
    
#     for element in records:
#         if str(uid) == element[1]:
#             return True
#     else:
#         return False


# def get_user_information_by_id(id):
#     sqlite_connection = sqlite3.connect('sqlite.db')
#     cursor = sqlite_connection.cursor()
#     sqlite_select_query = '''SELECT * from users WHERE id='''+str(id)
#     cursor.execute(sqlite_select_query)
#     records_tup = cursor.fetchall()
#     records = []
#     for i in records_tup[0]:
#         records.append(i)
#     cursor.close()
#     return {
#         "id":records[0],
#         "uid":records[1],
#         "name":records[2],
#         "elo":records[3],
#         "wins":records[4],
#         "loses":records[5]
#     }


# print(get_user_information_by_id(1))

# def get_user_information_by_uid(uid):
#     sqlite_connection = sqlite3.connect('sqlite.db')
#     cursor = sqlite_connection.cursor()
#     sqlite_select_query = '''SELECT * from users WHERE uid="'''+str(uid)+'''"'''
#     cursor.execute(sqlite_select_query)
#     records_tup = cursor.fetchall()
#     records = []
#     for i in records_tup[0]:
#         records.append(i)
#     cursor.close()
#     return {
#         "id":records[0],
#         "uid":records[1],
#         "name":records[2],
#         "elo":records[3],
#         "wins":records[4],
#         "loses":records[5]
#     }
    
    
# def change_elo(elo,uid):
#     sqlite_connection = sqlite3.connect('sqlite.db')
#     cursor = sqlite_connection.cursor()
#     user_elo = get_user_information_by_uid(uid)["elo"]+elo
#     sqlite_select_query = '''UPDATE users SET elo = ''' + str(user_elo) + ''' WHERE uid='''+str(uid)
#     cursor.execute(sqlite_select_query)
#     sqlite_connection.commit()
#     cursor.close()


# def add_win(uid):
#     sqlite_connection = sqlite3.connect('sqlite.db')
#     cursor = sqlite_connection.cursor()
#     user_wins = get_user_information_by_uid(uid)["wins"]+1
#     sqlite_select_query = '''UPDATE users SET wins = ''' + str(user_wins) + ''' WHERE uid='''+str(uid)
#     cursor.execute(sqlite_select_query)
#     sqlite_connection.commit()
#     cursor.close()
    
    
# def add_lose(uid):
#     sqlite_connection = sqlite3.connect('sqlite.db')
#     cursor = sqlite_connection.cursor()
#     user_loses = get_user_information_by_uid(uid)["loses"]+1
#     sqlite_select_query = '''UPDATE users SET loses = ''' + str(user_loses) + ''' WHERE uid='''+str(uid)
#     cursor.execute(sqlite_select_query)
#     sqlite_connection.commit()
#     cursor.close()


# def set_rounds_from_id(id,ar,br):
#     sqlite_connection = sqlite3.connect('sqlite.db')
#     cursor = sqlite_connection.cursor()
    
#     sqlite_select_query = '''UPDATE matches SET team_a_rounds = ''' + ar + ''', team_b_rounds = ''' + br + ''' WHERE id='''+id
#     cursor.execute(sqlite_select_query)
#     sqlite_connection.commit()
#     cursor.close()
    
    
# def end_match(id):
#     sqlite_connection = sqlite3.connect('sqlite.db')
#     cursor = sqlite_connection.cursor()
    
#     sqlite_select_query = '''UPDATE matches SET was_ended = "1" WHERE id='''+id
#     cursor.execute(sqlite_select_query)
#     sqlite_connection.commit()
#     cursor.close()
    
    
# def get_match_info_from_id(id):
#     sqlite_connection = sqlite3.connect('sqlite.db')
#     cursor = sqlite_connection.cursor()

#     sqlite_select_query = '''SELECT * from matches WHERE id=''' + id
#     cursor.execute(sqlite_select_query)
#     records_tup = cursor.fetchall()
#     records = []
#     for i in records_tup[0]:
#         records.append(i)
#     cursor.close()
#     return {
#         "match_id":records[0],
#         "team_a_rounds":records[1],
#         "team_b_rounds":records[2],
#         "winner":records[3],
#         "team_a_members":json.loads(records[4]),
#         "team_b_members":json.loads(records[5]),
#         "map":records[6],
#         "played_in":records[7],
#         "was_ended":bool(int(records[8])),
#         "org":records[9],
#         "url":records[10]
#     }
    
    
# def create_user(name,uid):
#     sqlite_connection = sqlite3.connect('sqlite.db')
#     cursor = sqlite_connection.cursor()
#     sqlite_insert_query = '''INSERT INTO users
#                           (uid, name, elo, wins, loses)  
#                           VALUES  ("''' + str(uid) + '''" ,"''' + name + '''" ,1000 ,0 ,0)'''
#     count = cursor.execute(sqlite_insert_query)
#     sqlite_connection.commit()
#     cursor.close()
    
    
# def create_match(team_a_members, team_b_members, map, org, url):
#     sqlite_connection = sqlite3.connect('sqlite.db')
#     cursor = sqlite_connection.cursor()
#     sqlite_insert_query = '''INSERT INTO matches
#                           (team_a_rounds, team_b_rounds, winner, team_a_members, team_b_members, map, played_in, was_ended, org, url)  
#                           VALUES  (0, 0, "none", "''' + str(team_a_members) + '''", "''' + str(team_b_members) +'''", "''' + map + '''", ''' + str(time.time()) + ''', "0", "''' + org + '''", "''' + url + '''")'''
#     count = cursor.execute(sqlite_insert_query)
#     sqlite_connection.commit()
#     cursor.close()