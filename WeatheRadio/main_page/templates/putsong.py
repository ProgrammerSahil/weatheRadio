from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter

def putSong(song):
    tag =     "<iframe style=\"border-radius:12px\" src=\"https://open.spotify.com/embed/track/%s?utm_source=generator\"width=\"50%\" height=\"352\" frameBorder=\"0\" allowfullscreen=\"\" allow=\"autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture\" loading=\"lazy\"></iframe>"%song
    return tag
