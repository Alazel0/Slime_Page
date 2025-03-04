import reflex as rx

#comun

# def lang() -> rx.Component:
#     return rx.Script("document.documentElement.lang='es'")
# preview = "poner una imagen aqui"

_meta = [
    {"name": "og:type", "content": "website"},
    # {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@SlimeGamer44"},
]

#index
index_title = "Slime Gamer | Enlaces de plataforma Discord con Twitter"
index_description = "poner una descripcion aqui"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)