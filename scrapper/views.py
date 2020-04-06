import os
import time
import json
from PyPDF2 import PdfFileReader

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect

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

            # HERE GOES FUNCTION THAT TRANSLATES PDF TO JSON
            json_file = default_storage.save(file_name.replace(".pdf", ".json"),
                                             ContentFile(str(GLOBAL_TEST_JSON).replace("\'", "\"")))

            data = dict_to_html_ret_str(GLOBAL_TEST_JSON)

            # TODO with saving file, save JSON with exact same name to place new values after changing
            path = 'media/' + file_name

            return render(request, "scrapper/action.html", {'form': form, 'path': path, 'data': data})
        # data = dict_to_html_ret_str(json.dumps(request.POST.dict()))
        full_req = request.POST.dict()
        full_req.pop('csrfmiddlewaretoken')
        result = full_req
        # JUST FOR TESTING DICTIONARY
        return render(request, "scrapper/action.html", {'form': form, 'result': result})
    else:
        form = UploadFileForm()
    return render(request, "scrapper/action.html", {'form': form})


def preview(request, path):
    return render(request, 'scrapper/preview.html', context={
        'path': path
    })
