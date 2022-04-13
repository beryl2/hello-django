from django.shortcuts import render, redirect

from .models import Category, Image


# Create your views here.
def gallery_view(request):
    category = request.GET.get('category', 'all')

    categories = Category.objects.all()

    if category == 'all':
        images = Image.objects.all()
    else:
        try:
            cat = Category.objects.get(name=category)
            images = Image.objects.filter(category=cat)
        except Category.DoesNotExist:
            images = []

    context = {
        "categories": categories,
        "images": images
    }
    return render(request, 'photos/gallery.html', context)


def photo_details_view(request, pk):
    try:
        image = Image.objects.get(pk=pk)
    except Image.DoesNotExist:
        image = None
    
    context = { "image": image }
    return render(request, 'photos/photo.html', context)


def add_photo_view(request):
    return render(request, 'photos/add.html')

# from django.urls import reverse
# from .forms import ImageForm
# def add_photo_view_(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('gallery'))
#     else:
#         form = ImageForm()
    
#     context = {'form': form}
#     return render(request, 'photos/add.html', context)

category_images = [
    {
        "name": "pets",
        "images": [
            {
                "src":'https://media.istockphoto.com/photos/closeup-portrait-of-funny-ginger-cat-wearing-sunglasses-isolated-on-picture-id1188445864?k=20&m=1188445864&s=612x612&w=0&h=0vuJeOxJr8Lu3Q1VdT1z7t6HcM8Oj7EVJe3CexGnH_8=', 
                "pk":1,
                "category": "pets",
            },
        ]
    },
    {
        "name": "money",
        "images": [
            {
                "src":"https://www.investopedia.com/thmb/sfFOpKbj8TUyJkvfKarzAI8WV90=/2121x1414/filters:fill(auto,1)/GettyImages-1222040206-f0faae8379c54ff58961774f75be3065.jpg",
                "pk": 10,
                "category": "money",
            },
            {
                "src": "https://www.nationalworld.com/jpim-static/image/2021/09/30/11/iPhone%2013.jpg?width=640&enable=upscale",
                "pk": 11,
                "category": "phone"
            }
        ]
    },
    {
        "name": "books",
        "images": [
            {
                "src":"https://media.wired.com/photos/5be4cd03db23f3775e466767/master/pass/books-521812297.jpg",
                "pk": 20,
                "category": "books",
            },
        ]
    },
    {
        "name": "food",
        "images": [
            {
                "src": "https://media-cldnry.s-nbcnews.com/image/upload/t_focal-758x379,f_auto,q_auto:best/rockcms/2022-03/plant-based-food-mc-220323-02-273c7b.jpg",
                "pk": 30,
                "category": "food"
            }
        ]
    },
    {
        "name":"nature",
        "images": [
            {
                "src":"https://thumbs.dreamstime.com/b/beautiful-rain-forest-ang-ka-nature-trail-doi-inthanon-national-park-thailand-36703721.jpg",
                "pk":40,
                "category":"nature"
            }
        ]
    }
]

