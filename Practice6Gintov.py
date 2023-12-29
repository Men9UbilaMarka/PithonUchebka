import psycopg2

host = "127.0.0.1"
port = 5432
database = "Python"
user = "postgres"
password = "1234"

def get_relation_tables(database_name, table_names):
    relation_tables = []  # Список таблиц связки

    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        cursor = conn.cursor()

        for table_name in table_names:
            # Формирование имени таблицы связки
            relation_table_name = '_'.join(table_name)

            # Проверка, существует ли таблица связки
            query = f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '{relation_table_name}');"
            cursor.execute(query)
            exists = cursor.fetchone()[0]

            if exists:
                relation_tables.append(relation_table_name)

        cursor.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Ошибка соединения с PostgreSQL: {e}")

    return relation_tables

# Пример вызова функции
database_name = 'Python'
table_names = ['users', 'orders']
relation_tables = get_relation_tables(database_name, table_names)

print(relation_tables)