from django.shortcuts import render_to_response


def index(request):
    return render_to_response("index.html")


def about(request):
    return render_to_response("about.html")


def order(request):
    return render_to_response("order.html")


def contact(request):
    return render_to_response("contact.html")
