<<<<<<< HEAD
from django.shortcuts import render

def lobby(request):
    return render(request, 'chat/lobby.html')
=======
from rest_framework import status, viewsets
from rest_framework.response import Response
from .forms import UploadForm
from django.views.decorators.csrf import csrf_exempt
from .rag import process_document
class DocumentViewSet(viewsets.ModelViewSet):
    http_method_names = ['post'] 
    
    # make sure to reactivate csrf protection and integrate login/register for the users, the csrf token will get taken in the frontend out of the cookies and sent with the request
    @csrf_exempt
    def create(self, request, *args, **kwargs):
        if request.FILES:
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # process document here
                print(form.instance.document.path)
                process_document(form.instance.document.path)
                return Response({"succes": True}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> feat/rag
