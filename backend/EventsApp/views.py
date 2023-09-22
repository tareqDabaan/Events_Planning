from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from django.db.models import Q


class Event(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    
    
#Class Based View API To return one place with the given ID http://127.0.0.1:8000/api/places/1
class Place_Id(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()


#Class Based View API To return all places and gives ability to add on them
class Places_List(APIView):
    serializer_class = PlaceSerializer
    def get(self, request):
       queryset = Place.objects.all()
       serializer = PlaceSerializer(queryset, many = True)
       return Response(serializer.data)
   

#Class API to return home page gallery
class Images_Home_Page(generics.ListCreateAPIView):
    serializer_class = HomePageGallerySerializer
    queryset = HomePageGallery.objects.all()
 

#To post the customer data and save in the DataBase
class Contacts_Add(generics.CreateAPIView):
    serializer_class = ContactSerializer
    queryset = ContactUs.objects.all()
    def post(self,request,*args,**kwargs):   
        serializer = self.serializer_class(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = 404)


#An Api which takes the ID to Retrieve the customer data and give ability to Delete the customer data
class Contacts_Delete(generics.RetrieveDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = ContactUs.objects.all()


# An Api to list and display all Customers Data (GET)
class Contacts_List(generics.ListAPIView):
    serializer_class = ContactSerializer
    queryset = ContactUs.objects.all()
    lookup_field = 'id'


#An API that List Photographer data 
class Photographer_List(generics.ListAPIView):
    serializer_class = PhotographerSerializer
    queryset = Photographer.objects.all()


#An API Function that returns data for all cards
class Cards_List(generics.ListCreateAPIView):
    serializer_class = CardSerializer
    def get_queryset(self):
        queryset =  Card.objects.all().order_by('cost')   
        return queryset     


#An API Function that returns data only for the given id card
@api_view(['GET'])
def Card_List(request, id):
    try:
        card = Card.objects.get(id=id)
    except:
        return Response({'Error': f"Sorry, card with id = {id} not found"}, status = status.HTTP_204_NO_CONTENT)
    data = CardSerializer(card).data
    return Response({f'Card {id}':data})
    

#An API that returns ImageURL and Cost for decorations
class Decoration_List_Flowers(APIView):
    serializer_class = DecorationSerializer
    def get(self,request):
       queryset = Decoration.objects.filter(category = 'Flowers').order_by('cost')
       serializer = DecorationSerializer(queryset, many = True)
       return Response(serializer.data)
   
    def post(self,request):
        serializer = DecorationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        queryset = Decoration.objects.filter(category = 'Flowers')
        queryset.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
class Decoration_List_Balloons(APIView):
    serializer_class = DecorationSerializer
    def get(self,request):
        queryset = Decoration.objects.filter(category = 'Balloons').order_by('cost')
        serializer = DecorationSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = DecorationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        queryset = Decoration.objects.filter(category = 'Balloons')
        queryset.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

class Decoration_List_Stands(APIView):
    serializer_class = DecorationSerializer
    def get(self,request):
        queryset = Decoration.objects.filter(category = 'Stands').order_by('cost')
        serializer = DecorationSerializer(queryset, many = True)
        return Response(serializer.data)
   
    def post(self,request):
        serializer = DecorationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
   
    def delete(self,request):
        queryset = Decoration.objects.filter(category = 'Stands')
        queryset.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class Decoration_List_Tables(APIView):
    serializer_class = DecorationSerializer
    def get(self,request):
        queryset = Decoration.objects.filter(category = 'Tables')
        serializer = DecorationSerializer(queryset, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
   
    def post(self,request):
        serializer = DecorationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
 
    def delete(self,request):
        queryset = Decoration.objects.filter(category = 'Tables')
        queryset.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

#An Api to render all food packages except graduation and birthday packages
class Food_Packages(APIView):
    serializer_class = FoodSerializer
    def get(self, reuest):
        queryset = Food.objects.exclude(packageName__in = ['Graduation Package', 'Birthday Package']).order_by('cost')
        serializer = FoodSerializer(queryset, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK )
  
    def post(self, request):
        package_name = request.data.get('packageName')
        allowed_packages = ['Wedding Package','Baptism Package','Party Package','Baby Gender Package']
        if package_name in allowed_packages:
            serializer = FoodSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Error': f"Package name should be one of {', '.join(allowed_packages)}."},
                            status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request):
        queryset = Food.objects.exclude(packageName__in=['Graduation Package', 'Birthday Package'])
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
#ِAn Api to render only graduation and birthday food packages 
class Graduation_Birthday_Package(APIView):
    serializer_class = GraduationBirthdaySerializer
    def get(self, request):
        queryset = Food.objects.filter(Q(packageName = 'Graduation Package') | Q(packageName = 'Birthday Package')).order_by('cost')
        serializer = GraduationBirthdaySerializer(queryset, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        package_name = request.data.get('packageName')
        allowed_packages = ['Graduation Package', 'Birthday Package']
        if package_name in allowed_packages:
            serializer = GraduationBirthdaySerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Error': f"Package name should be one of {' or '.join(allowed_packages)}."},
                            status = status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request):
        queryset = Food.objects.exclude(packageName__in=['Wedding Package', 'Baptism Package', 'Party Package', 'Baby Gender Package'])
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#graceleenrita
@api_view(['POST','GET'])
def create_reservation(request):
    if request.method == 'GET':
        reservations = FinalReservation.objects.all().order_by('date')
        page = request.GET.get('page')
        if page is None:
            serializer = FinalReservationSerializer(reservations, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            paginator = Paginator(reservations, 5)
            try:
                reservations = paginator.page(page)
            except PageNotAnInteger:
                return Response({'Error':'Page is not an integer'}, status = status.HTTP_400_BAD_REQUEST)
            except EmptyPage:
                reservations = paginator.page(paginator.num_pages)
            serializer = FinalReservationSerializer(reservations, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        
    elif request.method == 'POST':
        serializer = FinalReservationSerializer(data = request.data)
        if serializer.is_valid():
            place = serializer.validated_data['place']
            date = serializer.validated_data['date']
            existing_reservations = FinalReservation.objects.filter(place = place, date = date)
            if existing_reservations.exists():
                return Response({'Message':'Place not available on this date.'}, status = status.HTTP_404_NOT_FOUND)
            serializer.save()
            return Response({'Message':'Reservation saved successfully'})
        return Response(serializer.errors, status = 400)
    
########################## An Api to return reservation dates for the place using the ID  #####################################################    
@api_view(['GET'])
def Reservation_List(request, id):
    if request.method == 'GET':
        if not id:
            return Response({'Error': 'No ID provided in URL.'})
        try:
            place = Place.objects.get(id=id)
        except Place.DoesNotExist:
            return Response({'Error': f"Place with ID {id} does not exist."})
        
        else:
            try:
                reservations = FinalReservation.objects.filter(place = id)
                if not reservations:
                    return Response({'Error': f"No reservations found for place ID {id}"})
            except:
                return Response({'Error': f"Sorry, NO reservations found for place ID {id}"}, status = status.HTTP_400_BAD_REQUEST)
            else:
                reservations_data = OnlyDateSerializer(reservations, many = True).data
                return Response(reservations_data)

@api_view(['GET'])
def gallery(request):
    if request.method == 'GET':
        try:
            gallery = Gallery.objects.all()
            serializer = GallerySerializer(gallery, many = True).data
            return Response(serializer, status = status.HTTP_200_OK)
        except:
            return Response({'Error':'No pictures found'})

