from workbook import Workbook
from word import Word
from ooodev.office.calc import Calc
from myutil import array2df,process_value_to_str
import pandas as pd
from typing import Sequence

if __name__ == '__main__':
    wb =Workbook(read_only=True,filepath=r"E:\Twikura\Projects\libreoffice\gen_report\data.xls",visible=False)

    df = array2df(wb.get_used_value(0))
    df['value'] = df.apply(process_value_to_str, axis=1)
    wb.close()
    word = Word(read_only=False, filepath=r"E:\Twikura\Projects\libreoffice\gen_report\test.doc", visible=True)
    df['label'] = df['label'].apply(lambda x: f"$({x})" if pd.notna(x) and x != '' else x)
    labels_list: Sequence[str] = df['label'].tolist()
    values_list: Sequence[str] = df['value'].tolist()
    print(labels_list)
    print(values_list)
    # for i in range(len(labels_list)):
    #     word.replace_word(labels_list[i], values_list[i])
    # # word.replace_words(['$(b1)'], '111222')
    word.replace_words(labels_list,values_list)

    # print(r)
    # word.save()
    # print(r)
    #word.close()
