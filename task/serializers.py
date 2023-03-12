from rest_framework import serializers
from .models import TaskDetail
from django.utils import timezone
import datetime


class TaskDetailSerializer(serializers.ModelSerializer):
    task = serializers.JSONField()
    
    # def __init__(self, data):             #Other methods also use this serializer, so __init__ connot be used
    #     task_data = TaskDetail(task = data['abc'])
        # task_data.save()
        # print(task_data.task)
        # task_data.task = data['abc']
        # task_data.created_at = data['created_at']
        # task_data.estimated_time = data['estimated_time']
        
    def create(self, data):
        print("Entered in custom create")
        task_data = TaskDetail.objects.create(task = data['abc'])
        task_data.estimated_time = data['estimated_time']
        task_data.is_task_completed = data['is_task_completed']
        task_data.save()
        return task_data
    
    def update(self, instance, data):
        instance.task = data.get('abc', instance.task)
        instance.estimated_time = data.get('estimate_time', instance.estimated_time)
        instance.is_task_completed = data.get('is_task_completed', instance.is_task_completed)
        
        instance.save()
        return instance
    
    def update_patch(self, instance, data):
        dataset = data['abc']|instance.task     #Adding two dictionaries for patch
        
        instance.task = dataset
        instance.estimated_time = data.get('estimate_time', instance.estimated_time)
        instance.is_task_completed = data.get('is_task_completed', instance.is_task_completed)
        
        instance.save()
        return instance

    class Meta:
        model = TaskDetail
        fields = '__all__'



# class TaskDetailSerializer(serializers.ModelSerializer):
#     task = serializers.JSONField()
    
#     class Meta:
#         model = TaskDetail
#         fields = ('task', )
#         extra_kwargs = {}
    
#     def create(self, validate_data):
#         task = TaskDetail.objects.create(task = validate_data['abc'])
#         task.save()
#         return task
        
        
    
