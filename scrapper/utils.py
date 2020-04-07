import ast
import collections.abc


def handle_uploaded_file(f):
    with open(f, 'wb+') as destination:
        for chunk in f.chunks():
            print(chunk)


def dict_to_html(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print(
                "<li><label for='" + key + "'>" + key + " : </label><input type='text'  id='" + key + "' name='" + key + "'><ul>")
            dict_to_html(value)
            print("</ul></li>")
        elif isinstance(value, list):
            print(
                "<li><label for='" + key + "'>" + key + " : </label><input type='text'  id='" + key + "' name='" + key + "'><ul>")
            for i in range(len(value)):
                dict_to_html(value[i])
                print("<br>")
            print("</ul>")
        else:
            print(
                "<li><label for='" + key + "'>" + key + " : </label><input type='text'  id='" + key + "' name='" + key + "' value='" + str(
                    value) + "'></li>")


GLOBAL_LITE_TEST_JSON = {"first": {"first_first": 1, "first_second": 2}, "second": 3, "third": 4}
GLOBAL_TEST_JSON = {
    "SECTION 1: Identification of the substance/mixture and of the company/undertaking": {
        "1.1 Product identifier": {
            "Default": "",
            "Product name": "",
            "Additional identification": [{
                "Chemical name": "",
                "INDEX No.": "",
                "CAS-No.": "",
                "EC No.": "",
                "REACH Registration No.": ""
            }]
        },

        "1.2 Relevant identified uses of the substance or mixture and uses advised against": {

            "Identified uses": "",
            "Uses advised against": ""

        },
        "1.3 Details of the supplier of the safety data sheet": {
            "Company Name": "",
            "Telephone": "",
            "E-mail": ""
        },
        "1.4 Emergency telephone number": {
            "24-Hour Health Emergency": ""
        }
    },
    "SECTION 2: Hazards identification": {
        "2.1 Classification of the substance or mixture": {
            "Default": "",
            "Classification according to Regulation (EC) No 1272/2008 as amended": {
                "Health Hazards": ""
            }
        },
        "2.2 Label Elements": {
            "Signal Words": "",
            "Hazard Statement(s)": "",
            "Supplemental label information": "",
            "Precautionary Statements ": {
                "Prevention": "",
                "Response": "",
                "Disposal": ""
            }
        },
        "2.3 Other hazards": {
            "Other hazards": ""
        }
    },
    "SECTION 3: Composition/information on ingredients": {
        "3.1 Substances": {
            "Chemical name": "",
            "INDEX No.": "",
            "CAS-No.": "",
            "EC No.": "",
            "REACH Registration No.": "",
            "Table": {
                "Chemical name": "",
                "Concentration": "",
                "CAS-No.": "",
                "EC No.": "",
                "REACH Registration No.": "",
                "M-Factor": "",
                "Notes": ""
            }
        }
    },
}


# def dict_to_html_ret_str(dictionary, data='', salt=[]):
#     if not salt:
#         salt.append(0)
#     for key, value in dictionary.items():
#         if isinstance(value, dict):
#             salt[0] += 1
#             data += "<li><label for='" + key + str(
#                 salt[0]) + "'>" + key + " : </label><input type='text'  id='" + key + str(
#                 salt[0]) + "' name='" + key + str(
#                 salt[0]) + "'><ul>"
#             data += dict_to_html_ret_str(value)
#             data += "</ul></li>"
#         elif isinstance(value, list):
#             data += "<li><label for='" + key + str(
#                 salt[0]) + "'>" + key + " : </label><input type='text'  id='" + key + str(
#                 salt[0]) + "' name='" + key + str(
#                 salt[0]) + "'><ul>"
#             for i in range(len(value)):
#                 salt[0] += 1
#                 data += dict_to_html_ret_str(value[i])
#                 data += "<br>"
#             data += "</ul>"
#         else:
#             data += "<li><label for='" + key + str(
#                 salt[0]) + "'>" + key + " : </label><input type='text'  id='" + key + str(
#                 salt[0]) + "' name='" + key + str(
#                 salt[0]) + "' value='" + str(
#                 value) + "'></li>"
#     return data

# def dict_to_html_ret_str(dictionary, data=''):
#     if not data:
#         data = ''
#     for key, value in dictionary.items():
#         if isinstance(value, dict):
#             data += "<li><label for='" + key + "'>" + key + " : </label><input type='text'  id='" + key + "' name='" + key + "'><ul>"
#             data += dict_to_html_ret_str(value)
#             data += "</ul></li>"
#         elif isinstance(value, list):
#             data += "<li><label for='" + key + "'>" + key + " : </label><input type='text'  id='" + key + "' name='" + key + "'><ul>"
#             for i in range(len(value)):
#                 data += dict_to_html_ret_str(value[i])
#                 data += "<br>"
#             data += "</ul>"
#         else:
#             data += "<li><label for='" + key + "'>" + key + " : </label><input type='text'  id='" + key + "' name='" + key + "' value='" + str(
#                 value) + "'></li>"
#     return data


def dict_to_html_ret_str(dictionary, data=''):
    if not data:
        data = ''
    for key, value in dictionary.items():
        if isinstance(value, dict):
            data += "<li><label for='" + key + "'>" + key + " : </label><ul>"
            data += dict_to_html_ret_str(value)
            data += "</ul></li>"
        elif isinstance(value, list):
            data += "<li><label for='" + key + "'>" + key + " : </label><ul>"
            for i in range(len(value)):
                data += dict_to_html_ret_str(value[i])
                data += "<br>"
            data += "</ul>"
        else:
            data += "<li><label for='" + key + "'>" + key + " : </label><input type='text'  id='" + key + "' name='" + key + "' value='" + str(
                value) + "'></li>"
    return data


def recursive_changer(dictionary, other):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            recursive_changer(value, other)
        else:
            if key in other.keys():
                dictionary[key] = other[key]


def dict_to_json(path_to_init_json, new_data):
    file = open(path_to_init_json, 'r')
    print(path_to_init_json)
    start_json = file.read()
    file.close()
    start_json_in_dict = ast.literal_eval(start_json)
    recursive_changer(start_json_in_dict, new_data)
    file = open(path_to_init_json, 'w')
    file.write(str(start_json_in_dict).replace("\'", "\""))
    file.close()

# dict_to_json("../media/create.json", {'Product name': 'VPS 7162',
#                                       'Chemical name': '1,3,5-tris[3-(trimethoxysilyl)propyl]-1,3,5-triazine-2,4,6(1H,3H,5H)-trione Chemical formula C21H45N3O12Si3',
#                                       'INDEX No.': '-', 'CAS-No.': '26115-70-8', 'EC No.': '247-465-8',
#                                       'REACH Registration No.': '01-2120807606-55-0001',
#                                       'Identified uses': 'For industrial use Additive Coupling agent',
#                                       'Uses advised against': 'Not determined.',
#                                       'Company Name': 'Evonik Resource Efficiency GmbH RE-ES-PS Hanau Postfach 1345 63403 Hanau Germany',
#                                       'Telephone': '+49 6181 59 4787', 'E-mail': 'sds-hu@evonik.com',
#                                       '24-Hour Health Emergency': '+49 7623 919191', 'END': ''})

# first = {"one": {"one_one": '11', "one_two": '12'}, "two": '2'}
# second = {"one_one": '12', "one_two": '13', "two": '3'}
# recursive_changer(first, second)
# print(first)
