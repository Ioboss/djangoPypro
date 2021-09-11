import pytest
from django.urls import reverse

from pypro.base.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivo:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200

def test_titulo_video(resp):
    assert_contains(resp, '<h1>Video aperitivo : Motivação</h1>')

def test_conteudo_video(resp):
    assert_contains(resp, 'src="https://player.vimeo.com/video/602764344?h=963b6c3f44"')
