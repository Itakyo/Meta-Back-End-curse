from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Welcome to Little Lemon !")

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu for Little Lemon")

def book(request):
    return HttpResponse("Make a booking")
################################################

# def menuitems(request, dish):
#     items = {
#         'pasta': 'wrgnwifnswoseiofnwofno',
#         'falafel': 'wfpewmwienfpiweiwenmfwef-wef-m',
#         'cheescake': 'wepfinmweiofnweofnweofnwe'
#     }

#     description = items[dish]

#     return HttpResponse(f"<h2> {dish} </h2>"+ description)

###########################

# def home(request):
#     path = request.path
#     scheme = request.scheme
#     method = request.method
#     address = request.META['REMOTE_ADDR']
#     user_agent = request.META['HTTP_USER_AGENT']
#     path_info = request.path_info
    
#     response = HttpResponse()
#     response.headers['Age'] = 20

#     msg = f"""
#         Path:{path}
#         Address:{address}
#         Scheme:{scheme}
#         Method:{method} 
#         User agent:{user_agent}
#         Path info:{path_info}    
#         Response header:  {response.headers}
#     """
  
#     # path = request.path
#     # response = HttpResponse("This works !")
#     # return response
#     return HttpResponse(msg, content_type = 'text/hmtl', charset ='utf-8'  )
    