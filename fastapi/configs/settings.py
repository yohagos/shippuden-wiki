from schemas.user import authConfiguration

keycloak_url ="http://localhost:9090/"
realm = "shippuden"

""" settings = authConfiguration(
    server_url=keycloak_url,
    realm=realm,
    client_id="shippuden",
    client_secret="",
    authorization_url=f"{keycloak_url}realms/{realm}/protocol/openid-connect/auth",
    token_url=f"{keycloak_url}/realms/{realm}/protocol/openid-connect/token",
) """