from django.views import generic
from .forms import InquiryForm

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FromView):
    template_name = "inquiry.html"
    form_class = InquiryForm

# Create your views here.