from django.db import models

#create the choices for the product category
PRODUCT_CHOICES = [
    ('LAP', 'Laptop'),
    ('DESK', 'Desktop'),
    ('MOB', 'Mobile Phone'),
    ('TAB', 'Tablet Phone'),
    ('MTR', 'Monitor'),
    ('TV', 'Television'),
]

MOBILE_PRODUCT_BRANDS = [
    #mobile brands
    ('MI', 'Xioami'),
    ('IPH' 'Apple'),
    ('SAM', 'Samsung'),
    ('VIVO', 'Vivo'),
    ('OPPO', 'Oppo'),
    ('REME', 'Realme'),
    ('MIMAX', 'Micromax'),
]

LAPTOP_PRODUCT_BRANDS = [
    #laptop and desktop brands
    ('APP', 'Apple'),
    ('DELL', 'Dell'),
    ('HP', 'HP'),
    ('LNO', 'Lenovo'),
    ('ACER', "Acer"),
    ('ASUS', 'Asus'),
]

TV_PRODUCT_BRANDS = [
    # monitor and television brands
    ('LG', 'LG'),
    ('SONY', 'Sony'),
    ('SAMTV', 'Samsung'),
    ('MITV', 'Xioami'),   
]
# Create Product model
class Product(models.Model):
    #define the good variables for product categories
    LAPTOP = 'LAP'
    DESKTOP = 'DESK'
    MOBILE = 'MOB'
    TABLET = 'TAB'
    MONITOR = 'MTR'
    TV = 'TV'
    '''#define the good variables for mobile Product brands
    XIOAMI_MOBILE = 'MI'
    IPHONE = 'IPH'
    SAMSUNG_MOBILE = 'SAM'
    VIVO = 'VIVO'
    OPPO = 'OPPO'
    REALME = 'REME'
    MIMAX = 'MICROMAX'
    #define the good variables for Laptop Product Brands
    APPLE = 'APP'
    DELL = 'DELL'
    HP = 'HP'
    LENOVO = 'LNO'
    ACER = 'ACER'
    ASUS = 'ASUS'
    #define the good variables for TV product Brands
    LG = 'LG'
    SONY = 'SONY'
    SAMSUNGTV = 'SAMTV'
    XIOAMI_TV = 'MITV'
    '''

    PRODUCT_CATEGORY = [
        (LAPTOP , 'Laptop'),
        (DESKTOP , 'Desktop'),
        (MOBILE , 'Mobile Phone'),
        (TABLET , 'Tablet Phone'),
        (MONITOR , 'Monitor'),
        (TV , 'Television'),
    ]

    #Defines all the attributes of the Product model
    name = models.CharField(max_length= 100)
    image = models.ImageField(upload_to = 'media/profile_images', default='media/profile_images/default.jpg')
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length = 5, choices=PRODUCT_CATEGORY)
    released_date = models.DateField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'products')

    def __str__(self):
        self.return f'{self.id} {self.name}'
