from django.shortcuts import render

def index(request):
    d=[
        {"id":1, 
        "name": "dafsgdhfh",
        "image": "woodland.jpeg",
        },
         {"id":2, 
        "name": "sadgfhj",
        "image": "7cf3f477777.jpg",
        },
         {"id":3, 
        "name": "sfhgjuki",
        "image": "pexels-photo.webp",
        },
         {"id":4, 
        "name": "dhgkjlio",
        "image": "pexels-photo1.jpeg",
        },
         {"id":5, 
        "name": "qewretyry",
        "image": "pexels-photo2.webp",
        },
         {"id":6, 
        "name": "xcxvbnm",
        "image": "pexels-photo3.jpeg",
        }
    ]
    return render(request, 'work/index.html', {
        "products":d,
    })

def about(request):    
    return render(request, 'work/about.html')

def contact(request):    
    return render(request, 'work/contact.html')   

def news(request): 
        d=[
           {"id":1, 
            "name": "dafsgdhfh",
            "image": "woodland.jpeg",
            },
           {"id":2, 
            "name": "sadgfhj",
            "image": "7cf3f477777.jpg",
            },
           {"id":3, 
             "name": "sfhgjuki",
             "image": "pexels-photo.webp",
             },
           {"id":4, 
              "name": "dhgkjlio",
              "image": "pexels-photo1.jpeg",
            },
           {"id":5, 
             "name": "qewretyry",
             "image": "pexels-photo2.webp",
            },
           {"id":6, 
             "name": "xcxvbnm",
             "image": "pexels-photo3.jpeg",
             },
            {"id":7, 
             "name": "xcxvbnm",
             "image": "pexels-photo4.webp",
             },
            {"id":8, 
             "name": "xcxvbnm",
             "image": "pexels.jpeg",
             },
            {"id":9, 
             "name": "xcxvbnm",
             "image": "pexels-photo3.jpeg",
             }
            ]   
        return render(request, 'work/news.html', {
           "products":d,
       })  
