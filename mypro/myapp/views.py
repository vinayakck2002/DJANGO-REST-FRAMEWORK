from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def index(request):
    if request.method == 'GET':
        return Response({
            'name':'vinayak',
            'age':22,
            'place':'nadapuram'
        })
    elif request.method == 'POST':
        return Response({
            'name':'akshay',
            'age':20,
            'place':'panoor'
        })
    elif request.method == 'PUT':
        return Response({
            'name':'abhi',
            'age':22,
            'place':'calicut'
        })
    elif request.method == 'PATCH':
        return Response({
            'name':'hari',
            'age':21,
            'place':'calicut'
            
        })
    
