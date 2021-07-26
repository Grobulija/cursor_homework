from django.http import HttpResponse
import random


def status(request):
	return HttpResponse("OK")


def random_color(request):
	color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
	html = f'<html><body bgcolor={color}>Random color: {color}</body></html>'
	return HttpResponse(html)
