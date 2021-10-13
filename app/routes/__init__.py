def register_routes(api, app, root="api"):
    from app.routes.admin.controller import api as admin_api
    from app.routes.client.controller import api as client_api
    from app.routes.auth.controller import api as login_api

    api.add_namespace(admin_api, path=f"/{root}")
    api.add_namespace(client_api, path=f"/{root}")
    api.add_namespace(login_api, path=f"/{root}")
