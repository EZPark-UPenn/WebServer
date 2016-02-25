from client.models import Client
from registration.signals import user_registered

def user_created(sender, user, request, **kwargs):
    up = Client(user=user, car=request.POST['car'])
    up.save()

user_registered.connect(user_created)