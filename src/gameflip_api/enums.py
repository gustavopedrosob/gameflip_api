from enum import Enum

class ShippingPaidBy(Enum):
    BUYER = "buyer"
    SELLER = "seller"


class Category(Enum):
    GAMES = 'CONSOLE_VIDEO_GAMES'  # Video games, digital or physical
    INGAME = 'DIGITAL_INGAME'  # In-game items, digital only
    GIFTCARD = 'GIFTCARD'  # Gift cards, digital or physical
    CONSOLE = 'VIDEO_GAME_HARDWARE'  # Console game hardware, physical listing only
    ACCESSORIES = 'VIDEO_GAME_ACCESSORIES'  # Console game accessories, physical listing only
    TOYS = 'TOYS_AND_GAMES'  # Collectibles, physical listing only
    VIDEO = 'VIDEO_DVD'  # Movies, physical or digital
    OTHER = 'UNKNOWN'  # Unsupported category


class Kind(Enum):
    ITEM = 'item'  # Item selling
    GIG = 'gig'  # Gig selling


class UPC(Enum):
    ANIMAL_CROSSING_NH = '045496596439'
    CSGO = '094922417596'
    DOTA2 = '111111111111'
    TF2 = '014633098693'
    RUST = '000000252490'
    PUBG = '000000578080'
    PUBG_LITE = 'GF00PUBGLITE'
    GTA5_PC = '710425414534'
    GTA5_PS4 = '710425474521'
    GTA5_XONE = '710425494512'
    H1Z1 = '000000433850'
    H1Z1_JS = '000000295110'
    FORTNITE = 'GFFORTNITE'
    RL_ALL = '023171037943,812872018928,812872018935,GF00RLSWITCH'
    RL_STEAM = '023171037943'
    RL_PS4 = '812872018928'
    RL_XONE = '812872018935'
    RL_SWITCH = 'GF00RLSWITCH'
    ROBLOX = 'GF0000ROBLOX'
    FALLOUT76_PC = 'GFPCFLLOUT76'
    FALLOUT76_PS4 = 'GFPSFLLOUT76'
    FALLOUT76_XONE = 'GFXOFLLOUT76'
    BORDERLANDS3_PC = 'GFPCBDLANDS3'
    BORDERLANDS3_PS4 = 'GFPSBDLANDS3'
    BORDERLANDS3_XONE = 'GFXOBDLANDS3'
    FIFA = 'GF000000FIFA'
    MADDEN = 'GF0000MADDEN'
    POKEMON_SWORD_SHIELD = '045496596972'
    POKEMON_LETS_GO = '045496593940'
    POKEMON_SUN_MOON = 'GFPOKSUNMOON'


class Platform(Enum):
    XBOX = 'xbox'
    X360 = 'xbox_360'
    XONE = 'xbox_one'
    PS1 = 'playstation'
    PS2 = 'playstation_2'
    PS3 = 'playstation_3'
    PS4 = 'playstation_4'
    PSP = 'playstation_portable'
    PSVITA = 'playstation_vita'
    N64 = 'nintendo_64'
    NGAMECUBE = 'nintendo_gamecube'
    NWII = 'nintendo_wii'
    NWIIU = 'nintendo_wiiu'
    NSWITCH = 'nintendo_switch'
    NDS = 'nintendo_ds'
    NDSI = 'nintendo_dsi'
    N3DS = 'nintendo_3ds'
    STEAM = 'steam'
    ORIGIN = 'origin'
    UPLAY = 'uplay'
    GOG = 'gog'
    MOBILE = 'mobile'
    BATTLENET = 'battlenet'
    XLIVE = 'xbox_live'
    PSN = 'playstation_network'
    UNKNOWN = 'unknown'  # For PC platform, use UNKNOWN


class ShippingWithinDays(Enum):
    AUTO = 0
    ONE = 1
    TWO = 2
    THREE = 3


class ExpireInDays(Enum):
    SEVEN = 7
    FOURTEEN = 14
    THIRTY = 30


class EscrowStatus(Enum):
    START = 'start'  # Initial condition: seller has Steam item(s)
    RECEIVE_PENDING = 'receive_pending'  # Offer made to seller to get Steam item(s)
    RECEIVED = 'received'  # Gameflip has Steam item(s)
    LISTED = 'listed'  # Gameflip has created listings for Steam item(s)
    STEAM_ESCROW = 'steam_escrow'  # Steam item(s) is held by Steam in escrow
    TRADE_HOLD = 'trade_hold'  # Gameflip has item(s) but there is a trade hold on them (e.g., Just Survive)
    DELIVER_PENDING = "deliver_pending"  # Escrow status: Offer made to buyer, but not accepted yet
    DELIVERED = "delivered"  # Escrow status: Buyer has item (terminal state)
    RETURN_PENDING = "return_pending"  # Escrow status: Trade offer made to seller to return item, but not accepted yet
    RETURNED = "returned"  # Escrow status: Seller has accepted return of item


class ListingStatus(Enum):
    DRAFT = "draft"  # Listing is draft/editing mode. You cannot list it when it's in this mode
    READY = "ready"  # Listing is ready to be listed, required fields have been filled
    ONSALE = "onsale"  # Listing is published to the public
    SALE_PENDING = "sale_pending"  # A buyer just bought the listing, and payment is being processed
    SOLD = "sold"  # A buyer had bought the listing


class ListingPhotoStatus(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    DELETED = "deleted"


class ListingOps(Enum):
    TEST = "test"
    ADD = "add"
    REPLACE = "replace"
    REMOVE = "remove"


class ExchangeStatus(Enum):
    PENDING = "pending"  # Exchange is being created
    PENDING_CANCEL = "pending_cancel"  # Exchange is being canceled
    PENDING_RESCINDING = "pending_rescinding"  # Exchange is being refunded
    SETTLED = "settled"  # Exchange has payment settled (verified and approved)
    RECEIVED = "received"  # Buyer has received the item
    PENDING_COMPLETION = "pending_completion"  # Exchange is being completed, happens after seller rates
    COMPLETE = "complete"  # Exchange completes, both buyer and seller have rated each other
    CANCELLED = "cancelled"  # Exchange has been cancelled, and payment authorization (if any) is also cancelled
    RESCINDED = "rescinded"  # Exchange has been cancelled with refund completed


class AcceptCurrency(Enum):
    USD = "USD"
    FLP = "FLP"
    BOTH = "BOTH"


# Steam APP IDs and Context IDs can be defined in a similar manner if needed.
class SteamAppID(Enum):
    CSGO = '730'  # CS:GO
    TF2 = '440'  # Team Fortress 2
    DOTA2 = '570'  # DOTA 2
    RUST = '252490'  # Rust
    PUBG = '578080'  # PlayerUnknown's Battlegrounds
    H1Z1_KOK = '433850'  # H1Z1: King of the Kill
    JUST_SURVIVE = '295110'  # H1Z1: Just Survive


class SteamContextID(Enum):
    CONTEXT_ID_433850 = '1'  # H1Z1: King of the Kill
    CONTEXT_ID_295110 = '1'  # Just Survive
    CONTEXT_ID_DEFAULT = '2'  # Default if not specified above