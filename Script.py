
class script(object):
    HELP_TXT = """π·π΄π {}
π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π."""
    ABOUT_TXT = """<b>β― πΌπ π½π°πΌπ΄: {}</b>
β― π»πΈπ±ππ°ππ: πΏπππΎπΆππ°πΌ
β― π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ πΉ
β― π³π°ππ° π±π°ππ΄: πΌπΎπ½πΆπΎ π³π±
β― π±πΎπ ππ΄πππ΄π: vps
β― π±ππΈπ»π³ πππ°πππ: v4.0.6 [ π±π΄ππ° ]""" 
    SOURCE_TXT = """<b>NOTE:</b>
- Not Open Source Project 
  Contact to bot owner"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- movies house Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. movies house supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/xxxxxxx_xxxx)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of movies house bot

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specified user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """β ππΎππ°π» π΅πΈπ»π΄π: <code>{}</code>
β <b>ππΎππ°π» πππ΄ππ: <code>{}</code>
β ππΎππ°π» π²π·π°ππ: <code>{}</code>
β πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
β π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±"""
    LOG_TEXT_G = """#NewGroup
Group = {}, {}.
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    START_TXT = """<b>Κα΄Κ {}..

Ιͺα΄ β‘οΈ α΄α΄α΄‘α΄Κ?α΄Κ α΄α΄α΄α΄-?ΙͺΚα΄α΄Κ Κα΄α΄...
π Κα΄α΄ α΄α΄Ι΄ α΄sα΄ α΄α΄ α΄s α΄ α΄α΄α΄α΄-?ΙͺΚα΄α΄Κ ΙͺΙ΄ Κα΄α΄Κ Ι’Κα΄α΄α΄ ....
Ιͺα΄s α΄α΄sΚ α΄α΄ α΄sα΄ α΄α΄: α΄α΄sα΄ α΄α΄α΄ α΄α΄ α΄α΄ Κα΄α΄Κ Ι’Κα΄α΄α΄ α΄s α΄α΄α΄ΙͺΙ΄, α΄Κα΄α΄s α΄ΚΚ, Ιͺ α΄‘ΙͺΚΚ α΄Κα΄α΄ Ιͺα΄α΄ α΄α΄α΄ Ιͺα΄s α΄Κα΄Κα΄...π

β οΈ α΄α΄Κα΄ Κα΄Κα΄ α΄Κα΄α΄α΄ Κα΄Κα΄ Κα΄α΄α΄α΄Ι΄..</b>"""

    MALIK_TXT =  """<b>Donation</b>

<b>Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive...</b>


βͺΌ <b>ππ¨π? πππ§ ππ¨π§ππ­π ππ§π² ππ¦π¨π?π§π­ ππ¨π? πππ―π π³. 

<b>βββββββββα Payment Methods αβββββββββ

β? ππΌπΌπ΄πΉπ²π£π?π
β? π£π?πππΊ           
β? π£π΅πΌπ»π²π£π²     
β? π£π?ππ£π?πΉ

_ππ¨π§π­πππ­ ππ ππ¨π« ππ§π¨π° πππ¨π?π­ ππ‘π πππ²π¦ππ§π­ ππ§ππ¨_
ββββββββββββα <a href=https://t.me/Akshay_Chand4><b>Akshay chand</b></a> αββββββββββββ"""
    DINETTE_TXT =  """<b>Donation</b>


<b>Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive...</b>


βͺΌ <b>ππ¨π? πππ§ ππ¨π§ππ­π ππ§π² ππ¦π¨π?π§π­ ππ¨π? πππ―π π³. 

<b>βββββββββα Payment Methods αβββββββββ

β? ππΌπΌπ΄πΉπ²π£π?π
β? π£π?πππΊ           
β? π£π΅πΌπ»π²π£π²     
β? π£π?ππ£π?πΉ

_ππ¨π§π­πππ­ ππ ππ¨π« ππ§π¨π° πππ¨π?π­ ππ‘π πππ²π¦ππ§π­ ππ§ππ¨_
ββββββββββββα <a href=https://t.me/Akshay_Chand4><b>Akshay Chand</b></a> αββββββββββββ"""
    VIDEO_TXT ="""<b>π·π΄π»πΏ ππΎπ ππΎ π³πΎππ½π»πΎπ°π³ ππΈπ³π΄πΎ π΅ππΎπΌ ππΎππππ±π΄.

β’ ππ΄π’π¨π¦
π π°πΆ ππ’π― ππ°πΈπ―π­π°π’π₯ ππ―πΊ ππͺπ₯π¦π° ππ³π°π? π π°πΆπ΅πΆπ£π¦

ππ€π¬ ππ€ ππ¨π
β’ ππΊπ±π¦ /video or /mp4 ππ―π₯ (ππͺπ₯π¦π° Link)
β’ ππΉπ’π?π±π­π¦:
/π?π±4 https://youtu.be/Your Link<\b>"""

    VIDEOS_TXT ="""<b>π·π΄π»πΏ ππΎπ ππΎ π³πΎππ½π»πΎπ°π³ ππΈπ³π΄πΎ π΅ππΎπΌ ππΎππππ±π΄.

β’ ππ΄π’π¨π¦
π π°πΆ ππ’π― ππ°πΈπ―π­π°π’π₯ ππ―πΊ ππͺπ₯π¦π° ππ³π°π? π π°πΆπ΅πΆπ£π¦

ππ€π¬ ππ€ ππ¨π
β’ ππΊπ±π¦ /video or /mp4 ππ―π₯ (ππͺπ₯π¦π° Link)
β’ ππΉπ’π?π±π­π¦:
/π?π±4 https://youtu.be/Your Link<\b>"""

    YTTHUMB_TXT = """<b>π·π΄π»πΏπ ππΎ π³πΎππ½π»πΎπ°π³ π°π½π ππΎππππ±π΄ ππΈπ³π΄πΎ ππ·ππΌπ±π½π°πΈπ»
    
β­ππ€π¬ ππ€ ππ¨π
ππΊπ±π¦ /ytthumb ππ―π₯ ππͺπ₯π¦π° ππͺπ―π¬

β’ ππΉπ’π?π±π­π¦
/ytthumb https://youtu.be/yourlink</b>"""

    FORCESUB_TXT = """β οΈ Join our updated channel below.  bot will not give you movie until you join from our update channel...

β οΈ ΰ?ΰ―ΰ?΄ΰ― ΰ?ΰ?³ΰ―ΰ?³ ΰ?ΰ?ΰ―ΰ?ΰ?³ΰ― ΰ?ͺΰ―ΰ?€ΰ―ΰ?ͺΰ―ΰ?ͺΰ?Ώΰ?ΰ―ΰ?ΰ?ͺΰ―ΰ?ͺΰ?ΰ―ΰ? ΰ?ΰ―ΰ?©ΰ?²ΰ?Ώΰ?²ΰ― ΰ?ΰ―ΰ?°ΰ?΅ΰ―ΰ??ΰ―.  ΰ?ΰ?ΰ―ΰ?ΰ?³ΰ― ΰ?ͺΰ―ΰ?€ΰ―ΰ?ͺΰ―ΰ?ͺΰ?Ώΰ?ͺΰ―ΰ?ͺΰ― ΰ?ΰ―ΰ?©ΰ?²ΰ?Ώΰ?²ΰ― ΰ?¨ΰ―ΰ?ΰ―ΰ?ΰ?³ΰ― ΰ?ΰ―ΰ?°ΰ―ΰ??ΰ― ΰ?΅ΰ?°ΰ― ΰ?ͺΰ―ΰ?ΰ― ΰ?ΰ?ΰ―ΰ?ΰ?³ΰ―ΰ?ΰ―ΰ?ΰ― ΰ?€ΰ?Ώΰ?°ΰ―ΰ?ͺΰ―ΰ?ͺΰ?ΰ?€ΰ―ΰ?€ΰ― ΰ?΅ΰ?΄ΰ?ΰ―ΰ?ΰ?Ύΰ?€ΰ―... 

β οΈ ΰ¨Ήΰ©ΰ¨ ΰ¨Ύΰ¨ ΰ¨Έΰ¨Ύΰ¨‘ΰ© ΰ¨ΰ¨ͺΰ¨‘ΰ©ΰ¨ ΰ¨ΰ©ΰ¨€ΰ© ΰ¨ΰ©ΰ¨¨ΰ¨² ΰ¨΅ΰ¨Ώΰ©±ΰ¨ ΰ¨Έΰ¨Όΰ¨Ύΰ¨?ΰ¨² ΰ¨Ήΰ©ΰ¨΅ΰ©ΰ₯€  ΰ¨¬ΰ©ΰ¨ ΰ¨€ΰ©ΰ¨Ήΰ¨Ύΰ¨¨ΰ©ΰ©° ΰ¨ΰ¨¦ΰ©ΰ¨ ΰ¨€ΰ©±ΰ¨ ΰ¨?ΰ©ΰ¨΅ΰ© ΰ¨¨ΰ¨Ήΰ©ΰ¨ ΰ¨¦ΰ©ΰ¨΅ΰ©ΰ¨ΰ¨Ύ ΰ¨ΰ¨¦ΰ©ΰ¨ ΰ¨€ΰ©±ΰ¨ ΰ¨€ΰ©ΰ¨Έΰ©ΰ¨ ΰ¨Έΰ¨Ύΰ¨‘ΰ© ΰ¨ΰ¨ͺΰ¨‘ΰ©ΰ¨ ΰ¨ΰ©ΰ¨¨ΰ¨² ΰ¨€ΰ©ΰ¨ ΰ¨Έΰ¨Όΰ¨Ύΰ¨?ΰ¨² ΰ¨¨ΰ¨Ήΰ©ΰ¨ ΰ¨Ήΰ© ΰ¨ΰ¨Ύΰ¨ΰ¨¦ΰ©...

β οΈ ΰ΄ΰ΅ΰ΄΅ΰ΄ΰ΅ΰ΄―ΰ΅ΰ΄³ΰ΅ΰ΄³ ΰ΄ΰ΄ΰ΅ΰ΄ΰ΄³ΰ΅ΰ΄ΰ΅ ΰ΄ΰ΄ͺΰ΅βΰ΄‘ΰ΅ΰ΄±ΰ΅ΰ΄±ΰ΅ ΰ΄ΰ΅ΰ΄―ΰ΅βΰ΄€ ΰ΄ΰ΄Ύΰ΄¨ΰ΄²ΰ΄Ώΰ΅½ ΰ΄ΰ΅ΰ΄°ΰ΅ΰ΄.  ΰ΄ΰ΄ΰ΅ΰ΄ΰ΄³ΰ΅ΰ΄ΰ΅ ΰ΄ΰ΄ͺΰ΅βΰ΄‘ΰ΅ΰ΄±ΰ΅ΰ΄±ΰ΅ ΰ΄ΰ΄Ύΰ΄¨ΰ΄²ΰ΄Ώΰ΅½ ΰ΄¨ΰ΄Ώΰ΄¨ΰ΅ΰ΄¨ΰ΅ ΰ΄¨ΰ΄Ώΰ΄ΰ΅ΰ΄ΰ΅Ύ ΰ΄ΰ΅ΰ΄°ΰ΅ΰ΄¨ΰ΅ΰ΄¨ΰ΄€ΰ΅ ΰ΄΅ΰ΄°ΰ΅ ΰ΄¬ΰ΅ΰ΄ΰ΅ΰ΄ΰ΅ ΰ΄¨ΰ΄Ώΰ΄ΰ΅ΰ΄ΰ΅Ύΰ΄ΰ΅ΰ΄ΰ΅ ΰ΄Έΰ΄Ώΰ΄¨ΰ΄Ώΰ΄? ΰ΄¨ΰ΅½ΰ΄ΰ΄Ώΰ΄²ΰ΅ΰ΄²....

β οΈ ΰ€Ήΰ€?ΰ€Ύΰ€°ΰ₯ ΰ€¨ΰ€Ώΰ€ΰ₯ ΰ€¦ΰ€Ώΰ€ ΰ€ΰ€―ΰ₯ update ΰ€ΰ₯ΰ€¨ΰ€² ΰ€ΰ₯ join ΰ€ΰ€°ΰ₯ ΰ€ΰ€¬ ΰ€€ΰ€ ΰ€ΰ€ͺ ΰ€Ήΰ€?ΰ€Ύΰ€°ΰ₯ update ΰ€ΰ₯ΰ€¨ΰ€² ΰ€ΰ₯ join ΰ€¨ΰ€Ήΰ₯ΰ€ ΰ€ΰ€°ΰ₯ΰ€ΰ€ΰ₯ ΰ€€ΰ€¬ ΰ€€ΰ€ bot ΰ€ΰ€ͺΰ€ΰ₯ ΰ€?ΰ₯ΰ€΅ΰ₯ ΰ€¨ΰ€Ήΰ₯ΰ€ ΰ€¦ΰ₯ΰ€ΰ€Ύ..."""

    URLSHORT_TXT = """<b>β€ πππ₯π©: π΄ππ πππππππΎπ

ππππ πππππππ πππππ π’ππ ππ πππππ π πππ 

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ /short: πππΎ ππππ πΌππππΊππ½ ππππ ππππ ππππ ππ ππΎπ ππππππΎπ½ πππππ

βπ€ππΊππππΎ:
/short https://t.me/+veUIdIW2CQ5GU5</b>"""


    URLSHORTN_TXT = """<b>β€ πππ₯π©: π΄ππ πππππππΎπ

ππππ πππππππ πππππ π’ππ ππ πππππ π πππ 

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ /short: πππΎ ππππ πΌππππΊππ½ ππππ ππππ ππππ ππ ππΎπ ππππππΎπ½ πππππ

βπ€ππΊππππΎ:
/short https://t.me/+veUIdIW25mOGU5</b>"""

    GHHM_TXT = """<b>7k User π Thanks For Your Support...

π©πππ π π½π½ π?ππ π‘ππ π³π πΈπππ π¦ππππ π π π π½πππ, π¨π πΆπππ π―πππππ½πΎ π¬ππππΎπ π³ππΎππΎ... π


     βοΈ ππ²π?πππΏπ²π βοΈ

βͺ AutoFilter, Manual Filter
βͺ IMDb HD Posters
βͺ IMDb Real Details
βͺ Two Buttons Mode
βͺ Force Subscribe
βͺ Extra Features: download songs, download you tube video, URL Shortner,  

β More Features Adding Soon</b> π"""

    GHHN_TXT = """Extra features"""

    OWNER_TXT = """<b>>ββββα Owner Details αββββ<
    
β­οΈ FULL NAME : Akshay Chand
β­οΈ USERNAME: uploading
β­οΈPERMANENT DM LINK : Uploading"""

    SPELLING_TEXT = """<u><b> Malik name test</b></u>"""


    GROUP_R_TXT = """<b>GROUP RULES

βοΈ  Search With Correct Spelling..

βοΈ Try to Search movie With  Year If The bot is Not Sending You Accurate Result..

βοΈ Search Series In The Given From Example : Gotham S03E01 And S03E10..

βοΈ Search Movies  in The Given From Example:    
(1) Avengers.. β
(2) Avengers Hindi. β
(3) Don't Tipe Avengers Hindi Dubbed..β

βοΈDon't Do Any Self Promotion.

βοΈ Don't Send Any Kind Of Photo Video Documents URL ETC.

βοΈ Sending The Above  Mantained Things Will Lead To Permanent Ban.

βοΈDon't Request Any Things Other Than Movie Series Animes.

βοΈ Give and Tak Respect</b>.."""

MALIK_PHH = """<b>Hay π {}.... π· β€οΈ

π welcome to Our Group...
  
        π π <s>{}</s> π π

π You Can Find π Movies / Series / Animes etc. From Here. Enjoy π...

π Plz do You not request the owner for the movie.. or else you will be blocked directly...β οΈ

β If there is any problem with the bot then contact the owner..

If you have any question then contact us below  π</b>"""

ALURT_FND = """<b>Your π {}βοΈ spelling is not correct, please choose from the list given π
               ββββββ’ββ’Β°β’ββ’Β°β’ββββββ
 β° CHECK YOUR MOVIE ON THE GIVEN LIST AND SELECT YOUR MOVIE..                                             β°
               ββββββ’ββ’Β°β’ββ’Β°β’ββ’β βββ
"""

MNTFN = """<b>β­οΈ α΄ΚΙͺκ± α΄α΄α΄ Ιͺα΄ Ι΄α΄α΄ ?α΄α΄Ι΄α΄ α΄Κ α΄α΄α΄α΄Κα΄κ±α΄. Κα΄Η«α΄α΄κ±α΄ α΄α΄ α΄α΄α΄ΙͺΙ΄..

β­οΈ Κα΄ α΄α΄α΄ Ιͺα΄ Κα΄α΄α΄Κα΄ α΄α΄α΄α΄Κα΄κ±α΄ α΄α΄ α΄α΄ α΄ΙͺΚα΄ΚΚα΄ Ι΄α΄ΚΙͺ Κα΄Ιͺ Ι΄Ιͺα΄Κα΄ α΄α΄α΄ΙͺΙ΄ κ±α΄ Κα΄Η«α΄α΄κ±α΄ α΄α΄Κα΄... 

β­οΈ Κα΄Η«α΄α΄κ±α΄ α΄α΄ α΄α΄α΄ΙͺΙ΄.. π</b>"""


ADG = """<b>Hay. {}..\n\nThankyou For Adding Me In.. β£οΈ

             π <s>{}</s> π </b>"""

ADDG = """Κα΄Κ..

Ιͺα΄ β‘οΈ α΄α΄α΄‘α΄Κ?α΄Κ α΄α΄α΄α΄-?ΙͺΚα΄α΄Κ Κα΄α΄...
π Κα΄α΄ α΄α΄Ι΄ α΄sα΄ α΄α΄ α΄s α΄ α΄α΄α΄α΄-?ΙͺΚα΄α΄Κ ΙͺΙ΄ Κα΄α΄Κ Ι’Κα΄α΄α΄ ....
Ιͺα΄s α΄α΄sΚ α΄α΄ α΄sα΄ α΄α΄: α΄α΄sα΄ α΄α΄α΄ α΄α΄ α΄α΄ Κα΄α΄Κ Ι’Κα΄α΄α΄ α΄s α΄α΄α΄ΙͺΙ΄, α΄Κα΄α΄s α΄ΚΚ, Ιͺ α΄‘ΙͺΚΚ α΄Κα΄α΄ Ιͺα΄α΄ α΄α΄α΄ Ιͺα΄s α΄Κα΄Κα΄...π

β οΈ α΄α΄Κα΄ Κα΄Κα΄ α΄Κα΄α΄α΄ Κα΄Κα΄ Κα΄α΄α΄α΄Ι΄..

Β©α΄α΄Ι΄α΄α΄ΙͺΙ΄α΄α΄ ΚΚ: Akshay Chand"""

M_NNT_FND = """Updating"""

M_NNT_FNDD = """Updating."""


