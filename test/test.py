table_schema = 'schema'
table_name = 'test_tb'

def make_query(**context):

    datas = [['1', 'park'], ['2', 'kim'], ['3', 'lee']]
    col_data = [['id'], ['name']]
    cols = ['id', 'name']

    sql_statements = []

    # 각 데이터에 대한 SELECT 문을 생성
    for inner_list in datas:
        values = ', '.join(f"'{val}'" for val in inner_list)
        sql_statement = f"SELECT {values} FROM DUAL"
        sql_statements.append(sql_statement)

    # SELECT 문들을 UNION ALL로 연결
    full_sql = ' UNION ALL\n'.join(sql_statements)

    # 최종 SQL 문장 생성
    full_sql = f"INSERT INTO {table_schema}.{table_name} ({', '.join(cols)})\n{full_sql}"

    # full_sql = ' UNION ALL\n'.join(sql_statements)

    print(full_sql)
    return full_sql

make_query()

# 'INSERT INTO table_schema.table_name {cols}'.format(