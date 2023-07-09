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
BOT_WORKERS = int(getenv("BOT_WORKERS", "2"))
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
SESSION1 = getenv("SESSION1", "BQAhIHQALwRIGakVYWr1ITyivjLButIE5dV68jY8XSsOpoF2ufGT6OHE6wTUBU54sUlJ61uJf3DFnPboBUvg1_ZmXIbTBqn7ZmlutBFyYu8uydEYN3JxAzsaAK7OproKdBWSEP9ZRDriPRQeho0jg6HZbLCEqjYh9zx0tIuntlbzMIKrr1CQ9ZLwdmXIcCnYLuI0ZNqBmgmRUcrsm7hCBvusoLuWIY8UrUM7G6XbW8BGecI_ynr-UakxaBlKXnqQDRoK7TAeFLhquqjVVWhYMDQbY7_22U7AvnRwlL16K0BK9Ad9rGRwVmZzamE0N90Xi2NfMIxlLmHAR8HGWuQHydwu3pExXAAAAAB_3XRvAA")
SESSION2 = getenv("SESSION2", "BQAhIHQAIqEt9iLnnuVSZ0klCr2WFernpb7tjhPSII8vDre7xxDlQBjFStMzFUlIyNBRukCgJjeV5Qc2u9AKGGTPGtlxw7D1sJgK4xXYJwmwmBpIsCnMocMjDYGHVC-25C48e1wKlmDa7yu6SS2vBQI-uJkDi_T7KpThVEolzJSnpJRWXnIFjnOGUNj0UPpiNbsG1rBpY3gifLgN0x1N81yr8_q8cdD9ptD4xvBMI_MZuHtnGPj95u_uk9NGFOdqdB_IjryuIC2SyM2SGWhmk1xa77bwKpd1X7g0KvIzY5KR2giD35z6e0gL8I8_EOf1C_rqci6Esx2WaMET6noBDLLOxQU6kQAAAAB00RupAA") 
SESSION3 = getenv("SESSION3", "BQAhIHQAJiJtV2Cv0iUr9ULbizlYm0sklVhV_4aLy0vynqdOQ4Db6a3EdOufbC9GhEMR5i7zHDSpmoXyXxVrqZ1sku_N0Hgk_n-XYmrup9_XhFSCenOJkadXuXVVEVYsJz8w2_mComLJ-3HfmG_jbjAdLxFsELqi1Zj-M1844R166siAhpdTvA0IfI0EsOOb1zIgQm4uqRCSnp90jURjIlLgqr9FDbhn_BZbzCvgQc22OkTlOFAvn_2Vqg04JHaMr4Lle3gPArwNboZBbhVQjWYlr5Smt_tLWWwddTkRFoA5Sc5HDu67V6qdM54b_1vZt3dQZTP00GaeuZJLjU_zSHN6Ch8D-gAAAABLyUKTAA")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
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
