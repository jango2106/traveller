from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/api"
API_URL = "/api/specs"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Travellers API"
    }
)
