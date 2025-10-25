from enum import Enum

class ShippingPaidBy(str, Enum):
    BUYER = "buyer"
    SELLER = "seller"


class Category(str, Enum):
    GAMES = 'CONSOLE_VIDEO_GAMES'  # Video games, digital or physical
    INGAME = 'DIGITAL_INGAME'  # In-game items, digital only
    GIFTCARD = 'GIFTCARD'  # Gift cards, digital or physical
    CONSOLE = 'VIDEO_GAME_HARDWARE'  # Console game hardware, physical listing only
    ACCESSORIES = 'VIDEO_GAME_ACCESSORIES'  # Console game accessories, physical listing only
    TOYS = 'TOYS_AND_GAMES'  # Collectibles, physical listing only
    VIDEO = 'VIDEO_DVD'  # Movies, physical or digital
    OTHER = 'UNKNOWN'  # Unsupported category


class Kind(str, Enum):
    ITEM = 'item'  # Item selling
    GIG = 'gig'  # Gig selling


class UPC(str, Enum):
    ANIMAL_CROSSING_NH = "045496596439"
    BORDERLANDS3_PC = "GFPCBDLANDS3"
    BORDERLANDS3_PS4 = "GFPSBDLANDS3"
    BORDERLANDS3_XONE = "GFXOBDLANDS3"
    BRAWLHALLA = "045496663285"
    BRAWL_STARS = "GFBRAWLSTARS"
    CLASH_OF_CLANS = "GFCLASHOCLAN"
    CLASH_ROYALE = "GFCLASHROYAL"
    COD_BLOPS6 = "7340f6b6-3a5a-4737-9033-237b9fb522ca"
    COD_MWII = "GF0000CODMW2"
    COD_MWIII = "GF0000CODMW3"
    COD_WZ = "GF00000CODWZ"
    CS2 = "094922417596"
    DARK_AND_DARKER = "GF00DADARKER"
    DARK_SOULS_3 = "GFDARKSOULS3"
    DCU_ONLINE = "GF000000DCUO"
    DEAD_BY_DAYLIGHT = "GFDBDAYLIGHT"
    DIABLO_4 = "GF000DIABLO4"
    DOTA2 = "111111111111"
    DRAGONS_DOGMA_2 = "GFDRAGONSDM2"
    DREAMLIGHT_VALLEY = "GFDREAMLIGHT"
    DYING_LIGHT_2_PS4 = "662248923314"
    DYING_LIGHT_2_PS5 = "662248924915"
    DYING_LIGHT_2_XONE = "662248923369"
    DYING_LIGHT_2_XSERIES = "662248924823"
    ELDEN_RING_PC = "GF000ERINGPC"
    ELDEN_RING_PS5 = "GF000ERINGPS"
    ELDEN_RING_XSERIES = "GF000ERINGXS"
    ENSHROUDED = "GFENSHROUDED"
    ESO_PC = "GF00000PCESO"
    ESO_PS5 = "GF00000PSESO"
    ESO_XSERIES = "GF00000XSESO"
    EVE_ONLINE = "GF0000000EVE"
    FALLOUT76_PC = "GFPCFLLOUT76"
    FALLOUT76_PS4 = "GFPSFLLOUT76"
    FALLOUT76_XONE = "GFXOFLLOUT76"
    FIFA = "GF000000FIFA"
    FORTNITE = "GFFORTNITE"
    GROWTOPIA = "GF0GROWTOPIA"
    GTA5_PC = "710425414534"
    GTA5_PS4 = "710425474521"
    GTA5_PS5 = "GF000GTA5PS5"
    GTA5_XONE = "710425494512"
    GTA5_XSERIES = "GF000GTA5XSX"
    HALO_INFINITE = "GF000HALOINF"
    HAY_DAY = "GF0000HAYDAY"
    LEAGUE_OF_LEGENDS = "GF0000000LOL"
    LORDS_OF_THE_FALLEN = "GFLORDFALLEN"
    MADDEN = "GF0000MADDEN"
    MONOPOLY_GO = "GFMONOPOLYGO"
    NO_MANS_SKY = "GF0NOMANSSKY"
    PATH_OF_EXILE = "GF000POEXILE"
    PATH_OF_EXILE_2 = "6ce9c6d3-c32d-4037-9554-3f1f9de866bd"
    POKEMON_DIAMOND_PEARL = "045496597894"
    POKEMON_LEGENDS_ARCEUS = "045496598044"
    POKEMON_SCARLET_VIOLET = "045496599058"
    POKEMON_SWORD_SHIELD = "045496596972"
    PUBG = "000000578080"
    PUBG_MOBILE = "GF00PUBGMOBI"
    RUNESCAPE = "GF0RUNESCAPE"
    RUST = "000000252490"
    RUST_CONSOLE = "GFRUSTCONSOL"
    SEA_OF_THIEVES = "GFSEATHIEVES"
    SKULL_BONES = "GFSKULLBONES"
    STATE_OF_DECAY_2 = "GF00SODECAY2"
    SWTOR = "GF00000SWTOR"
    TF2 = "014633098693"
    TINY_TINAS_WONDERLANDS = "GF00TTWONDER"
    WARFRAME_PC = "GFSTWARFRAME"
    WARFRAME_PS = "GFPSWARFRAME"
    WARFRAME_SWITCH = "GFSWWARFRAME"
    WARFRAME_XBOX = "GFXOWARFRAME"
    WORLD_OF_WARCRAFT = "GF000WOW0000"
    XDEFIANT = "GF00XDEFIANT"


class Platform(str, Enum):
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


class ShippingWithinDays(int, Enum):
    AUTO = 0
    ONE = 1
    TWO = 2
    THREE = 3


class ExpireInDays(int, Enum):
    SEVEN = 7
    FOURTEEN = 14
    THIRTY = 30


class EscrowStatus(str, Enum):
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


class ListingStatus(str, Enum):
    DRAFT = "draft"  # Listing is draft/editing mode. You cannot list it when it's in this mode
    READY = "ready"  # Listing is ready to be listed, required fields have been filled
    ONSALE = "onsale"  # Listing is published to the public
    SALE_PENDING = "sale_pending"  # A buyer just bought the listing, and payment is being processed
    SOLD = "sold"  # A buyer had bought the listing


class ListingPhotoStatus(str, Enum):
    PENDING = "pending"
    ACTIVE = "active"
    DELETED = "deleted"


class ListingOps(str, Enum):
    TEST = "test"
    ADD = "add"
    REPLACE = "replace"
    REMOVE = "remove"


class ExchangeStatus(str, Enum):
    PENDING = "pending"  # Exchange is being created
    PENDING_CANCEL = "pending_cancel"  # Exchange is being canceled
    PENDING_RESCINDING = "pending_rescinding"  # Exchange is being refunded
    SETTLED = "settled"  # Exchange has payment settled (verified and approved)
    RECEIVED = "received"  # Buyer has received the item
    PENDING_COMPLETION = "pending_completion"  # Exchange is being completed, happens after seller rates
    COMPLETE = "complete"  # Exchange completes, both buyer and seller have rated each other
    CANCELLED = "cancelled"  # Exchange has been cancelled, and payment authorization (if any) is also cancelled
    RESCINDED = "rescinded"  # Exchange has been cancelled with refund completed


class AcceptCurrency(str, Enum):
    USD = "USD"
    FLP = "FLP"
    BOTH = "BOTH"


# Steam APP IDs and Context IDs can be defined in a similar manner if needed.
class SteamAppID(str, Enum):
    CSGO = '730'  # CS:GO
    TF2 = '440'  # Team Fortress 2
    DOTA2 = '570'  # DOTA 2
    RUST = '252490'  # Rust
    PUBG = '578080'  # PlayerUnknown's Battlegrounds
    H1Z1_KOK = '433850'  # H1Z1: King of the Kill
    JUST_SURVIVE = '295110'  # H1Z1: Just Survive


class SteamContextID(str, Enum):
    CONTEXT_ID_433850 = '1'  # H1Z1: King of the Kill
    CONTEXT_ID_295110 = '1'  # Just Survive
    CONTEXT_ID_DEFAULT = '2'  # Default if not specified above


class Visibility(str, Enum):
    UNLISTED = 'unlisted'
    PUBLIC = 'public'