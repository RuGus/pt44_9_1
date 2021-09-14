# --*-- coding: utf-8 --*--
"""Задача №1 Определение самого умного супергероя по версии superheroapi.com"""
import requests


def get_superhero_intelligence(name: str, access_token: str) -> int:
    """Получение информации об интеллекте супергероя из superheroapi.com

    Args:
        name(str): Superhero name
        access_token(str): Access token to superheroapi.com

    Returns:
        intelligence(int): Superhero's intelligence
    """
    url = f"https://superheroapi.com/api/{access_token}/search/{name}"
    response = requests.get(url).json()
    try:
        intelligence = int(response["results"][0]["powerstats"]["intelligence"])
    except KeyError:
        intelligence = 0
    return intelligence


access_token = input("Enter access_token to superheroapi.com: ")
heroes_list = ["Hulk", "Captain America", "Thanos"]
heroes_intelligence = {}

for hero in heroes_list:
    heroes_intelligence.setdefault(hero, get_superhero_intelligence(hero, access_token))

max_int_hero_name = ""
max_int_hero_count = 0

for hero in heroes_intelligence:
    if heroes_intelligence[hero] > max_int_hero_count:
        max_int_hero_name = hero
        max_int_hero_count = heroes_intelligence[hero]

print(
    f"Самый умный супергерой {max_int_hero_name} с интеллектом {max_int_hero_count} единиц"
)
