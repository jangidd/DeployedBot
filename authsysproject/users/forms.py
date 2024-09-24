from django import forms
from multiupload.fields import MultiFileField
from .models.DICOMData import DICOMData
from .models.EcgPdfReport import EcgReport
from .models.XrayPdfReport import XrayReport
from .models.Location import Location

class DICOMDataForm(forms.ModelForm):
    dicom_file = MultiFileField(min_num=1, max_num=10, max_file_size=1024 * 1024 * 25)
    class Meta:
        model = DICOMData
        fields = ['dicom_file']
class EcgReportForm(forms.ModelForm):
    class Meta:
        model = EcgReport
        fields = ['pdf_file']



class XrayReportForm(forms.ModelForm):
    class Meta:
        model = XrayReport
        fields = ['pdf_file']

class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField(label="Upload PDF")
    location = forms.ModelChoiceField(queryset=Location.objects.all(), label="Select Location")

class ECGUploadForm(forms.Form):
    ecg_file = MultiFileField(min_num=1, max_num=50, max_file_size=1024 * 1024 * 5)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), label="Select Location", required=True)