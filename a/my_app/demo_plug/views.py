from common.djangoapps.edxmako.shortcuts import render_to_response
from django.shortcuts import render

# Create your views here.
def demoplug(request):
	return render(request,"demoplug/mydemo.html", {})
