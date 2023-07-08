import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool


load_dotenv(".env")


API_ID = int(getenv("API_ID", "28094601")) #optional
API_HASH = getenv("API_HASH", "70756c6b7f3bf1d996ab7d157b270970") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1715348447").split()))
DEEP_AI = getenv("DEEP_AI", "d7394561-0528-4714-a1ee-edd7020b48e1")
OWNER_ID = int(getenv("OWNER_ID") or 6080624164)
ADMIN1_ID = list(map(int, getenv("ADMIN1_ID", "6080624164").split()))
ADMIN2_ID = list(map(int, getenv("ADMIN2_ID", "1715348447").split()))
ADMIN3_ID = list(map(int, getenv("ADMIN2_ID", "5633133204").split()))
ADMIN4_ID = list(map(int, getenv("ADMIN2_ID", "5657257558").split()))


ADMIN1_ID.append(6080624164)
ADMIN2_ID.append(1715348447)
ADMIN3_ID.append(5633133204)
ADMIN4_ID.append(5657257558)

MONGO_URL = getenv("MONGO_URL", "mongodb+srv://claypronek:Malik10_@cluster0.xtwc7.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6050133470:AAEj0R_Y0EUfsLLb8gYClqpaf5oYuZsIhyg")
BOT_WORKERS = int(getenv("BOT_WORKERS", "1"))
USER_WORKERS = int(getenv("BOT_WORKERS", "8"))
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT", "Malik Anak Ganteng... ututututu")
PM_LOGGER = getenv("PM_LOGGER", None)
OPENAI_API = getenv("OPENAI_API", "")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "-1001566281443").split()}
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "Fairy") #don't change
REPO_URL = getenv("REPO_URL", "https://github.com/Malik22222/Cuan")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SUPPORT = int(getenv("SUPPORT", "-1001528080636"))
CHANNEL = int(getenv("CHANNEL", "-1001841693247"))
SESSION1 = getenv("SESSION1", "AQAhIHQAeQnv4G5m2oaXpj9ghuTDVuJAHRWLvc7f000skvbCAT4ZuqPzqavMCh3FIRq8zRBbBYcLRGWPk2EFbztcVdQf6eH5uTrsOI0R7vmmPl6G-hMo3faSxZ1gHdm0joeMnXBaG5zshNdueM-9waD9v1XxGgLM4CkO3-LIMCHL2O9AtlZc3PdZgYKyBqSfg7bBJqes-FMkBk0TpnLWPC5YbK9JEy2CvqsM4dWaqTn2I4muMdL4Hcikw4bH8FQu_utbef3oX0MBRhXTn3wEAxAWF2Q_03b9Shr2CRVovQ9X2PTPb2hH3yRCVUAlxvoBZFW7hj5CLJtSirmsu69LO3Bd3dM6LwAAAAFqbvYkAA")
SESSION2 = getenv("SESSION2", "BQAhIHQANMCuCfExEZrDIluP3_q-DpTJrm64pObOCRljXdixqnKuC64wtLqkjQ3ms1hkKAt5-1FVisdvBvUDfmFVvRi5xnt7VI-qpCpoQtNRumF19lD-u552vwKZZwFmWB59v9BukS9c0avDHFocDiwGU0fCwm4JbVfAbRe_CDuLXBy-SIvGjCzMoBwRf0ogEwSTw2OFbtRMYupQm6KppEw-dWiZpsRlCYYdUqZRwTT5tXuHXxIy2av57qcpBqCmLXFsfaKtKUSTCeB9m_UEZAy0Pj_h1vmJpoDCP7cp9-rHjN1-6K75aAsvUuY3osRxrHEfvIUp_2-Wkxcoq7ykcdbYj2TLNAAAAABpyqBnAA")
SESSION3 = getenv("SESSION3", "AQAhIHQAhuPqb4PMWGXi94eHFnMbr7xPpajrYkVftgNZxY6VFQt0cAgtdC6LK555RfxsdshK-lQgBBgZATogxGTAEdzZt2IEkmIJTY5HwFEokWRvV0fCFzHbiWOa1kWYlhuNljiA8V8eLPAqTUUxEtwtub3ddadsQOUgY9yJ7vc-1gvGtamKijCWfbumqIuQHWYxj8vqj4QvMSizQi-uWvIfHOE67EafuwBy7pSyPUTRVBmdifB9m_fhvheNOXsALwr1ZaA6rLIxqiGqBaMw0lsXdRMMh-4t9erRtwX4lC-dLRtVpgR2d-dkUqqvxKucqHb38eOQEBVx3a2KxrMzcCyQvsLiVwAAAAFyZ2h-AA")
SESSION4 = getenv("SESSION4", "AQAhIHQAB-b_uVMkyQ_wLuJkb0uOJv7bd4nWu99DfOQh_RkIoZgQjRurXcfebaP5dmBZQ2NP6k9bdqXrATrYyfzTuyWYFTb-lp_rVDND1bzyDaVO2x4677tzv3WK6h3ZSJIcr4oA8IMECYUEJvkkQMaMX6luCtQLhQ-xCNfjj3v4rtZ1T2t9u0kceIS3wD8CyvDKlbV4FQm4mJojsoSxbbpF6ucoi-7DIQmeppYevbdfpG8GpdBGkX9jKxByG_jwNFOfWx7UPiE80H6LbW96DRhiK1pHdFoZMZBe9URO0a4TS6fa4J3gdMeuMPEE4tbKzBnocdN990mnV6soo8b5FH1DnHkEHQAAAAFPwsqUAA")
SESSION5 = getenv("SESSION5", "BQAhIHQAF6xxmf7ss5Ulc12JN0XJZIHHAqp9VzirlenPUuABGtKKiA1K4QDBBhef_gU9L3kLhAPwKw4OF5jPFz8Xd_5W-m_I4W10JYYZfFDNAlNhtbIupvci7OMLb0CGVIyc21UamlSzUR0h3ej3SV2CGtrZgYkLdcY7eBP8wDDc4-9mkNXfMjk9FMWPJFRdX2dN1j1V0p01zErgCTuulQPlyR2VY8y-Jm6dZKgNlZwbGhv-Uda63uE6o75d6LJlrd0XSG3xkZ4tnDIEtXE4iM5X1I4iWTJ55A7tmjnsAx3VPFeZ0FuCc6MnaSLYe7JfUg4kbvK_GUzj_6IlxN2fxQXCv4JOpQAAAABMgA6fAA")
SESSION6 = getenv("SESSION6", "BQAhIHQAPqYYUT-Mazx4Y23uT4e-1XE0vATGPuVvP2-U6usi4FN17dC-FbLOo0aho2qpv67Ud5A3Cf-otcpI97-JIUMYVWa-nL2VgpDzSZSYC3Ksy3f0TVPzdhUt2sFwVkWce6SSp2pPYsgoxAzmV7Kz_Wt-s-XpyznrAMdw6kqw1jy32414ws-lHlb4TGDHqkfA9eJhNUAEbvpfF8t_IQ6tLoYFZbvktGmgblYFU-YNgRlPTEcXs5t3XHiQwOnBYUvVBU0-lbyHCaCG8pUwRn8Ym70qt_5_zCfBQvhXeHGqZWsqFq6Lx0wRudEO48yQUXlxQMF0PFptZOZthGPPHAN6nqhFvAAAAABGZ2YHAA")
SESSION7 = getenv("SESSION7", "BQAhIHQAUGkkGdaw4LZ0f9Zg7atXjJSSyFTefiCqkJ3E06-IUidTyny1pntdjg-amMIS0ODZ6aj2ALJ7l0R2g26i690jel9kxV2y8WXzfWE04AQ05QgESzgsPFhEo5SXF3ebr-VQf6VejHWzTiCoQrrfV5GKhSdzis0TGKTMc3xU3B4rOu84x5YBQlfM-Xb5ChoWybFQJdGKyWCzVQj1M6wmGuuZp5ofAEJU4V3rJtM480s8kNEQfwIS02nqubrIYmr-31zIi6flqzUDZuLQ_3go1qce2p-xCm-29Pc2ZLRFJhOcB2VUIKOuwJm5KwcMpu-i2eyuOuJ1sBW9lblyXFyl4bVquAAAAABRh1JLAA")
SESSION8 = getenv("SESSION8", "AQAhIHQAvxAfR47Ffp8peDEujfmtL95ioaHuwJZOpe6z6NmyLfdXaBaTmDuCu2j8P05Xcbgrc7QgsL72kchMSTgTTNVaEF5-_wJfgLnrte_khvlipIVrEWcp2PKeUySsqbTA_EPEHD7nwg5hhKQZ13TiaxnFkYeflBeYQyPF7swZPrXAFO9h3ibHWotdc1swCWE-uIevF6rQXGUC5R1NEBdhXcOyBBJgYdwXYJfPUYU9ccNJbgWk-KsEiyUYzd0fgbuldMzuox_DsAXphaRvWrm2KTW4W7wlVmsXUFvwlJOYD59Vg1t2NKcbrQO-jEk4PUyzrXin3stuBYB4QnwO8xEByF35rAAAAAFvpr8pAA")
SESSION9 = getenv("SESSION9", "AQAhIHQAMjuJ_92gf60uAYDQXMg7ktCzK-p0X-mLh9r8xRbIEaC2fo-WcCXRof7FyoLPWXbMm37tHwCNANTVEOyTF0hdCQnNJimEu4W9GpoXXxaxQWCPkfFBIVMzwnOBLhrdSsqD6ioivI-H39tOub3LESF5ef7R1d0Ziu-9Fd6FtXLyHXJb4nvnbquB1V8EJUGdx5sxcPvbQLVFIKO6eeCCkhhELwFl5bPmsDaX4A3i0Gc6uhSLaJ8dvLfIiHvembbDgZDWwJL5q_OcDYJEYXWLtcexlJXy0sQgNjcbKXxpFt5E2KwmmI32ymYyXhGpyKH9oMwVaBL_xi8Eg0rZf2uOkwDEdAAAAAFwqD9lAA")
SESSION10 = getenv("SESSION10", "")
SESSION11 = getenv("SESSION11", "")
SESSION12 = getenv("SESSION12", "")
SESSION13 = getenv("SESSION13", "")
SESSION14 = getenv("SESSION14", "")
SESSION15 = getenv("SESSION15", "")
SESSION16 = getenv("SESSION16", "")
SESSION17 = getenv("SESSION17", "")
SESSION18 = getenv("SESSION18", "")
SESSION19 = getenv("SESSION19", "")
SESSION20 = getenv("SESSION20", "")
SESSION21 = getenv("SESSION21", "")
SESSION22 = getenv("SESSION22", "")
SESSION23 = getenv("SESSION23", "")
SESSION24 = getenv("SESSION24", "")
SESSION25 = getenv("SESSION25", "")
SESSION26 = getenv("SESSION26", "")
SESSION27 = getenv("SESSION27", "")
SESSION28 = getenv("SESSION28", "")
SESSION29 = getenv("SESSION29", "")
SESSION30 = getenv("SESSION30", "")
SESSION31 = getenv("SESSION31", "")
SESSION32 = getenv("SESSION32", "")
SESSION33 = getenv("SESSION33", "")
SESSION34 = getenv("SESSION34", "")
SESSION35 = getenv("SESSION35", "")
