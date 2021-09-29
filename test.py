from main import GameflipApi, Visibility


def test_visibility_argument():
    Visibility("onsale").validate()


def test_request_items():
    r = GameflipApi.request_all_item_information()
    possible_types = {item.type for item in r}
    pass


def test_rl_listing():
    gapi = GameflipApi()
    gapi.rl_listing("Chequered Flag", "Buy now!", "trail", color="Cobalt", visibility="draft")

