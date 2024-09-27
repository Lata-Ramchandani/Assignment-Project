from django.shortcuts import render
from .models import AssignmentModel
from django.db import transaction
import threading

def assignment_signal(request):
    print(f"Main thread: {threading.get_ident()}")
    try:
        with transaction.atomic():
            assignment_obj = AssignmentModel.objects.create(name='Assignment Object')
            print("Object created...")
            raise Exception("Transaction Error")
    except:
        print("Transaction Rolled Back")

    return render(request, 'my_app/assignment_sample.html',{'object':assignment_obj})
