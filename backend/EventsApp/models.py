from django.db import models 
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator 
from decimal import Decimal 
from phone_field import PhoneField 
from datetime import date

class Event(models.Model): 
    name = models.CharField(max_length = 50) 
 
    def __str__(self): 
        return self.name 

    class Meta: 
        verbose_name = "Event" 
        verbose_name_plural = "Event" 
 
 
class HomePageGallery(models.Model): 
   text = models.CharField(max_length = 30) 
   image = models.ImageField(null=True, blank=True ) 
    
   def __str__(self):
        return self.text
        
   class Meta: 
        verbose_name = "Home Page Gallery" 
        verbose_name_plural = "Home Page Gallery" 
 
 
class Place(models.Model): 
    RATING_CHOICES = [
        (int(rate), int(rate))
          for rate in range(1, 6)
        ]
    rate = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    eventID = models.ManyToManyField("Event") 
    name = models.CharField(max_length = 50) 
    location = models.CharField(max_length = 50) 
    crew = models.BooleanField(default = False) 
    capacity = models.IntegerField(validators=[MinValueValidator(Decimal('1'))]) 
    period = models.DecimalField(max_digits = 3, decimal_places = 2, validators=[MinValueValidator(Decimal('0.01'))]) 
    cost = models.IntegerField(validators=[MinValueValidator(Decimal('1'))]) 
    image = models.ImageField(upload_to='images/')  

    def __str__(self): 
        return self.name     
     
    @property 
    def imageURL(self): 
        try: 
            url = self.image.url 
        except: 
            url ='' 
        return url 

    class Meta: 
        verbose_name = "Place" 
        verbose_name_plural = "Place" 
        ordering=["name"] 
     
 
class Card(models.Model): 
    eventID = models.ForeignKey("Event", on_delete = models.CASCADE) 
    imgURL = models.ImageField(upload_to='images/') 
    cost = models.IntegerField(validators=[MinValueValidator(Decimal('1'))]) 
   
    class Meta: 
        verbose_name = "Card" 
        verbose_name_plural = "Card" 
 

class Decoration(models.Model): 
    Decoration_category =(
        ('Balloons','Balloons'),
        ('Flowers','Flowers'),
        ('Stands','Stands'),
        ('Tables','Tables'))
    category = models.CharField(max_length=20, choices = Decoration_category, null= False, default = 'Flowers')
    imgURL = models.URLField(max_length = 400, null = True) 
    cost = models.IntegerField(validators=[MinValueValidator(Decimal('1'))]) 
    
    def __str__(self): 
        return self.category 
     
    class Meta: 
        verbose_name = "Decoration" 
        verbose_name_plural = "Decoration" 
 

class Food(models.Model): 
    choices =(('Wedding Package','Wedding Package'),
              ('Birthday Package','Birthday Package'),
              ('Party Package','Party Package'),
              ('Graduation Package','Graduation Package'),
              ('Baptism Package','Baptism Package'),
              ('Baby Gender Package ','Baby Gender Package '))
    
    eventID = models.ManyToManyField("Event") 
    packageName = models.CharField(choices=choices,max_length = 100) 
    img = models.ImageField(null= True) 
    cost = models.IntegerField(validators=[MinValueValidator(Decimal('1'))]) 
    Main_Dish = models.CharField(max_length=200, null = True, blank = True)
    Drinks = models.CharField(max_length=200, null = True, blank = True)
    Entrees = models.CharField(max_length=200, null = True, blank = True)
    Desserts = models.CharField(max_length=200, null = True, blank = True)

    def __str__(self): 
        return self.packageName 
     
    class Meta: 
        verbose_name = "Food" 
        verbose_name_plural = "Food" 

 
class Photographer(models.Model): 
    name = models.CharField(max_length=50) 
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Please enter phone number in the format: '+963 999999999'. Up to 9 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    instagram_profile = models.URLField() 
    facebook_profile = models.URLField()
    image = models.ImageField() 
    sessionPrice = models.IntegerField(default=1) 
    description = models.TextField(null = True, blank=True, max_length = 400 , help_text='Session Description')

    class Meta: 
        verbose_name = "Photographer" 
        verbose_name_plural = "Photographer" 
 
    def __str__(self): 
        return self.name 
 
 
class ContactUs(models.Model): 
    name = models.CharField(max_length = 100) 
    email = models.EmailField() 
    message = models.TextField() 
     
    class Meta: 
        verbose_name = "ContactUs" 
        verbose_name_plural = "ContactUs" 
    
    def __str__(self): 
        return self.name


class FinalReservation(models.Model):
    customerName = models.CharField(max_length = 30, null = False)
    place = models.ForeignKey(Place, on_delete = models.CASCADE, null = False)
    date = models.DateField(default = date.today , null = False, validators = [MinValueValidator(limit_value = date.today)])
    startTime = models.TimeField(null = False)
    endTime = models.TimeField(null = False)
    num_of_guests = models.IntegerField(default = 0)
    num_of_tables = models.IntegerField(default = 0)
    crew = models.BooleanField(null = True)
    food_package = models.ForeignKey(Food, on_delete = models.CASCADE, null = True, blank = True)
    photographer = models.ForeignKey(Photographer, null = True, on_delete = models.CASCADE, blank=True)
    balloon_decoration = models.ForeignKey(Decoration, related_name = 'balloon_decoration', on_delete=models.CASCADE,null = True, blank = True, limit_choices_to={'category':'Balloons'})
    stand_decoration = models.ForeignKey(Decoration, related_name = 'stand_decoration', on_delete=models.CASCADE,null = True, blank = True, limit_choices_to={'category':'Stands'})
    table_decoration = models.ForeignKey(Decoration, related_name = 'table_decoration', on_delete=models.CASCADE,null = True, blank = True, limit_choices_to={'category':'Tables'})
    flower_decoration = models.ForeignKey(Decoration, related_name = 'flower_decoration', on_delete=models.CASCADE,null = True, blank = True, limit_choices_to={'category':'Flowers'})
    card = models.ForeignKey(Card, on_delete = models.CASCADE, null = False)
    number_of_cards = models.IntegerField(null = False)
    card_text = models.CharField(max_length = 255, null = False)
    customer_number = models.CharField(max_length = 255, null = False)  
    customer_email = models.EmailField(null = False)  
    total_price = models.IntegerField(default = 1, null = False, validators = [MaxValueValidator(1000000000), MinValueValidator(0)])
    message = models.TextField(max_length = 400, null = True, blank = True)
    
    def __str__(self): 
        return self.customerName
    
    class Meta: 
        verbose_name = "Final Reservation" 
        verbose_name_plural = "Final Reservation" 


class Gallery(models.Model):
    image = models.ImageField()
    
    class Meta: 
        verbose_name = "Gallery" 
        verbose_name_plural = "Gallery"