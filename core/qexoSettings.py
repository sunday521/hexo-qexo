import json
import random

QEXO_VERSION = "2.4.1"

DEFAULT_EMOJI = {"ๅพฎ็ฌ": "๐", "ๆๅด": "๐ฆ", "่ฒ": "๐", "ๅๅ": "๐", "ๅพๆ": "๐",
                 "ๆตๆณช": "๐ญ", "ๅฎณ็พ": "๐", "้ญๅด": "๐ท", "็ก": "๐ด",
                 "ๅคงๅญ ": "๐ก", "ๅฐดๅฐฌ": "๐ก", "ๅๆ": "๐", "่ฐ็ฎ": "๐", "ๅฒ็": "๐ฏ",
                 "ๆ่ฎถ": "๐", "้พ่ฟ": "๐", "้ท": "๐จ", "ๅทๆฑ": "๐ฑ", "ๆ็": "๐ต", "ๅ ": "๐",
                 "ๅท็ฌ": "โบ", "ๆๅฟซ": "๐", "็ฝ็ผ": "๐", "ๅฒๆข": "๐", "้ฅฅ้ฅฟ": "๐ช", "ๅฐ": "๐ซ",
                 "ๆๆ": "๐", "ๆตๆฑ": "๐", "ๆจ็ฌ": "๐", "ๆ ้ฒ ": "๐", "ๅฅๆ": "๐",
                 "ๅ้ช": "๐", "็้ฎ": "๐", "ๅ": "๐ต", "ๆ": "๐", "็ฏไบ": "๐", "่กฐ": "๐",
                 "้ชท้ซ": "๐", "ๆฒๆ": "๐ฌ", "ๅ่ง ": "๐", "ๆฆๆฑ": "๐", "ๆ ้ผป": "๐",
                 "้ผๆ": "๐", "็ณๅคงไบ": "๐", "ๅ็ฌ": "๐", "ๅทฆๅผๅผ": "๐", "ๅณๅผๅผ": "๐",
                 "ๅๆฌ ": "๐", "้่ง": "๐", "ๅงๅฑ ": "๐", "ๅฟซๅญไบ": "๐", "้ด้ฉ": "๐",
                 "ไบฒไบฒ": "๐", "ๅ": "๐", "ๅฏๆ": "๐", "่ๅ": "๐ช", "่ฅฟ็": "๐", "ๅค้": "๐บ",
                 "็ฏฎ็": "๐", "ไนไน ": "โช", "ๅๅก": "โ", "้ฅญ": "๐", "็ชๅคด": "๐ท", "็ซ็ฐ": "๐น",
                 "ๅ่ฐข": "๐น", "ๅดๅ": "๐", "็ฑๅฟ": "๐", "ๅฟ็ข": "๐", "่็ณ": "๐", "้ช็ต ": "โก",
                 "็ธๅผน": "๐ฃ", "ๅ": "๐ก", "่ถณ็": "โฝ", "็ข่ซ": "๐", "ไพฟไพฟ": "๐ฉ", "ๆไบฎ": "๐",
                 "ๅคช้ณ": "โ", "็คผ็ฉ": "๐", "ๆฅๆฑ": "๐ค", "ๅผบ ": "๐", "ๅผฑ": "๐", "ๆกๆ": "๐",
                 "่ๅฉ": "โ", "ๆฑๆณ": "โ", "ๅพๅผ": "โ", "ๆณๅคด": "โ", "ๅทฎๅฒ": "โ", "็ฑไฝ ": "โ",
                 "NO": "โ", "OK": "๐", "ๅฟๅ": "๐", "ๆ่ธ": "๐", "ๅฅธ็ฌ": "๐", "ๆบๆบ": "๐",
                 "็ฑ็": "๐", "่ถ": "๐", "ๅ็": "๐", "ๅ ๆฒน": "๐", "ๆฑ": "๐", "ๅคฉๅ": "๐",
                 "็คพไผ็คพไผ": "๐", "ๆบๆด": "๐", "ๅฅฝ็": "๐", "ๅ": "๐"}

DEFAULT_CDN = [
    {"name": "Cloudflare", "url": "https://cdnjs.cloudflare.com/ajax/libs/"},
    {"name": "Loli", "url": "https://cdnjs.loli.net/ajax/libs/"},
    {"name": "ไธ็ไบ", "url": "https://cdn.staticfile.org/"},
    {"name": "75CDN", "url": "https://lib.baomitu.com/"},
    {"name": "BootCDN", "url": "https://cdn.bootcdn.net/ajax/libs/"},
    # {"name": "้ๅบ้ฎ็ตๅคงๅญฆ", "url": "https://mirrors.cqupt.edu.cn/cdnjs/ajax/libs/"},  # ๆดๆฐไธๅๆถ
    {"name": "ๅๆน็งๆๅคงๅญฆ", "url": "https://mirrors.sustech.edu.cn/cdnjs/ajax/libs/"}
]

DEFAULT_UPDATES = [
    {"name": "master", "url": "https://github.com/Qexo/Qexo/tarball/master/"},
    {"name": "dev", "url": "https://github.com/Qexo/Qexo/tarball/dev/"}
]

ALL_SETTINGS = [  # [ๅ็งฐ, ้ป่ฎคๅผ, ๆฏๅฆๅจๅฐ่ฏไฟฎๅคๆถ้็ฝฎ, ็ฎไป]
    ["ABBRLINK_ALG", "crc16", False, "็ญ้พๆฅ็ฎๆณ"],
    ["ABBRLINK_REP", "dec", False, "็ญ้พๆฅๆ ผๅผdec/hex"],
    ["CDN_PREV", "https://unpkg.com/", True, "่ฐ็จNPM็CDNๅ็ผ"],
    ["CDNJS", "https://cdn.staticfile.org/", True, "่ฐ็จCDNJS็CDNๅ็ผ"],
    ["INIT", "2", False, "ๅๅงๅๆ ่ฏ"],
    ["QEXO_ICON", "https://unpkg.com/qexo-static@1.4.0/assets/img/brand/favicon.ico", False, "็ซ็นICON"],
    ["QEXO_LOGO", "https://unpkg.com/qexo-static@1.4.0/assets/img/brand/qexo.png", False, "็ซ็นLOGO"],
    ["QEXO_NAME", "Hexo็ฎก็้ขๆฟ", False, "็ซ็นๅ"],
    ["QEXO_SPLIT", "-", False, "็ซ็นๅ้็ฌฆ"],
    ["VDITOR_EMOJI", json.dumps(DEFAULT_EMOJI), True, "่ชๅฎไน่กจๆ"],
    ["WEBHOOK_APIKEY", ''.join(random.choice("qwertyuiopasdfghjklzxcvbnm1234567890") for x in range(12)), False, "APIๅฏ้ฅ"],
    ["VERCEL_TOKEN", "", False, "Vercelๅฏ้ฅ"],
    ["PROJECT_ID", "", False, "Qexo้กน็ฎID"],
    ["ALLOW_FRIEND", "ๅฆ", False, "ๆฏๅฆๅ่ฎธๅ้พ็ณ่ฏท ๆฏ/ๅฆ"],
    ["LAST_LOGIN", "", True, "ๅไธปๆๅไธ็บฟๆถ้ด(ๆ ้ๆดๆน)"],
    ["IMG_HOST", "{\"type\":\"ๅณ้ญ\",\"params\":{}}", False, "2.0ไนๅ็ๅพๅบ่ฎพ็ฝฎJSON"],
    ["ONEPUSH", "", False, "OnePushๆถๆฏ้็ฅ"],
    ["PROVIDER", "", False, "2.0ไนๅ็ๅนณๅฐJSON"],
    ["STATISTIC_ALLOW", "ๅฆ", False, "ๆฏๅฆๅผๅฏ็ป่ฎกๅ่ฝ ๆฏ/ๅฆ"],
    ["STATISTIC_DOMAINS", "", False, "็ป่ฎกๅฎๅจๅๅ ่ฑๆๅ่ง้ๅท้ด้"],
    ["FRIEND_RECAPTCHA", "ๅฆ", False, "ๅฏ็จๅ้พ้ช่ฏ็ reCaptcha ๅณ้ญ/v2/v3"],
    ["RECAPTCHA_TOKEN", "", False, "็จไบๅ้พreCaptchaๆๅกๅจ็ซฏๅฏ้ฅ"],
    ["LOGIN_RECAPTCHA_SITE_TOKEN", "", False, "็จไบ็ปๅฝ้ช่ฏ็reCaptchaV3็ฝ็ซๅฏ้ฅ"],
    ["LOGIN_RECAPTCHA_SERVER_TOKEN", "", False, "็จไบ็ปๅฝ้ช่ฏ็reCaptchaV3ๆๅก็ซฏๅฏ้ฅ"],
    ["POST_SIDEBAR",
     "[{\"search\":\"title\",\"name\":\"ๆ ้ข\",\"icon\":\"fas fa-heading\"},{\"search\":\"abbrlink\",\"name\":\"็ผฉๅ\",\"icon\":\"fas fa-id-card\"},{\"search\":\"date\",\"name\":\"ๅๅธไบ\",\"icon\":\"fas fa-globe-americas\"},{\"search\":\"updated\",\"name\":\"ๆดๆฐไบ\",\"icon\":\"fas fa-calendar-alt\"},{\"search\":\"tags\",\"name\":\"ๆ ็ญพ\",\"icon\":\"fas fa-tags\"},{\"search\":\"categories\",\"name\":\"ๅ็ฑป\",\"icon\":\"fas fa-folder-open\"}]",
     False, "ๆ็ซ ไพง่พนๆ ้็ฝฎJSON"],
    ["PAGE_SIDEBAR",
     "[{\"search\":\"title\",\"name\":\"ๆ ้ข\",\"icon\":\"fas fa-heading\"},{\"search\":\"date\",\"name\":\"ๅๅธไบ\",\"icon\":\"fas fa-globe-americas\"},{\"search\":\"updated\",\"name\":\"ๆดๆฐไบ\",\"icon\":\"fas fa-calendar-alt\"}]",
     False, "้กต้ขไพง่พนๆ ้็ฝฎJSON"],
    ["EXCERPT_POST", "ๅฆ", False, "ๆฏๅฆๅผๅฏๅจๆๅฝไธบ็ฉบๆถ่ชๅจๆชๅๆ็ซ  ๆฏ/ๅฆ"],
    ["EXCERPT_LENGTH", "200", False, "่ชๅจๆชๅๆ็ซ ็้ฟๅบฆ"],
    ["ALL_CDN", json.dumps(DEFAULT_CDN), True, "CDNๅ่กจ"],
    ["ALL_UPDATES", json.dumps(DEFAULT_UPDATES), True, "ๆดๆฐๆบๅ่กจ"],
    ["UPDATE_FROM", "false", False, "ๆฏๅฆๆดๆฐ่ฟ"],
    ["JUMP_UPDATE", "false", False, "ๆฏๅฆ่ฝฌ่ทณๅฐๆดๆฐ็้ข"],
]
