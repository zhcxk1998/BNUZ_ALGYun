from django.shortcuts import render, render_to_response

# Create your views here.
def page_not_found(requests):
    return render_to_response('404page/404.html')