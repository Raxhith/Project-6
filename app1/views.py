from django.shortcuts import render

def dis_data(request):
	return render(request=request, template_name='App1/display.html')