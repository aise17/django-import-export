from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadForm
from .models import Document

def upload_file(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			instance = Document(docfile = request.FILES['docfile'])
			instance.save()
			return HttpResponseRedirect('uploads/')
	else:
		form = UploadForm()
	return render(request, 'upload.html', {'form': form})