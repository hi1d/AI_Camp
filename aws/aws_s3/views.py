from django.shortcuts import render
from django.http import JsonResponse
from aws_prac.settings import AWS_S3_ACCESS_KEY_ID, AWS_S3_SECRET_ACCESS_KEY
from django.conf import settings
import boto3


# Create your views here.
def index(request):
    return render(
        request,
        'index.html'
    )


def upload(request):
    file = request.FILES['file']
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_S3_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_S3_SECRET_ACCESS_KEY,
    )
    s3.upload_fileobj(
        file,
        f"{settings.AWS_STORAGE_BUCKET_NAME}",
        f"{file}",
        ExtraArgs={
            "ContentType": file.content_type,
            'ACL': "public-read",
        }
    )
    return JsonResponse({'msg': 'success'})
