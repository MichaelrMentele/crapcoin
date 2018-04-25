from django.shortcuts import render
from django.views import View
import json

from django.http import JsonResponse

from fullnode.models import Request, Response


class RequestView(View):
    def get(self, request):
        reqs = Request.objects.all().order_by('-created_at').values()
        resps = Response.objects.all().order_by('-created_at').values()

        return render(
            request,
            'requests.html',
            {'request_responses': zip(reqs, resps)}
        )

    def post(self, request):
        req = json.loads(request.body)
        Request.objects.create(**req['request'])
        Response.objects.create(**req['response'])
        return JsonResponse({"message": "Seen by the Eye"})
