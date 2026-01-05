from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Image
from .forms import ImageUploadForm

def home(request):
    return render(request, 'gallery/home.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            if request.user.is_authenticated:
                image.uploaded_by = request.user
            image.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('image_list')
    else:
        form = ImageUploadForm()
    return render(request, 'gallery/upload.html', {'form': form})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'gallery/image_list.html', {'images': images})
