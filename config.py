from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "23854524"))
API_HASH = getenv("API_HASH", "e765ba734e8c485b1b1f72dff94127de")

BOT_TOKEN = getenv("BOT_TOKEN", "6152203566:AAEWiQZIsvs5iA8LtKblIaqdac_u_1VF4xk")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID" "5988263194"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/27daf8d1526bc272fb8e8.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/189eab157cabed2cb5b85.jpg")

SESSION = getenv("SESSION", "BQDGWGUmJtcR58x-UYJTUTTobMZ0JxFneRFpqJ6GEI4YjbLKJPequSc2AAxQTutsRBEpeSeNK3uhsKY2GCaQ5B_RTVs6TDnIZ3s-a_lk4EJwoYrfkhIXqxMb9TBeZYNTWVp8-1Wm2NTo4TIVV9cBCMUw_ANbH7AzESBtaFS4CqLs_1Or_0DHbzn4gEqowzutrbSFsbs39UgaCRP7FKxZjCN0_FypHevvHCI8-R2uPdNlcE-Qwg52scSgne5v-kSpJjOVxnfGyl7alYgrWi5nVUR28uqtYMERqPOzKf1m5MO8NPG893fDRoKIEoW0fypvBlhRt5YGw7KyiaAtyuYHXScfAAAAAU3end8A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ISHQ00_I")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/XD_CUTETY")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5322208820").split()))


FAILED = "https://telegra.ph/file/cf09262a180b976603ecf.jpg"
