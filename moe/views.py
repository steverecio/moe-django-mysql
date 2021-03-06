import random
from django.http import HttpResponse
from django.shortcuts import render
from moe.models import Moe


RMS_PHOTOS = [
    "https://stallman.org/photos/rms-working/mid/mid_p1000844.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_0554.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_1755.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_3235.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_3658.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_4188.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_working-with-the-devil.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_p1000541.jpg",
]


def index(request):
    moes = Moe.objects.all().values_list('url', flat=True)
    moe_src = random.choice(moes or RMS_PHOTOS)
    return render(request, 'moe/index.html', {'moe_src': moe_src})

