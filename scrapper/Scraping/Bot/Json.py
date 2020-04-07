import json
from termcolor import colored
class json_structure():
    def __init__(self,path):
        self.path = path
#Return JSON file
    def get_json(self):
        with open(self.path, 'r') as f:
            data = json.load(f)
            return data

    def get_json_section(self,section):
        dict1 = dict(self.get_json())
        return dict1[section]

    def get_keys(self): # Return basic keys
        js = dict(self.get_json())
        return js.keys()

    def res(self, dict_a):
        with open(self.path, 'r') as f:
            data = json.load(f)

        dict = data['SAFETY DATA SHEET']
        str = "--"
        for key in dict:
            if bool(dict[key]) == False:
                print(str + " " + (colored(key, 'red')) + " Empty dict")
            else:
                print(colored(dict[key], 'red') + "Not Empty")
                self.res(dict[key])




class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



