from flask_swagger_ui import get_swaggerui_blueprint


BANCO_URL = "/api/docs/banco"
BANCO_API_URL = "/static/banco/banco_docs.yaml"

PLAYER_URL = "/api/docs/player"
PLAYER_API_URL = "/static/player/player_docs.yaml"

banco_swagger_blueprint = get_swaggerui_blueprint(
    base_url=BANCO_URL,
    api_url=BANCO_API_URL 
)

player_swagger_blueprint = get_swaggerui_blueprint(
    base_url= PLAYER_URL,
    api_url= PLAYER_API_URL
)