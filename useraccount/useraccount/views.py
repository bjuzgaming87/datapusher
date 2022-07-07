from django.http import JsonResponse
from .models import Useraccount
from .serializers import UseraccountSerializer
def user_list(request):
    #get all users
    #serialize
    #return in json
    users = Useraccount.objects.all()
    serializer = UseraccountSerializer(users, many=True)
    return JsonResponse({'useraccount':serializer.data})