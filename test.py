from rocket_league_gameflip_api import RocketLeagueGameflipAPI

api = RocketLeagueGameflipAPI()
jager_url = api.gen_icon_url("Jäger 619")
print(jager_url)
