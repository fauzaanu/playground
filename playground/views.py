from django.http import HttpResponse
from .models import Pizza, Topping


# Create your views here.
def index(request):
    # create_100_pizzas()

    # getting related data
    pizzas = Pizza.objects.all()
    for pizza in pizzas:
        for topping in pizza.topping_set.all():
            print(topping.name)

    return HttpResponse(pizzas)


def create_100_pizzas():
    """
    Helper to add some fake data
    """
    from .models import Pizza, Topping
    import random
    import string

    for i in range(100):
        name = ''.join(random.choices(string.ascii_uppercase, k=10))
        description = ''.join(random.choices(string.ascii_lowercase, k=100))
        price = random.uniform(5, 20)

        pizza = Pizza(name=name, description=description, price=price)
        pizza.save()

        for j in range(5):
            name = ''.join(random.choices(string.ascii_lowercase, k=10))
            topping = Topping(name=name)
            topping.save()
            pizza.topping_set.add(topping)
        pizza.save()
