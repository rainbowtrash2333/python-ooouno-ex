from workbook import Workbook
from word import Word
from ooodev.office.calc import Calc
from util import array2df
if __name__ == '__main__':
    wb =Workbook(read_only=True,filepath=r"E:\Twikura\Projects\libreoffice\gen_report\data.xls",visible=False)
    v = wb.get_used_value(0)
    pd = array2df(v)
    wb.close()
    print(pd)

    # word = Word(read_only=True, filepath=r"E:\Twikura\Projects\libreoffice\gen_report\test.doc", visible=True)
    # #txt = word.get_content_text()
    # #print("txt: "+txt)
    # r = word.replace_word("$(b1)", "123")
    # print(r)
    # word.close()
    # https://github.com/Amourspirit/python-ooouno-ex/blob/3ed03052067b063dbab0182975e2336e81d6bbd4/ex/auto/writer/odev_shuffle/start.py#L57