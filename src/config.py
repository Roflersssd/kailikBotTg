import os

TOKEN = os.environ['HOOKAH_BOT_TOKEN']

HELLO_MESSAGE = "💨 Привет! Этот бот покажет тебе кальянные, которые находятся поблизости и даст краткий обзор на них..."

HELP_MESSAGE = "TODO"

MAP_TOKEN = "675ff94ca0c5c7577ba070b4b116e40d360d7970"

MAP_SECRET = "2893bff858838d79e2ae73de299f251aedbb1d04"

HOME_EMOJI = '🏠'

MESSAGES_PATH = 'channel_messages.json'

DIRECT_GEO_API = "https://catalog.api.2gis.com/3.0/items/geocode?lat={}&lon={}&fields=items.point&key=ruxnee7092"

REVERT_GEO_API = "https://catalog.api.2gis.com/3.0/items/geocode?q={}&fields=items.point&key=ruxnee7092"