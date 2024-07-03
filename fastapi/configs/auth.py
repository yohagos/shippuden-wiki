from fastapi import Security, Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from keycloak import KeycloakOpenID
from fastapi_keycloak_middleware import KeycloakConfiguration
from configs.settings import settings
from schemas.user import User

""" kc_url = "hhtp://localhost:9090/auth/"

keycloak_config = KeycloakConfiguration(
    url=kc_url,
    realm=settings.realm,
    client_id=settings.client_id,
    client_secret_key=settings.client_secret,
    authentication_scheme="Token",
) """

