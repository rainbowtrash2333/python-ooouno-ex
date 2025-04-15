import shutil
import os
from workbook import Workbook
from word import Word
from myutil import *
from officeLoader import OfficeLoader
from ooodev.utils.color import CommonColor
from ooodev.format.calc.direct.cell.borders import Side
from ooodev.format.calc.direct.cell.borders import BorderLineKind
from ooodev.formatters.formatter_table import FormatterTable


def foo():
    wb_src = Workbook(read_only=True, filepath=r"F:\客户风险\数据\2024年11月重点客户风险排查情况表.xlsx", visible=False)
    sheet1_props = wb_src.doc.sheets[0].get_custom_properties()


def gen_xls(src_file: str, tgt_wb: Workbook, sheet_n, data_cell_name: str, date_str: str = None,
            date_cell_name: str = None,
            order: [] = None,
            sum_cells_list: [] = None, merge_list: [] = None) -> None:
    src_wb = Workbook(read_only=True, filepath=src_file, visible=False)
    data = array2df(src_wb.get_used_value(0))
    if order is not None:
        data = reorder_dataframe_columns(data, order)

    src_wb.close()
    tgt_wb.set_pandas_range(data, sheet_n, data_cell_name)
    if date_str is not None and date_cell_name is not None:
        tgt_wb.doc.sheets[sheet_n][data_cell_name].value = date_str
    if sum_cells_list is not None:
        for cell in sum_cells_list:
            tgt_wb.sum_col(sheet_n, cell)
    if merge_list is not None:
        for cell in merge_list:
            tgt_wb.merge_same_cells(sheet_n, cell)

def key_customers():
    template_path = r'F:\客户风险\teml\重点客户风险排查情况表-模板.xlsx'
    data_path = r'F:\客户风险\数据'
    src_list = list(map(lambda x: os.path.join(data_path, x),
                        ['借新还旧汇总.xlsx', '借新还旧明细.xlsx', '逾期60天至90天对公贷款明细.xlsx']))

    orders = [
        ['贷款发放行名称', '贷款笔数', '发放金额', '贷款余额'],
        ['贷款发放行名称', '贷款客户名称', '借新还旧次数', '发放日期', '到期日期',
         '发放金额', '贷款余额', '欠本天数', '欠息天数', '五级分类', '贷款发放类型'],
        ['贷款发放行名称', '贷款客户名称', '发放日期', '到期日期', '发放金额',
         '贷款余额', '欠本天数', '欠息天数', '五级分类', '贷款发放类型']
    ]
    date_str = "2025年1月"
    result_path = os.path.join(r'F:\客户风险\1', f"{date_str}重点客户风险排查情况表.xlsx")

    if not os.path.exists(result_path):
        shutil.copy2(template_path, result_path)
    wb_tgt = Workbook(read_only=False, filepath=result_path, visible=True)
    data = [
        [src_list[0], wb_tgt, 0, 'A5', date_str, 'A2', orders[0], ['B4', 'C4', 'D4'], None],
        [src_list[1], wb_tgt, 1, 'A4', date_str, 'A2', orders[1], None, None],
        [src_list[2], wb_tgt, 2, 'A5', date_str, 'A2', orders[2], ['E4', 'F4'], ['A5']]
    ]

    for d in data:
        gen_xls(*d)

    wb_tgt.save()
    wb_tgt.close()



def covering_up_asset_quality():
    template_path = r'F:\客户风险\teml\疑似掩盖资产质量贷款台账-模板.xlsx'
    data_path = r'F:\客户风险\数据'
    src_list = list(map(lambda x: os.path.join(data_path, x),
                        ['借新还旧汇总.xlsx', '借新还旧明细.xlsx', '逾期60天至90天对公贷款明细.xlsx']))


def main():
    key_customers()


if __name__ == '__main__':
    raise SystemExit(main())
