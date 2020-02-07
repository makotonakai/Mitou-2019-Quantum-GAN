from django.shortcuts import render

# Create your views here.
from .forms import ContactForm
from django.http import HttpResponse
import io
import matplotlib.pyplot as plt
import numpy as np

image = []

#png画像形式に変換数関数
def plt2png():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=200)
    s = buf.getvalue()
    buf.close()
    return s

# html表示view
def index(request):
    form = ContactForm()
    hoge = {
        'form': form,
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print("post")
        global image
        image = []
        #formで送信された値を取得
        if form.is_valid():
            print("VALIDATION SUCCESS")
            for i in range(16):
                image.append(int(form.cleaned_data['color'+str(i)]))
            image = np.array(image)
            image = image.reshape(4,4)
            return render(request, 'qgan/result.html', {'form': form})
    return render(request, 'qgan/index.html', hoge)

import sys
sys.path.append("../../../qwgan_code")
import train as qwgan

#画像埋め込み用view
def img_plot(request):
    global image
    image = qwgan.main(image)
    plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False)
    plt.tick_params(bottom=False,left=False,right=False,top=False)
    plt.imshow(image, cmap='gray')
    png = plt2png()
    plt.cla()
    response = HttpResponse(png, content_type='image/png')
    return response
