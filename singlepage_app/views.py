from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

# The texts are much longer in reality, but have 
# been shortened here to save space
texts = [
    "<h2>Section 1</h2><p>这是第一部分的内容。这里可以展示一些文本信息。</p><img src='https://picsum.photos/300/200?random=1' alt='图片1' width='300'>",
    "<h2>Section 2</h2><p>这是第二部分的内容。这里可以展示更多文本和图片。</p><img src='https://picsum.photos/300/200?random=2' alt='图片2' width='300'>",
    "<h2>Section 3</h2><p>这是第三部分的内容。这里可以展示最终的内容。</p><img src='https://picsum.photos/300/200?random=3' alt='图片3' width='300'>"
]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")
