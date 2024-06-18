# Decaten

## Team Info
- Team Member 1 Anton Prymush: [GitHub Profile](https://github.com/luny-06)
- Team Member 2 Andrii Druzhha: [GitHub Profile](https://github.com/GKAndrey)
- Team Member 3 Mykhailo Fatuyev: [GitHub Profile](https://github.com/mishafat)
- Team Member 4 Yaroslav Samchuk: [GitHub Profile](https://github.com/YaroslavSamchuk)

## Links
- Figma(https://www.figma.com/design/He9uAMtimSi7BggXDkfste/Decaten?node-id=0-1&t=j5Bxubp8ji2jO3ty-0)
- FigJam(https://www.figma.com/board/FJDA9tQkrUKBHibZFNrBFG/Untitled?node-id=1-14&t=DluDv1APBdXD8PLG-0)

## Description

Decaten is a site where you can buy disposable e-cigarettes.

## Libraries and Technologies

List the libraries and technologies used in the project.

- HTML
- CSS
- Java Script
- Django
- JavaScript
- Jquery
- Ajax
- Bootstrap
- SQLite3

## Models

### NameOfFilter
This model responsible for name of category of filters.
```
class NameOfFilter(models.Model):
    name = models.CharField(max_length=255)
```
- name: Name of category of filters.

### Filter
This model responsible for filters in the category.
```
class Filter(models.Model):
    name = models.CharField(max_length=255)
    name_of_filter = models.ForeignKey(NameOfFilter, on_delete=models.CASCADE)
```
- name: name of filter in category.
- name_of_filter: name of category of filters.

### Product
This model responsible for products, in our case - e-cigarettes.
```
class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    filters = models.ManyToManyField(Filter)
```
- image: -
- name: name of product.
- price: price of product.
- filters: filters, which product has.

### Flavour
This model responsible for flavours for e-cigarettes.
```
class Flavour(models.Model):
    name = models.CharField(max_length=255)
    for_product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
```
- name: name of flavour.
- for_product: defines what product uses this flavour.
- image: image of e-cigarette.

### Cart
This model responsible for cart.
```
class Cart(models.Model):
    sessionkey = models.CharField(max_length =255)
```
- sessionkey: saves session key of user.

### ProductInCart
This model responsible for product in cart.
```
class ProductInCart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    count=models.IntegerField()
    flavour = models.ForeignKey(Flavour, on_delete=models.CASCADE, blank=True, null=True)
```
- product: saves id of product which user added to cart.
- cart: saves id of cart which user uses.
- count: count of added product.
- flavour: defines flavour of saved product.

### Carusel
This model is responsible for images in slider on the main page.
```
class Carusel(models.Model):
    img = models.ImageField()
```
- img: image, which will be added to slider.

### MyUser
This model is responsible for saving registration data of user.
```
class MyUser(User):
    number = models.IntegerField()
```
- number: saves phone number of user.
