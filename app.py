from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.globals['enumerate'] = enumerate

news_articles = [
    {
        "id": 1,
        "tag": "Sikhumbula",
        "title": "Sekuphele 8 Years Adlula Emhlabeni USbongiseni Ngubane — Mjik'jelwa",
        "summary": "USbongiseni 'Mjik'jelwa' Ngubane wazalwa mhla zingama-17 kuSepthemba 1983 washona mhla zingama-25 kuNhlaba 2018 eneminyaka engu-35. Wayengagcini nje ngokuba umculi kuphela, kodwa wayeyingqalabutho yeMaskandi — umqambi, umdidiyeli, umeluleki kanye nesigingci esivelele sezintambo eziyi-12 esadabuka KwaZulu-Natal.",
        "author": "Maskandi Online Magazine",
        "date": "25 May 2026",
        "read_time": "3 min read",
        "featured": True,
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
        "tag": "Events",
        "title": "Big Maskandi Festival Returns to Durban This August",
        "summary": "Thousands of fans are expected at the annual Maskandi Music Festival, returning bigger than ever with a two-day programme and over 20 artists on the lineup.",
        "author": "Nomsa Zulu",
        "date": "17 May 2026",
        "read_time": "2 min read",
        "featured": False,
        "image": "",
    },
    {
        "id": 4,
        "tag": "Interview",
        "title": "Ntencane Speaks Out on Challenges Facing Young Maskandi Artists",
        "summary": "In a candid exclusive interview, Ntencane opens up about his humble beginnings, industry obstacles, and his vision for the future of Maskandi music.",
        "author": "Bongani Mthembu",
        "date": "16 May 2026",
        "read_time": "5 min read",
        "featured": False,
        "image": "",
    },
    {
        "id": 5,
        "tag": "Music",
        "title": "Mthandeni SK New Single Breaks Streaming Records",
        "summary": "The Maskandi sensation's latest release hit one million streams on local platforms within 48 hours, a first for the genre.",
        "author": "Thandi Nkosi",
        "date": "15 May 2026",
        "read_time": "2 min read",
        "featured": False,
        "image": "",
    },
]

artists = [
    {
        "initials": "KH",
        "name": "Khuzani Mpungose",
        "age": 36,
        "region": "Nkandla, KwaZulu-Natal",
        "albums": "Inja Nogodo, Umqhele Nethawula",
        "songs": "Isixaxa Samaxoki, Bengingazi, Ngeke Ngihleke",
        "bio": "Khuzani is one of the biggest Maskandi stars in South Africa and continues to dominate the genre.",
        "image": "khuzani.png",
    },
    {
        "initials": "MZ",
        "name": "Mzukulu",
        "age": "30s",
        "region": "KwaZulu-Natal",
        "albums": "Ivolovolo, Yimi Unompempe",
        "songs": "Amagobongo, Ithuba, Yimi Unompempe",
        "bio": "Mzukulu is known for traditional Maskandi sounds and energetic live performances.",
        "image": "mzukulu.png",
    },
    {
        "initials": "NT",
        "name": "Ntencane",
        "age": "Mid-20s",
        "region": "KwaZulu-Natal",
        "albums": "Uboya Enkomeni, Isigqila Sothando",
        "songs": "Wawuthembeni, Ngivunywe Usathane, Uboya Enkomeni",
        "bio": "Ntencane became famous for emotional love songs mixed with Maskandi style.",
        "image": "ntencane.png",
    },
    {
        "initials": "TL",
        "name": "Thokozani Langa",
        "age": 54,
        "region": "Ulundi, KwaZulu-Natal",
        "albums": "I-Protection Order, Ipeni Nephepha",
        "songs": "Ngelinye Ilanga, I-Protection Order",
        "bio": "Respected for storytelling, humor, and strong Zulu cultural themes in his music.",
        "image": "thokozane_langa.png",
    },
    {
        "initials": "SM",
        "name": "Sminofu",
        "age": "Young generation",
        "region": "KwaZulu-Natal",
        "albums": "Rush Hour, Gqiba I Bigger",
        "songs": "Ngiziphathele, Sehlukene, Sajola Kamnandi",
        "bio": "Sminofu mixes modern music styles with traditional Maskandi and is popular among youth.",
        "image": "",
    },
    {
        "initials": "MT",
        "name": "Mthandeni SK",
        "age": "30s",
        "region": "KwaZulu-Natal",
        "albums": "Impisi Iyalaya, Amakhothangqoko",
        "songs": "Paris, Gucci, Imali Nemoto",
        "bio": "Known for modern Maskandi hits and a strong fan base across South Africa.",
        "image": "mthandeni.png",
    },
]

events = [
    {"date": "07 Jun 2026", "title": "Khuzani Live at Moses Mabhida Stadium", "location": "Durban, KwaZulu-Natal"},
    {"date": "14 Jun 2026", "title": "Maskandi Nite Jozi Edition", "location": "Johannesburg, Gauteng"},
    {"date": "28 Jun 2026", "title": "Ntencane and Friends Annual Bash", "location": "Nkandla, KwaZulu-Natal"},
    {"date": "02 Aug 2026", "title": "Maskandi Music Festival 2026", "location": "Durban ICC, KwaZulu-Natal"},
]

@app.route("/")
def home():
    featured = next((a for a in news_articles if a["featured"]), None)
    latest = [a for a in news_articles if not a["featured"]]
    return render_template("index.html", featured=featured, latest=latest, artists=artists, events=events)

@app.route("/news")
def news():
    return render_template("news.html", articles=news_articles)

@app.route("/artists")
def artists_page():
    return render_template("artists.html", artists=artists)

@app.route("/events")
def events_page():
    return render_template("events.html", events=events)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
