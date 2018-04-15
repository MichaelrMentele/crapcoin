from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from sauron.models import Request


class RequestView(View):
    def get(self, request):
        reqs = Request.objects.all().order_by('-created_at')
        return render(request, 'index.html', {'requests': reqs})

    def post(self, request):
        Request.objects.create(body=request.body)
        return JsonResponse({"message": "Seen by the Eye"})
