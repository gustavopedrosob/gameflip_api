from rocket_league_gameflip_api import RocketLeagueGameflipAPI
import rocket_league_utils as rl_utils

api = RocketLeagueGameflipAPI()
jager = rl_utils.ReprItem("Jäger 619", "car", False, "crimson")
respective_jager = api.get_data_item(jager)
jager_url = api.gen_icon_url("Jäger 619")

print(jager_url)
print(respective_jager.get_full_icon_url(respective_jager.get_icon_by_color(jager.color)))
