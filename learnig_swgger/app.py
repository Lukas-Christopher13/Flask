from flask import Flask
from flask_cors import CORS
from flask import jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app)

SWAGGER_URL = "/docs"
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
)

app.register_blueprint(swaggerui_blueprint)


@app.route("/docs")
def docs():
    return jsonify({
  "openapi": "3.0.0",
  "info": {
    "title": "Test api",
    "description": "minha api de teste com o swegger",
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "http://localhost:5000/",
      "description": "localhost"
    }
  ],
  "paths": {
    "/hello": {
      "get": {
        "summary": "Retorna uma mensagem \"hello world\"",
        "description": "Rotorna um json contendo uma mensagem de \"hello world\"",
        "responses": {
          "200": {
            "description": "mensagem recebida com sucesso",
            "content": {
              "application/json": {
                "schema": {
                  "type": "string"
                }
              }
            }
          }
        }
      }
    },
    "/parametro/{num}": {
      "get": {
        "summary": "retornam o numero passado",
        "parameters": [
          {
            "name": "num",
            "in": "path",
            "required": true,
            "description": "um numero qualquer",
            "schema": {
              "type": "integer",
              "format": "int64",
              "minimum": 1
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/create": {
      "post": {
        "summary": "criar um usuário",
        "description": "rota usada para criar usuário",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "username": {
                    "type": "string"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "o usuário foi criado com sucesso"
          }
        }
      }
    },
    "/users/{userId}": {
      "get": {
        "summary": "Returns a user by ID.",
        "parameters": [
          {
            "name": "userId",
            "in": "path",
            "required": true,
            "description": "The ID of the user to return.",
            "schema": {
              "type": "integer",
              "format": "int64",
              "minimum": 1
            }
          }
        ],
        "responses": {
          "200": {
            "description": "A user object.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/User"
                }
              }
            }
          },
          "400": {
            "description": "The specified user ID is invalid (not a number)."
          },
          "404": {
            "description": "A user with the specified ID was not found."
          },
          "default": {
            "description": "Unexpected error"
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "User": {
        "type": "object",
        "properties": {
          "username": {
            "type": "string",
            "example": "lukas"
          },
          "password": {
            "type": "string",
            "example": 123
          }
        },
        "required": [
          "username",
          "password"
        ]
      }
    }
  }
})



@app.route("/hello")
def hello():
    return jsonify({"msg": "hello world"})

@app.route("/parametro/<int:num>")
def parametro(num):
    return jsonify({"msg": f"{num}"})

@app.route("/create", methods=["POST"])
def create():
    username = request.json.get("username")

    return jsonify({"msg": f"criado {username}"})

if __name__ == "__main__":
    app.run(debug=True)

