
# mgptapp/views.py
from django.shortcuts import render, redirect
from .forms import TextForm
from .models import Text
from .mgpt_model import generate_text

def text_processor_view(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text_instance = form.save(commit=False)
            text_instance.generated_text = generate_text(text_instance.input_text)
            text_instance.is_match = (text_instance.input_text.strip() == text_instance.generated_text.strip())
            text_instance.save()
            return redirect('text_detail', pk=text_instance.pk)
    else:
        form = TextForm()
    return render(request, 'form.html', {'form': form})

 # def text_detail_view(request, pk):
 #     text_instance = Text.objects.get(pk=pk)
 #     return render(request, 'mgptapp/text_detail.html', {'text': text_instance})


# Create your views here.
