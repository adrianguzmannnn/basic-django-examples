import sys
from django.shortcuts import render


class Views():

    def home(request):
        return render(request, 'home.html', {'module': sys._getframe().f_code.co_name})
