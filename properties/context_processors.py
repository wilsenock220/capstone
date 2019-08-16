from .models import Apartment, ApartmentUnit, House



def apartment_count(request):
    count = Apartment.objects.count()
    return {'apartment_count': count}

def apartmentunit_count(request):
    count = ApartmentUnit.objects.count()
    return {'apartmentunit_count': count}

def house_count(request):
        count = House.objects.count()
        return {'house_count': count}
    
    