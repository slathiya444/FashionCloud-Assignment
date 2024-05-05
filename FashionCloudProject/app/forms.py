from django import forms


class FileUploadForm(forms.Form):
    main_file = forms.FileField(label='Main File', required=True)
    mapping_file = forms.FileField(label='Mapping File', required=False)
