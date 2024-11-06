def convert_to_batch_inserts(input_sql_file_path, output_sql_file_path):
    with open(input_sql_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 初始化批量插入语句的变量
    batch_inserts = []
    batch_values = []
    table_name = None

    for line in lines:
        if line.strip().startswith("INSERT INTO"):
            if table_name is not None:
                # 如果不是第一行INSERT语句，保存之前的批量插入语句
                batch_inserts.append(f"INSERT INTO {table_name} VALUES {', '.join(batch_values)};")
            # 获取表名
            table_name = line.split(' ')[2]
            # 清空values列表
            batch_values = []
        if line.strip().startswith("VALUES"):
            # 添加值到values列表
            values = line.split('VALUES')[1].strip()
            batch_values.append(values)

    # 添加最后一批次的数据
    if table_name is not None and batch_values:
        batch_inserts.append(f"INSERT INTO {table_name} VALUES {', '.join(batch_values)};")

    # 写入输出文件
    with open(output_sql_file_path, 'w') as file:
        for insert in batch_inserts:
            file.write(insert + "\n")


# 使用函数r
input_sql_file_path = r'E:\feiyu\sql文件\扬尘\ja_t_dust_site_data_info.sql'  # 你的输入SQL文件路径
output_sql_file_path = r'C:\Users\19125\Desktop\ja_t_dust_site_data_info.sql'  # 你的输出SQL文件路径
convert_to_batch_inserts(input_sql_file_path, output_sql_file_path)
