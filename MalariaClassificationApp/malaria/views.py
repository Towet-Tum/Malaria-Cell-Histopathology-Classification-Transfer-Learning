# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .models import PatientRecords
from MalariaCellHistopathologyClassification.pipeline.stage_04_prediction import (
    PredictionPipeline,
)


media = "media"
import os


def home(request):
    return render(request, "index.html")


def upload(request):
    if request.method == "POST" and request.FILES["upload"]:
        f = request.FILES["upload"]
        fss = FileSystemStorage()
        file = fss.save(f.name, f)
        file_url = fss.url(file)
        pred_img = os.path.join(media, file)
        pred = PredictionPipeline(pred_img)
        class_name, conf = pred.makePrediction()
        patient = request.user
        record = PatientRecords.objects.create(
            patient=patient, image=f, pred_class=class_name, score=conf
        )
        record.save()

        return redirect("results")

    return render(request, "upload.html")


def results(request):
    record = PatientRecords.objects.last()
    context = {"record": record}
    return render(request, "result.html", context)


def dashboard(request):
    records = PatientRecords.objects.all().order_by("-date_added")
    context = {"records": records}
    return render(request, "dashboard.html", context)


def train_model(request):
    os.chdir("../")
    os.system("dvc repro")

    # Get the current working directory
    current_directory = os.getcwd()
    print(f"Current Working Directory: {current_directory}")

    # Move to the next folder (replace 'next_folder' with the actual folder name)
    next_folder = "MalariaClassificationAPP"
    next_folder_path = os.path.join(current_directory, next_folder)

    # Change the current working directory to the next folder
    os.chdir(next_folder_path)

    # Print the new working directory
    new_directory = os.getcwd()
    print(f"New Working Directory: {new_directory}")
    return JsonResponse("Training completed succefully", safe=False)
