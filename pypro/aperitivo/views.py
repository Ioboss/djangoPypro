from django.shortcuts import render


def video(request, slug):
    videos = {'motivacao': {'titulo': 'Video aperitivo : Motivação', 'vimeo_id': '602764344?h=963b6c3f44'},
              'instalacao-windows': {'titulo': 'Instalação no Windows', 'vimeo_id': '251497668'},
              }
    video = videos[slug]
    return render(request, 'aperitivo/video.html', context={'video': video})
