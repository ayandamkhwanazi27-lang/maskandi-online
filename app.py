from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
app.jinja_env.globals['enumerate'] = enumerate

@app.route('/static/<path:filename>')
def static_files(filename):
    static_path = os.path.join(app.root_path, 'static', filename)
    if os.path.exists(static_path):
        return send_from_directory(os.path.join(app.root_path, 'static'), filename)
    return send_from_directory(app.root_path, filename)

news_articles = [
    {
        "id": 0,
        "tag": "Live Review",
        "title": "INKOS'YAMAGCOKAMA LIVE: Umgowo Experience Leaves Carnival City Wanting More",
        "summary": "Thousands of Maskandi fans gathered at Carnival City for an unforgettable celebration of music, culture, and heritage. When Inkos'YamaGcokama stepped onto the stage, the crowd erupted with excitement, delivering a powerful live performance that will be remembered for years to come.",
        "full_story": "Supporters from across South Africa travelled to witness the historic event, creating an electric atmosphere from the moment the gates opened. Fans proudly dressed in traditional attire and artist merchandise filled the venue, ready to experience one of the biggest Maskandi shows of the year.\n\nWhen Inkos'YamaGcokama stepped onto the stage, the crowd erupted with excitement. He delivered a powerful live performance, taking fans on a musical journey through his biggest hits while celebrating the rich traditions of Maskandi. Every song was met with loud singalongs, dancing, and applause, making it a night that will be remembered for years to come.\n\nThe event featured outstanding production, quality sound, spectacular stage lighting, and memorable guest appearances, giving fans an experience worthy of its name. The success of INKOS'YAMAGCOKAMA LIVE: Umgowo Experience once again demonstrated the growing influence of Maskandi music and Inkos'YamaGcokama's ability to unite people through his artistry.\n\nFollowing the successful event, Inkos'YamaGcokama thanked everyone who contributed to making the show a triumph.\n\n'Ngithanda ukubonga bonke abantu abaphume ngobuningi bazongeseka eCarnival City ngoMgqibelo. Uthando eningibonise lona lukhulu kakhulu. Ngiyabonga kubalandeli bami, kubaculi, kubaxhasi, kubahleli bomcimbi, nakubo bonke abasebenze kanzima ukuze INKOS'YAMAGCOKAMA LIVE: Umgowo Experience ibe yimpumelelo. Sengathi uNkulunkulu anganibusisa nonke.'\n\nThe success of INKOS'YAMAGCOKAMA LIVE: Umgowo Experience has set a new benchmark for Maskandi events, proving once again that the genre continues to grow while attracting audiences from all walks of life. As fans left Carnival City on Saturday night with smiles, songs, and unforgettable memories, one thing was certain — this was more than just a concert; it was an experience that will be talked about for a long time.",
        "author": "Maskandi Online Magazine",
        "date": "7 July 2026",
        "read_time": "4 min read",
        "featured": True,
        "image": "inkosi.jpg",
        "gallery": [],
    },
    {
        "id": 10,
        "tag": "Live Review",
        "title": "Mzukulu's Album Tour at Carnival City Declared a Major Success",
        "summary": "South African Maskandi star Mzukulu delivered a powerful and memorable performance at Carnival City's Big Top Arena in Johannesburg, where his highly anticipated album tour proved to be a major success, celebrating his latest project Ng'funa Intozami.",
        "full_story": "Held on 13 June 2026, the concert was staged at Carnival City, known for hosting large-scale live music and cultural events. The show opened its doors at 15:00, with the performance beginning later in the afternoon, creating a vibrant atmosphere filled with anticipation and excitement.\n\nFrom the moment Mzukulu stepped on stage, the energy in the arena reflected the strong connection he has built with his audience over the years. Fans responded enthusiastically as he performed a mix of his popular hits and newer material from the album, showcasing his signature blend of traditional Maskandi sound and modern stage production.\n\nThe Carnival City performance was designed as more than just a concert — it was presented as a theatrical musical experience, combining live instrumentation, cultural storytelling, and carefully crafted stage production.\n\nAudience reception was overwhelmingly positive, with many fans describing the event as one of Mzukulu's strongest live performances to date.",
        "author": "Maskandi Online Magazine",
        "date": "13 June 2026",
        "read_time": "4 min read",
        "featured": False,
        "image": "mzukulu1.jpeg",
        "gallery": ["mzukulu1.jpeg", "mzukulu2.jpeg", "mzukulu3.jpeg", "mzukulu4.jpeg", "mzukulu5.jpeg"],
    },
    {
        "id": 1,
        "tag": "Sikhumbula",
        "title": "Sekuphele 8 Years Adlula Emhlabeni USbongiseni Ngubane — Mjik'jelwa",
        "summary": "USbongiseni 'Mjik'jelwa' Ngubane wazalwa mhla zingama-17 kuSepthemba 1983 washona mhla zingama-25 kuNhlaba 2018 eneminyaka engu-35. Wayengagcini nje ngokuba umculi kuphela, kodwa wayeyingqalabutho yeMaskandi.",
        "author": "Maskandi Online Magazine",
        "date": "25 May 2026",
        "read_time": "3 min read",
        "featured": False,
        "image": "mjikjelwa.jpg",
    },
    {
        "id": 2,
        "tag": "New Album",
        "title": "Menzi Ndimande Drops New 2026 Album — EZohlala Nawe",
        "summary": "Maskandi artist Menzi Ndimande has just released his brand new 2026 album titled 'EZohlala Nawe', featuring 14 tracks. The album dropped 3 days ago and is already making waves across Maskandi music lovers in South Africa.",
        "author": "Maskandi Online Magazine",
        "date": "22 May 2026",
        "read_time": "2 min read",
        "featured": False,
        "image": "menzi_album.png",
    },
    {
        "id": 3,
        "tag": "Izindaba",
        "title": "'Ukugconana' kubakhele ugazi ezinkundleni zokuxhumana",
        "summary": "Umculi kamaskandi uGqizile Khanyile nomngani wakhe uMlondi Msweli sebezakhele ugazi ezinkundleni zokuxhumana ngama-video abo begconana. UGqizile usenabalandeli abangaphezu kuka-378 000 kwiFacebook, abawu-190 000 nama-like awu-3 million kwiTikTok.",
        "author": "Simangaliso Ntshangase",
        "date": "1 week ago",
        "read_time": "4 min read",
        "featured": False,
        "image": "gqizile.png",
    },
    {
        "id": 4,
        "tag": "Umculo",
        "title": "Ucikoza ngokwenzeka empilweni yabantu — uMlabalaba ne-albhamu entsha ethi Izethembiso",
        "summary": "Umculi kamaskandi uMlabalaba usedalule ukuthi ukuzinika isikhathi esanele sokupheka umculo wakhe omusha nokuqapha izinto ezenzeka empilweni yabantu kumsiza ukuthola izindikimba. I-albhamu yakhe yesikhombisa ethi Izethembiso inezingoma eziwu-17 futhi izingoma zayo sezidlalwe ngaphezu kuka-200 000.",
        "author": "Simangaliso Ntshangase",
        "date": "1 month ago",
        "read_time": "5 min read",
        "featured": False,
        "image": "mlablaba.png",
    },
    {
        "id": 5,
        "tag": "Izindaba",
        "title": "Uhlela ukuyoyethula kwezinye izindawo i-albhamu uBahubhe oxoshwe eWorkshop",
        "summary": "Umaskanda uBahubhe owenze indumezulu yomcimbi wokwethula i-albhamu yakhe ethi Ngiyobalanda usedalule ukuthi usexoshiwe eWorkshop eThekwini. Usehlela ukuyoyethula ngakubo, kanti uKhuzani wamthembisa ukeseka.",
        "author": "Fanelesibonge Bengu",
        "date": "2 months ago",
        "read_time": "3 min read",
        "featured": False,
        "image": "bahubhe.png",
    },
    {
        "id": 6,
        "tag": "Umculo",
        "title": "Ukusabalala ngemiyalezo kuqhakazise icwecwe likaNtencane — Awuyiphumuze",
        "summary": "Umculi kamaskandi uNtencane usedalule ukuthi ukugalela ngendlela ehlukile emculweni wakhe ngokudidiyela imiyalezo ehlukene kumsizile kakhulu. I-albhamu yakhe entsha ethi Awuyiphumuze enazo izingoma eziwu-16 sekukhona ezimbili ezidlalwe ngaphezu kuka-1 million.",
        "author": "Simangaliso Ntshangase",
        "date": "3 months ago",
        "read_time": "5 min read",
        "featured": False,
        "image": "",
    },
    {
        "id": 7,
        "tag": "Events",
        "title": "Newcastle Maskandi Festival Returns for Second Year",
        "summary": "The 2nd Annual Newcastle Maskandi Festival takes place at Majuba College Stadium, Madadeni on 2-3 May 2026. Two days of top Maskandi artists, food stalls, and a powerful community vibe.",
        "author": "Maskandi Online Magazine",
        "date": "01 May 2026",
        "read_time": "2 min read",
        "featured": False,
        "image": "",
    },
    {
        "id": 8,
        "tag": "Interview",
        "title": "Ntencane Speaks Out on Challenges Facing Young Maskandi Artists",
        "summary": "In a candid exclusive interview, Ntencane opens up about his humble beginnings, industry obstacles, and his vision for the future of Maskandi music.",
        "author": "Bongani Mthembu",
        "date": "16 May 2026",
        "read_time": "5 min read",
        "featured": False,
        "image": "",
    },
]

artists = [
    {"initials": "KH", "name": "Khuzani Mpungose", "age": 36, "region": "Nkandla, KwaZulu-Natal", "albums": "Inja Nogodo, Umqhele Nethawula", "songs": "Isixaxa Samaxoki, Bengingazi, Ngeke Ngihleke", "bio": "Khuzani is one of the biggest Maskandi stars in South Africa and continues to dominate the genre.", "image": "khuzani.png"},
    {"initials": "MZ", "name": "Mzukulu", "age": "30s", "region": "KwaZulu-Natal", "albums": "Ivolovolo, Yimi Unompempe", "songs": "Amagobongo, Ithuba, Yimi Unompempe", "bio": "Mzukulu is known for traditional Maskandi sounds and energetic live performances.", "image": "mzukulu.png"},
    {"initials": "NT", "name": "Ntencane", "age": "Mid-20s", "region": "KwaZulu-Natal", "albums": "Uboya Enkomeni, Isigqila Sothando", "songs": "Wawuthembeni, Ngivunywe Usathane, Uboya Enkomeni", "bio": "Ntencane became famous for emotional love songs mixed with Maskandi style.", "image": "ntencane.png"},
    {"initials": "TL", "name": "Thokozani Langa", "age": 54, "region": "Ulundi, KwaZulu-Natal", "albums": "I-Protection Order, Ipeni Nephepha", "songs": "Ngelinye Ilanga, I-Protection Order", "bio": "Respected for storytelling, humor, and strong Zulu cultural themes in his music.", "image": "thokozane_langa.png"},
    {"initials": "SM", "name": "Sminofu", "age": "Young generation", "region": "KwaZulu-Natal", "albums": "Rush Hour, Gqiba I Bigger", "songs": "Ngiziphathele, Sehlukene, Sajola Kamnandi", "bio": "Sminofu mixes modern music styles with traditional Maskandi and is popular among youth.", "image": "sminofu.jpeg"},
    {"initials": "MT", "name": "Mthandeni SK", "age": "30s", "region": "KwaZulu-Natal", "albums": "Impisi Iyalaya, Amakhothangqoko", "songs": "Paris, Gucci, Imali Nemoto", "bio": "Known for modern Maskandi hits and a strong fan base across South Africa.", "image": "mthandeni.png"},
]

events = [
    {"date": "2-3 May 2026", "title": "Newcastle Maskandi Festival (2nd Annual)", "location": "Majuba College Stadium, Madadeni", "description": "Two-day festival featuring top Maskandi artists, food stalls, cultural experience and community vibe.", "icon": "🎶"},
    {"date": "2 May 2026", "title": "Blue Nation Festival — Maskandi Feature", "location": "Carnival City, Sandton", "description": "Major music festival with Maskandi headliners, high-energy production and big-stage performances.", "icon": "🎤"},
    {"date": "16 June 2026", "title": "Umzumbe Maskandi Festival", "location": "Esibanini Sports Ground, Umzumbe", "description": "Focus on uplifting local artists and cultural tourism. Includes food village, workshops and community activities.", "icon": "🪘"},
    {"date": "26 September 2026", "title": "Ugu Maskandi Festival (6th Annual)", "location": "Ugu Sports & Leisure Centre, Port Shepstone", "description": "One of the biggest Maskandi celebrations in KZN. VIP and general tickets available.", "icon": "🪕"},
]

@app.route("/")
def home():
    featured = next((a for a in news_articles if a["featured"]), None)
    latest = [a for a in news_articles if not a["featured"]]
    return render_template("index.html", featured=featured, latest=latest, artists=artists, events=events)

@app.route("/news")
def news():
    return render_template("news.html", articles=news_articles)

@app.route("/article/<int:article_id>")
def article_detail(article_id):
    article = next((a for a in news_articles if a["id"] == article_id), None)
    if article is None:
        article = news_articles[0]
    return render_template("article.html", article=article)

@app.route("/artists")
def artists_page():
    return render_template("artists.html", artists=artists)

@app.route("/albums")
def albums():
    return render_template("albums.html")

@app.route("/events")
def events_page():
    return render_template("events.html", events=events)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/ads.txt")
def ads_txt():
    return send_from_directory(app.root_path, "ads.txt")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

if __name__ == "__main__":
    app.run(debug=True)
