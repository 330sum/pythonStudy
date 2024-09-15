table_schema = 'schema'
table_name = 'test_tb'


def make_query(**context):

    datas = [['1', 'park'], ['2', 'kim'], ['3', 'lee']]
    col_data = [['id'], ['name']]
    cols = ['id', 'name']


    sql_statements = []
    for inner_list in datas:
        values = ', '.join(f"'{val}'" for val in inner_list)
        sql_statement = f"SELECT {values} FROM DUAL"
        sql_statements.append(sql_statement)

    combined_selects = ' UNION ALL\n'.join(sql_statements)

    sql = f'INSERT INTO {table_schema}.{table_name} {cols}\n{combined_selects}'.format(
        table_schema=f'{table_schema}',
        table_name=f'{table_name}',
        cols='({})'.format(', '.join(cols)) if cols else '',
    )

    print(sql)


make_query()

# 'INSERT INTO table_schema.table_name {cols}'.format(
