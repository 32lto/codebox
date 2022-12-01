from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "index.html"

class IndexView2(generic.TemplateView):
    template_name = "hoge.html"

class Sugenakore(generic.TemplateView):
    template_name = "hone.html"
# Create your views here.