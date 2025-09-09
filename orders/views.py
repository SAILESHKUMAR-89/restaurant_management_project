from django.shortcuts import render

# Create your views here.
def homepage(request):
    specials = TodaySpecial.objects.all()
    return render(request, "homepage.html", {"specials":specials})