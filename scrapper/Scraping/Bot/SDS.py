# Get PDF and convert to TXT
import scrapper.Scraping.Bot
from scrapper.Scraping.Bot import Json, Regex
from scrapper.Scraping.Data import Dictionaries


class sds:
    items_list = []

    def __init__(self, txt_sds):
        self.txt_sds = txt_sds

    # ==============================================================================
    def get_items_list(self, DICT):
        self.recursive_determine_items(DICT)
        return self.items_list

    def recursive_determine_items(self, DICT):  # recursive in count = 108
        for i in DICT.keys():  # i  = items (1.1 Product identifier, 1.2,1.3 etc)
            if isinstance(DICT[i], dict):
                self.items_list.append(i)
                for key, value in DICT[i].items():  # Checking types of each element of dict
                    if isinstance(value, str):
                        self.items_list.append(key)
                    elif isinstance(value, dict):
                        self.items_list.append(key)
                        self.recursive_determine_items(value)

            else:
                self.items_list.append(i)


    # ====================================================================================
    def get_section(self, section_item):
        key = Dictionaries.SECTION_KEY
        nextelem = key[(section_item) % len(key)]
        first = Regex.reg(key[section_item - 1], self.txt_sds)
        second = Regex.reg(nextelem, self.txt_sds)
        new_txt = self.txt_sds[first[0]:second[0]]

        return new_txt

    def join(self, list_of_key_words, united_list):  # Get list with key(as #LIST) words and full sds(as #LIST)
        # Return new list where the key words are connected
        list_of_index = []
        for item in list_of_key_words:
            # print(list_of_key_words)
            if united_list.index(item):
                list_of_index.append(united_list.index(item))
            else:
                continue
        united_list[list_of_index[0]:list_of_index[-1] + 1] = [
            ' '.join(united_list[list_of_index[0]:list_of_index[-1] + 1])]
        print(united_list)
        return united_list

    def get_value(self, item1, item2, section_content):  # Indentifired value beetween @list_of_key_words
        first = Regex.reg(item1, section_content)
        second = Regex.reg(item2, section_content)


        return section_content[first[-1]:second[0]]
