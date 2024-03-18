from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
import pandas as pd

from .forms import ExcelUploadForm

def handle_uploaded_file(file):
    # Excel dosyasını oku
    excel_data = pd.read_excel(file)
    return excel_data

def home_view(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Dosyayı işle
            excel_data = handle_uploaded_file(request.FILES['excel_file'])
            # Verileri şablonla paylaş
            return render(request, 'index.html', {'excel_data': excel_data})
    else:
        form = ExcelUploadForm()
    return render(request, 'upload_excel.html', {'form': form})
