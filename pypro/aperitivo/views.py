from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.titulo = titulo
        self.vimeo_id = vimeo_id
        self.slug = slug

    def get_absolute_url(self):
        return reverse('aperitivo:video', args=(self.slug,))


videos = [
    Video('motivacao', 'Video aperitivo : Motivação', '602764344?h=963b6c3f44'),
    Video('instalacao-windows', 'Instalação no Windows', '251497668')
]

videos_dct = {vdeo.slug: vdeo for vdeo in videos}


def indice(request):
    return render(request, 'aperitivo/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivo/video.html', context={'video': video})
