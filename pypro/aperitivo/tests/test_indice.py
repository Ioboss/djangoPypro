import pytest
from django.urls import reverse

from pypro.base.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivo:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    {
        'Video aperitivo : Motivação',
        'Instalação no Windows'
    }
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)


@pytest.mark.parametrize(
    'slug',
    {
        'motivacao',
        'instalacao-windows'
    }
)
def test_link_video(resp, slug):
    video_link = reverse('aperitivo:video', args=(slug,))
    assert_contains(resp, f'href="{video_link}"')
