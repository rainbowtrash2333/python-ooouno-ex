from __future__ import annotations
import uno
from ooodev.calc import CalcDoc
from ooodev.utils.file_io import FileIO
from ooodev.loader import Lo
from ooodev.utils.gui import GUI
from ooodev.utils.type_var import PathOrStr
from ooodev.calc import CalcDoc, CalcSheet, ZoomKind, CalcSheetView
from ooodev.office.calc import Calc
from typing import Tuple


class Workbook:
    def __init__(self, read_only: bool = False, filepath: str | None = None, visible: bool = True) -> None:
        self._read_only = read_only
        self._filepath = filepath
        self._visible = visible
        self.doc = None

        try:
            loader = Lo.load_office(Lo.ConnectSocket())
            if self._filepath:
                self._input_fnm = FileIO.get_absolute_path(self._filepath)
                self.doc = CalcDoc.open_doc(fnm=self._input_fnm, loader=loader, visible=self._visible)
            else:
                self.doc = CalcDoc.create_doc(visible=True)

        except Exception:
            Lo.close_office()
            raise

    def save(self, save_path: str | None = None) -> None:
        if not self.doc:
            raise RuntimeError("No document to save.")

        path = save_path or self._filepath
        if not path:
            raise ValueError("No file path specified for saving.")
        out_file = FileIO.get_absolute_path(path)
        _ = FileIO.make_directory(out_file)
        out_fnm = out_file
        try:
            self.doc.save_doc(fnm=out_fnm)
        except Exception:
            Lo.close_office()
            raise

    def get_range_value(self,sheet_n:int, range_name:str)->Tuple[Tuple, ...]:
        cell_rng = Calc.get_range_obj(range_name="A1:B2")
        return self.doc.sheets[sheet_n].get_array(range_obj=cell_rng)

    def close(self):
        self.doc.close_doc()
        Lo.close_office()
        return 0


    def get_used_value(self,sheet_n:int)->Tuple[Tuple, ...]:

        used_rng = self.doc.sheets[sheet_n].find_used_range_obj()
        # start_idx = used_rng.start_row_index
        # end_idx = used_rng.end_row_index
        # start_col = used_rng.start_col_index
        # end_idx = used_rng.end_col_index
        return self.doc.sheets[sheet_n].get_array(range_obj=used_rng)