template = {
  "swagger": "2.0",
  "info": {
    "title": "Sorting Algorithm",
    "description": "See the full documentation on: https://github.com/owen-eternal/sorting#readme",
    "contact": {
      "responsibleDeveloper": "Owen Phakade",
      "email": "olwethuphakade89@gmail.com",
    },
    "version": "0.0.1"
  },
  "basePath": "/api/v1",
  "operationId": "getmyData"
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/"
}
