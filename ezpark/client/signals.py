from client.models import Client
from registration.signals import user_registered

def user_created(sender, user, request, **kwargs):
    client = Client(user=user, car=request.POST['car'])
    client.save()

user_registered.connect(user_created)