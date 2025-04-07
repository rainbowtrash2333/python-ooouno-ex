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


def gen_xls1(template_path: str, data_path: str, date: str):
    result_path = os.path.join(data_path, f"{date}重点客户风险排查情况表.xlsx")
    if not os.path.exists(result_path):
        shutil.copy2(template_path, result_path)
    sht_1 = os.path.join(data_path, '借新还旧汇总.xlsx')
    sht_2 = os.path.join(data_path, '借新还旧明细.xlsx')
    sht_3 = os.path.join(data_path, '逾期60天至90天对公贷款明细.xlsx')

    wb1 = Workbook(read_only=True, filepath=sht_1, visible=False)
    data1 = array2df(wb1.get_used_value(0))
    wb1.close()
    data1 = data1.drop(columns=[data1.columns[0]])

    wb_tgt = Workbook(read_only=False, filepath=result_path, visible=True)
    wb_tgt.set_pandas_range(data1, 0, "A4")
    wb_tgt.doc.sheets[0]['A2'].value = date

    wb2 = Workbook(read_only=True, filepath=sht_2, visible=False)
    data2 = array2df(wb2.get_used_value(0))
    data2 = reorder_dataframe_columns(data2,
                                      ['贷款发放行名称', '贷款客户名称', '借新还旧次数', '发放日期', '到期日期',
                                       '发放金额', '贷款余额', '欠本天数', '欠息天数', '五级分类', '贷款发放类型'])
    wb2.close()
    wb_tgt.set_pandas_range(data2, 1, "A4")
    wb_tgt.doc.sheets[1]['A2'].value = date
    merge_list = ['A4', 'B4']
    for ml in merge_list:
        wb_tgt.merge_same_cells(1, ml)

    wb_tgt.save()
    wb_tgt.close()


if __name__ == '__main__':
    template_path = r'F:\客户风险\数据\重点客户风险排查情况表-模板.xlsx'
    data_path = r'F:\客户风险\数据'
    date = "2025年1月"
    gen_xls1(template_path, data_path, date)
    # foo()
    office_loader = OfficeLoader()
    office_loader.close()
