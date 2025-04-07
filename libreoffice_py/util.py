import pandas as pd
from typing import Tuple
from typing import Union

def number_to_rounded_str(n: Union[int, float], digits: int = 2) -> str:
    if isinstance(n, int):
        return str(n)
    elif isinstance(n, float):
        # 检查小数部分是否为 0（如 5.0, 10.0）
        if n.is_integer():
            return str(int(n))
        else:
            # 四舍五入并保留指定位数
            rounded = round(n, digits)
            # 如果 digits=0，直接返回整数形式
            if digits == 0:
                return str(int(rounded))
            else:
                return f"{rounded}"
    else:
        raise ValueError("Input must be int or float")


def array2df(data_set: Tuple[Tuple, ...]) -> pd.DataFrame:
    # 识别列名行（假设列名行所有字段非空）
    columns = next(item for item in data_set if all(field != '' for field in item))

    # 提取数据行（排除列名行）
    rows = [list(item) for item in data_set if item != columns]

    # 创建DataFrame
    df = pd.DataFrame(rows, columns=columns)
    return df


#       type  label              value                      description
# 9              a6                0.0
# 10  /10000     a7         6413960.45
# 11     增减值     a8         -22.203955
# 12  /10000     a9         8945017.34
# 定义处理逻辑的函数
def process_value_to_str(row: [], decimal_places: int = 2) -> str:
    if row['type'] == '':  # type为空，不处理
        return row['value']

    value = row['value']
    if value == '':  # value为空，无法处理
        return ''

    if not (isinstance(value, int) or isinstance(value, float)):
        return value
    # 根据 type 进行运算
    if row['type'] == '增减值':
        return ("增加" if value >= 0 else "减少") + number_to_rounded_str(abs(value), decimal_places)

    operators = '+-*/'
    for op in operators:
        if row['type'].startswith(op):
            sign = op
            number = float(row['type'][1:])
            result = value
            # print(f"符号: {sign}, 数字: {number}")
            if sign == '/':
                result = value / number
            elif sign == '*':
                result = value * number
            elif sign == '+':
                result = value + number
            elif sign == '-':
                result = value - number
            # 返回整数或浮点数的字符串形式（根据实际需求调整）
            return  number_to_rounded_str(result, decimal_places)

    else:
        return number_to_rounded_str(value, decimal_places)  # 未知type，不处理
