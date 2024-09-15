def make_query(**context):

    datas = [['1', 'park'], ['2', 'kim'], ['3', 'lee']]
    col_data = [['id'], ['name']]
    cols = ['id', 'name']

    # Generate SELECT statements for each row of data
    sql_statements = [
        f"SELECT {', '.join(f"'{val}'" for val in inner_list)} FROM DUAL"
        for inner_list in datas
    ]

    # Combine all SELECT statements with UNION ALL
    combined_selects = ' UNION ALL\n'.join(sql_statements)

    # Format the full INSERT INTO ... SELECT query
    full_sql = f"INSERT INTO {table_schema}.{table_name} ({', '.join(cols)})\n{combined_selects}"

    print(full_sql)



make_query()

# 'INSERT INTO table_schema.table_name {cols}'.format(