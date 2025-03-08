from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="tu_clave_secreta")

config = Config(".env")
oauth = OAuth(config)

# Configuración de Discord
discord = oauth.register(
    "discord",
    client_id="TU_DISCORD_CLIENT_ID",
    client_secret="TU_DISCORD_CLIENT_SECRET",
    authorize_url="https://discord.com/oauth2/authorize",
    access_token_url="https://discord.com/api/oauth2/token",
    client_kwargs={"scope": "identify email"},
)

# Configuración de Twitter
twitter = oauth.register(
    "twitter",
    client_id="TU_TWITTER_CLIENT_ID",
    client_secret="TU_TWITTER_CLIENT_SECRET",
    authorize_url="https://api.twitter.com/oauth/authorize",
    access_token_url="https://api.twitter.com/oauth/access_token",
    client_kwargs={"scope": "read write"},
)

# Endpoints para Discord

@app.get("/auth/discord")
async def login_discord(request: Request):
    redirect_uri = request.url_for("auth_discord_callback")
    return await discord.authorize_redirect(request, redirect_uri)

@app.get("/auth/discord/callback")
async def auth_discord_callback(request: Request):
    token = await discord.authorize_access_token(request)
    user = await discord.parse_id_token(request, token)
    return {"user": user}

# Endpoints para Twitter

@app.get("/auth/twitter")
async def login_twitter(request: Request):
    redirect_uri = request.url_for("auth_twitter_callback")
    return await twitter.authorize_redirect(request, redirect_uri)

@app.get("/auth/twitter/callback")
async def auth_twitter_callback(request: Request):
    token = await twitter.authorize_access_token(request)
    user = await twitter.parse_id_token(request, token)
    return {"user": user}
