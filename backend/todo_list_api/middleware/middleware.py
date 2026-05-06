def authenticate(request, auth_service):
    token = request.headers.get("Authorization")
    if not token:
        return None
    return auth_service.authenticate(token)