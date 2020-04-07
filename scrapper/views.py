import os
import time
import json
from PyPDF2 import PdfFileReader
import ast

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect

from scrapper.Scraping.Data import Paths
from scrapper.Scraping.Feature.Helabot import helabot
from .forms import UploadFileForm
from .utils import *


# Create your views here.
def index(request):
    return render(request, "scrapper/index.html")


def action(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_name = default_storage.save(request.POST['title'] + '.pdf', ContentFile(file.read()))
            HELASOFT = helabot(os.path.dirname(os.path.dirname(__file__)) + "/media/" + str(file_name),
                               "SECTION 1: Identification of the substance/mixture and of the company/undertaking")

            content = {
                "SECTION 1: Identification of the substance/mixture and of the company/undertaking": ast.literal_eval(
                    HELASOFT.get_json())}

            json_file = default_storage.save(file_name.replace(".pdf", ".json"),
                                             ContentFile(str(content).replace("\'", "\"")))

            data = dict_to_html_ret_str(content)

            path = 'media/' + file_name

            return render(request, "scrapper/action.html", {'form': form, 'path': path, 'data': data})
        # data = dict_to_html_ret_str(json.dumps(request.POST.dict()))
        full_req = request.POST.dict()
        full_req.pop('csrfmiddlewaretoken')
        path_to_json = str(full_req.pop('path_to_file')).replace(".pdf", ".json")

        dict_to_json(path_to_json, full_req)

        result_json_file = open(path_to_json, 'r')

        result_dict = result_json_file.read()

        path_to_pdf_file = path_to_json.replace(".json", ".pdf")
        path_to_json_file = path_to_pdf_file.replace(".pdf", ".json")
        # result_json = dict_to_json(path_to_json, result_dict)
        return render(request, "scrapper/action.html",
                      {'form': form, 'result': result_dict, 'pdfpath': path_to_pdf_file, 'jsonpath': path_to_json_file})
    else:
        form = UploadFileForm()
    return render(request, "scrapper/action.html", {'form': form})


def preview(request, path):
    return render(request, 'scrapper/preview.html', context={
        'path': path
    })


def login(request):
    return render(request, 'scrapper/login.html')
