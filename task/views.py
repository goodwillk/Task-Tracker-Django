from .serializers import TaskDetailSerializer
from .models import TaskDetail
from django.http import HttpResponse

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

class TaskCreateFilterList(generics.ListAPIView):
    """Filter to get objects having a particular range of 'created_at' inside models'"""
    serializer_class = TaskDetailSerializer
    filterset_fields = ('created_at')
    
    def get_queryset(self):
        queryset = TaskDetail.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date:
            return queryset.filter(basemodel_ptr_id__created_at__range=[start_date, end_date])


class TaskEstimateFilterList(generics.ListAPIView):
    """Filter to get objects having a particular range of 'estimated_time' inside models'"""
    serializer_class = TaskDetailSerializer
    filterset_fields = ('estimated_time')
    
    def get_queryset(self):
        queryset = TaskDetail.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date:
            return queryset.filter(estimated_time__range=[start_date, end_date])


class TaskSearchFilterList(generics.ListAPIView):
    """Filter to check if a key is present in 'task' json field inside models"""
    serializer_class = TaskDetailSerializer
    filterset_fields = ('task')
    
    def get_queryset(self):
        queryset = TaskDetail.objects.all()
        key = self.request.query_params.get('key', None)
        if key:
            return queryset.filter(task__has_key=key)



class TaskList(APIView):
    """ No Primary Key Used
        1. GET - Will list all data 
        2. POST - Will create a new entry"""
    def get(self, request):
        """Will return all the objects from the database - GET"""
        try:
            dataset = TaskDetail.objects.all()
            serializer = TaskDetailSerializer(dataset, many=True)
            return Response(serializer.data)
        
        except Exception as e:
            return HttpResponse(e)


    def post(self, request):
        """Will create a new entry in database - POST"""
        try:
            stream = io.BytesIO(request.body)           #request.body is json data coming from FE
            python_data = JSONParser().parse(stream)

            serializer = TaskDetailSerializer(data=python_data)     #Pass only python data in serializer
            serializer = serializer.create(python_data)

            # if serializer.is_valid():             #For custom create we will create custom validation in serializers
            #     print("is valid called in POST")
            #     serializer.save()
            #     return Response(serializer.data)   
            return Response(serializer.task)
        except Exception as e:
            return HttpResponse(e)



class TaskSpecific(APIView):
    """ Operation on Specific Entry (Through PK)
        1. GET - Will show specific entry 
        2. PUT - Will be used to update an entry
        3. PATCH - Will be used to update an entry
        4. DELETE - Will be used to delete an object"""
    def get(self, request, pk=None):
        """Will return object of a specific task - GET"""
        try:
            dataset = TaskDetail.objects.get(pk=pk)
            serializer = TaskDetailSerializer(dataset)
            return Response(serializer.data)

        except Exception as e:
            return HttpResponse(e)
    
    
    def put(self, request, pk=None):
        """Will update all values of a specific entry in database - PUT"""
        try:
            dataset = TaskDetail.objects.get(pk=pk)
            
            stream = io.BytesIO(request.body)           #request.body is json data coming from FE
            python_data = JSONParser().parse(stream)
            
            serializer = TaskDetailSerializer(instance=dataset, data=python_data)
            serializer = serializer.update(dataset, python_data)
            
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response(serializer.data)
            return Response(serializer.task)

        except Exception as e:
            return HttpResponse(e)
            
    
    def patch(self, request, pk=None):
        """Will update all values of a specific entry in database - PATCH"""
        try:
            dataset = TaskDetail.objects.get(pk=pk)
            
            stream = io.BytesIO(request.body)           #request.body is json data coming from FE
            python_data = JSONParser().parse(stream)
            
            serializer = TaskDetailSerializer(dataset, data=python_data, partial=True)
            serializer = serializer.update_patch(dataset, python_data)
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response(serializer.data)
            return Response(serializer.task)
        
        except Exception as e:
            return HttpResponse(e)


    def delete(self, request, pk=None):
        """Will delete an object - DELETE"""
        try:
            dataset = TaskDetail.objects.get(pk=pk)
            dataset.delete()
            data = "Object Deleted Successfully."
            return Response(data=data ,status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return HttpResponse(e)



# @api_view(['GET'])
# def list(request):
#     """Will return all the data from the database - GET"""
#     dataset = TaskDetail.objects.all()
#     serializer = TaskDetailSerializer(dataset, many=True)
        
#     return Response(serializer.data)


# @api_view(['GET'])
# def retrieve(request, pk=None):
#     """Will return data of a specific task - GET"""
#     dataset = TaskDetail.objects.all()
#     specific_data = get_object_or_404(dataset, pk=pk)
#     serializer = TaskDetailSerializer(specific_data)
        
#     return Response(serializer.data)


# @api_view(['POST'])
# def create(request):
#     """Will create a entry in database - POST"""
#     serializer = TaskDetailSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['PUT'])
# def put(request, pk=None):
#     """Will update all values of a specific entry in database - PUT"""
#     dataset = TaskDetail.objects.get(pk=pk)
#     serializer = TaskDetailSerializer(instance=dataset, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)


# @api_view(['PATCH'])  
# def patch(request, pk=None):
#     """Will update all values of a specific entry in database - PATCH"""
#     dataset = TaskDetail.objects.get(pk=pk)
#     serializer = TaskDetailSerializer(instance=dataset, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def delete(request, pk=None):
#     """Will delete an object - DELETE"""
#     dataset = get_object_or_404(TaskDetail, pk=pk)
#     dataset.delete()
        
#     return HttpResponse("Object Deleted")


"""Not Required"""
# class TaskTimeFilter(FilterSet):
#     start_date_estimate = DateTimeFilter(field_name='estimated_time', lookup_expr='gte')
#     end_date_estimate = DateTimeFilter(field_name='estimated_time', lookup_expr='lte')
    
#     start_date_created = DateTimeFilter(field_name='created_at', lookup_expr='gte')
#     end_date_created = DateTimeFilter(field_name='created_at', lookup_expr='lte')
    
    # class Meta:
    #     model = TaskDetail
    #     fields = ['start_date_estimate', 'end_date_estimate', 'start_date_created', 'end_date_created']




"""Not Working  --->  Custom Filter Class"""
# class TaskFilter(FilterSet):
#     start = IsoDateTimeFilter(field_name="estimated_time", lookup_expr='gte')
#     end = IsoDateTimeFilter(field_name="estimated_time", lookup_expr='lte')

#     class Meta:
#         model = TaskDetail
#         fields = ['start', 'end']

# class TaskFilterList(viewsets.ReadOnlyModelViewSet):
#     serializer_class = TaskDetailSerializer
#     filter_backends = [DjangoFilterBackend]
#     filter_class = TaskFilter
#     queryset = TaskDetail.objects.all()
#     # filterset_fields = ('estimated_time')
    

