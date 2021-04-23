from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

texts = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tortor mauris, maximus semper volutpat vitae, varius placerat dui. Nunc consequat dictum est, at vestibulum est hendrerit at.",
"Mauris suscipit neque ultrices nisl interdum accumsan. Sed euismod, logula eget tristique semper, lectus est pellentesque dui, sit amet rhoncus leo mi nec orci. Curabitur hendrerit, est in ultricies interdum, lacus lacus aliquam mauris, vel vestibulum magna nisl id arcu.",
"Cras luctus tellus acconvallis venenatis. Cras consequat tempor tincidunt. Proin ultricies purus mauris, non tempor turpis mollis id. Nam iaculis risus mauris, quis ornare neque semper vel."]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")