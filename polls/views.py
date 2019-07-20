from django.shortcuts import render
from django.http import HttpResponse
from .models import TrackingItem
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from pyDes import des, CBC, PAD_PKCS5
import base64
# Create your views here.

@csrf_exempt
def index(request):

    secret_key = "4454GG44"
    iv = secret_key
    token = request.POST['token']

    data = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    charset = "utf-8"
    encrypted =base64.b64decode(token)
    decrypted = data.decrypt(encrypted).decode(charset)
    print ("Decrypted: " + decrypted)

    if decrypted[0:6]!="helpme":
        return HttpResponse('Permission deny', status=403)

    content = request.POST['content']
    #print(token,"\n",content) 
    q = TrackingItem()
    q.tracking_str = content
    q.upload_date = timezone.now()
    q.is_deal = False
    q.save()
    return HttpResponse("ok")