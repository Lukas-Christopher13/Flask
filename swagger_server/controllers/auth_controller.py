import connexion
import six

from swagger_server.models.auth_bancologin_body import AuthBancologinBody  # noqa: E501
from swagger_server.models.auth_salacode_body import AuthSalacodeBody  # noqa: E501
from swagger_server.models.createplayer_code_body import CreateplayerCodeBody  # noqa: E501
from swagger_server.models.invalid_username import InvalidUsername  # noqa: E501
from swagger_server.models.refresh_token import RefreshToken  # noqa: E501
from swagger_server.models.success_login import SuccessLogin  # noqa: E501
from swagger_server import util


def auth_banco_login_post(body=None):  # noqa: E501
    """Permite logar como \&quot;Banco\&quot;

    O usuário insere um &#x27;username&#x27; e um &#x27;password&#x27; valida e recebe um token de autorização e outro de refresh. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SuccessLogin
    """
    if connexion.request.is_json:
        body = AuthBancologinBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_create_player_code_post(code, body=None):  # noqa: E501
    """Cria um player

     # noqa: E501

    :param code: O codigo da sala em que o usuário vai pertencer
    :type code: str
    :param body: 
    :type body: dict | bytes

    :rtype: SuccessLogin
    """
    if connexion.request.is_json:
        body = CreateplayerCodeBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_refresh_post(body=None):  # noqa: E501
    """Recebe um &#x27;refresh_token&#x27; e retorna um token atualizado

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = RefreshToken.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_sala_code_post(body=None):  # noqa: E501
    """Verifica se uma sala existe e retorna o seu codigo

    Verifica se uma sala existe e se sim, retorna um json com o codigo da sala # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AuthSalacodeBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
