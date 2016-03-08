from client.models import Client, Car
from registration.signals import user_registered

def user_created(sender, user, request, **kwargs):
    client = Client(user=user)
    client.save()
    car = Car(make=request.POST['make'], model=request.POST['model'],
              color=request.POST['color'], state=request.POST['state'],
              license_plate=request.POST['license_plate'], client=client)
    car.save()

user_registered.connect(user_created)