import csv

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView

from .forms import UploadFileForm
from .models import Product


def handle_uploaded_file(file):

    for x in Product.objects.all().iterator(): x.delete()

    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.reader(decoded_file)
    print(reader)
    for row in reader:
        s = ';'.join(row)
        # print(s)
        l = list(s.split(';'))
        if len(l)>14:
            l = l[:14]
        a = Product()
        l1 = list(a.__dict__.keys())
        l1 = l1[2:]
        for i in range(len(l)):
            a.__setattr__(l1[i], l[i])

        a.save()


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('view/')

    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


class ProductView(ListView):
    model = Product
    template_name = 'view.html'

