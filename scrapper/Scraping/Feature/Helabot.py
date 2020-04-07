from scrapper.Scraping.Feature import Excel, PDF, Json, SDS
from scrapper.Scraping.Feature import Regex
import json
import scrapper.Scraping.Data.Paths as Paths
import pathlib


class helabot():
    Dict_dump = {}
    new_dict = {}
    iter_dict_in = {}
    iter_list_in = {}
    iter_str_in = {}

    def __init__(self, pdf_path, section_name):
        self.section_name = section_name
        self.pdf_path = pdf_path
        self.PDF_FILE = PDF.Pdf(self.pdf_path)
        self.JSON_TREE = Json.json_structure(self.define_json_path())
        self.SAFETY_DATA_SHEET = SDS.sds(self.PDF_FILE.get_full_pdf())
        self.Dict_dump = self.JSON_TREE.get_json_section(section_name)
        self.recursive_fill_items(self.Dict_dump)

    def define_json_path(self):
        return Paths.get_json_tree_path()

    def recursive_fill_items(self, DICT):  # recursive in count = 108

        for i in DICT.keys():
            if isinstance(DICT[i], dict):

                for key, value in DICT[i].items():  # Checking types of each element of dict

                    if isinstance(value, str):

                        self.iter_list_in[key] = self.set_json(key)


                    elif isinstance(value, dict):

                        self.iter_list_in[key] = self.iter_str_in
                        self.recursive_fill_items(value)
                test = self.iter_list_in.copy()
                self.iter_dict_in[i] = test
                self.iter_list_in.clear()

            else:
                self.iter_str_in[i] = self.set_json(i)

    def get_value_by_key(self, key, DICT):
        DICT = self.SAFETY_DATA_SHEET.get_items_list(DICT)

    def set_json(self, item):

        DICT = self.SAFETY_DATA_SHEET.get_items_list(self.Dict_dump)
        new_dict = {}

        for elem in DICT:
            if item == elem:
                if (DICT.index(elem)) + 1 != len(DICT):
                    elem = elem.replace(":", "").strip()
                    thiselem = elem
                    nextelem = DICT[DICT.index(elem) + 1]
                    nextelem = nextelem.replace(":", "").strip()
                    value = self.SAFETY_DATA_SHEET.get_value(thiselem, nextelem, self.SAFETY_DATA_SHEET.get_section(1))
                    value = value.replace(":", "").strip()
                    new_dict[thiselem] = value
                    return value

    def get_json(self):
        j = json.dumps(self.iter_dict_in, indent=4)
        pathlib.Path(Paths.get_filled_json()).write_text(j, encoding="utf-8")
        return j


# ===================================================================================================================
# HELASOFT = helabot(Paths.get_pdf_path(),
#                    "SECTION 1: Identification of the substance/mixture and of the company/undertaking")
#
# print(type(HELASOFT.get_json()))
