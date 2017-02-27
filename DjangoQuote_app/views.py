from django.shortcuts import render
from DjangoQuote_app.models import Quote

# Create your views here.
def get_quotes(request):
    return render(request, "DjangoQuote/home.html",
                  {'quote_list': Quote.objects.all()})