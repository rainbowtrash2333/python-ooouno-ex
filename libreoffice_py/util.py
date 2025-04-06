import pandas as pd
def array2df(data_set):
    # 识别列名行（假设列名行所有字段非空）
    columns = next(item for item in data_set if all(field != '' for field in item))

    # 提取数据行（排除列名行）
    rows = [list(item) for item in data_set if item != columns]

    # 创建DataFrame
    df = pd.DataFrame(rows, columns=columns)