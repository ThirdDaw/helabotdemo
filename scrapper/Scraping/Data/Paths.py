import os


def get_json_tree_path():  # Define JSON path
    path_to_current_file = os.path.realpath(__file__)
    path_to_current_folder = os.path.dirname(path_to_current_file)
    return path_to_current_folder + '/json-tree.json'


def get_filled_json():
    path_to_current_file = os.path.realpath(__file__)
    path_to_current_folder = os.path.dirname(path_to_current_file)
    return path_to_current_folder + '/filled_json.json'


def get_pdf_path():
    path_to_current_file = os.path.realpath(__file__)
    path_to_current_folder = os.path.dirname(path_to_current_file)
    return path_to_current_folder + '/evonik-sds.pdf'
