import pytest
import uuid

from http import HTTPStatus

from .conftest import create_pessoas

INVALID_TYPE = 1203
LONG_STR = "test_lksdjflasknlmsdjflojalsdkjfklaksjdiopfjlkasjdlfalsdkjfadslkjflsadkjdsafasdfasdf"


def test_create_pessoa(client, pessoa):
    response = client.post("/pessoas", json=pessoa)

    assert response.status_code == HTTPStatus.CREATED

def test_create_pessoa_ja_cadastrada(client, pessoa):
    response = client.post("/pessoas", json=pessoa)
    response = client.post("/pessoas", json=pessoa)

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

def test_create_pessoa_apelido_none(client, pessoa):
    pessoa["apelido"] = None

    response = client.post("/pessoas", json=pessoa)

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

def test_create_pessoa_wrong_type(client, pessoa):
    pessoa["apelido"] = INVALID_TYPE

    response = client.post("/pessoas", json=pessoa)

    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_create_pessoa_invalid_long_str(client, pessoa):
    pessoa["apelido"] = LONG_STR

    response = client.post("/pessoas", json=pessoa)

    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_create_pessoa_invalid_type_in_array(client, pessoa):
    pessoa["stack"][0] = INVALID_TYPE

    response = client.post("/pessoas", json=pessoa)

    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_get_pessoa(client, pessoa_id):
    response = client.get(f"/pessoas/{pessoa_id}")

    assert response.status_code == HTTPStatus.OK

def test_not_found_pessoa(client):
    id = uuid.uuid4()

    response = client.get(f"/pessoas/{id}")

    assert response.status_code == HTTPStatus.NOT_FOUND

def test_find_pessoas_by_termo(client):
    termo = "java"
    create_pessoas()

    response = client.get(f"/pessoas?t={termo}")

    assert response.status_code == HTTPStatus.OK

def test_find_pessoas_by_termo_termo_not_found(client):
    create_pessoas()

    response = client.get("/pessoas")

    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_count_pessoas(client):
    create_pessoas()

    response = client.get("/contagem-pessoas")

    assert response.text == "3"