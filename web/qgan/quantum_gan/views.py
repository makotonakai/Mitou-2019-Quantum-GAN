from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
import io
import matplotlib.pyplot as plt

#png画像形式に変換数関数
def plt2png():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=200)
    s = buf.getvalue()
    buf.close()
    return s


# html表示view
def index(request):
    return render(request, 'qgan/index.html')

#画像埋め込み用view
def img_plot(request):
    # matplotを使って作図する
    image = [[255, 255],[0, 0]]
    plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False)
    plt.tick_params(bottom=False,left=False,right=False,top=False)
    plt.imshow(image, cmap='gray')
    png = plt2png()
    plt.cla()
    response = HttpResponse(png, content_type='image/png')
    return response