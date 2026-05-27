from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.globals['enumerate'] = enumerate

news_articles = [
    {
        "id": 1,
        "tag": "Exclusive",
        "title": "Mfaz' Omnyama: 25 Years Since We Lost the African Jimi Hendrix of Maskandi",
        "summary": "On 17 March 2001, South Africa lost one of its greatest Maskandi legends — Mpatheni Khumalo, known as Mfaz' Omnyama. Twenty-five years later, we remember his extraordinary life, his left-handed guitar mastery, and the timeless songs that continue to echo across KwaZulu-Natal and beyond.",
        "author": "Maskandi Online Magazine",
        "date": "17 March 2026",
        "read_time": "5 min read",
        "featured": True,
        "image": "mfaz_omnyama.jpg",
        "facebook_embed": "https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid02x2ETQkdJH71RaU2zKrpowuNCN444PnZuYPtAopdzrQo66zGmznXMvdRZvtzTTCLjl%26id%3D61579378984039&show_text=true&width=500"
    },
    {
        "id": 2,
        "tag": "Tribute",
        "title": "Remembering Busani 'Ntshebe' Khuzwayo — The Guitar Legend of Izingane Zoma",
        "summary": "Maskandi Online pays tribute to Busani 'Ntshebe' Khuzwayo, the beloved guitarist of Izingane Zoma, whose extraordinary talent and love for the isiginci left a permanent mark on Maskandi music and its fans across South Africa.",
        "author": "Maskandi Online Magazine",
        "date": "13 May 2026",
        "read_time": "4 min read",
        "featured": False,
        "image": None,
        "facebook_embed": "https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid0f4gouWk4yUVTv9B655gq7GqhLPMA2MuJVjwSDVTtNYnBhKiFoZYwgC31kqaVF5Rhl%26id%3D61579378984039&show_text=true&width=500"
    },
    {
        "id": 3,
        "tag": "New Release",
        "title": "Ojakalasi Drop New EP 'Move On' — Available Now on All Streaming Platforms",
        "summary": "Rising Maskandi duo Ojakalasi have released their brand new EP titled 'Move On', now available on Spotify, Apple Music, and all major digital streaming platforms. The project showcases the duo's musical evolution and features a blend of traditional Maskandi sounds with fresh contemporary influences.",
        "author": "Maskandi Online Magazine",
        "date": "18 May 2026",
        "read_time": "2 min read",
        "featured": False,
        "image": "ojakalasi.jpg",
        "facebook_embed": "https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid04Kejn68RdHK1xdXR1zeSE7LSjSXJZa6dtzVn3hL5BhKoehDbdDMs4A6C7K32csd4l%26id%3D61579378984039&show_text=true&width=500"
    },
    {"id": 4, "tag": "Events", "title": "Big Maskandi Festival Returns to Durban This August", "summary": "Thousands of fans are expected at the annual Maskandi Music Festival, returning bigger than ever with a two-day programme and over 20 artists on the lineup.", "author": "Nomsa Zulu", "date": "17 May 2026", "read_time": "2 min read", "featured": False, "image": None, "facebook_embed": None},
    {"id": 5, "tag": "Interview", "title": "Ntencane Speaks Out on Challenges Facing Young Maskandi Artists", "summary": "In a candid exclusive interview, Ntencane opens up about his humble beginnings, industry obstacles, and his vision for the future of Maskandi music.", "author": "Bongani Mthembu", "date": "16 May 2026", "read_time": "5 min read", "featured": False, "image": None, "facebook_embed": None},
    {"id": 6, "tag": "Music", "title": "Mthandeni SK New Single Breaks Streaming Records", "summary": "The Maskandi sensation's latest release hit one million streams on local platforms within 48 hours, a first for the genre.", "author": "Thandi Nkosi", "date": "15 May 2026", "read_time": "2 min read", "featured": False, "image": None, "facebook_embed": None},
    {"id": 7, "tag": "News", "title": "Government Pledges Support for Maskandi Cultural Heritage Programme", "summary": "The Department of Arts and Culture announced a new fund to support upcoming Maskandi artists and preserve the genre's traditions for future generations.", "author": "Lungelo Dube", "date": "14 May 2026", "read_time": "3 min read", "featured": False, "image": None, "facebook_embed": None},
]

artists = [
    {"initials": "KH", "name": "Khuzani", "albums": 7, "region": "KZN"},
    {"initials": "MT", "name": "Mthandeni SK", "albums": 5, "region": "Eshowe"},
    {"initials": "NT", "name": "Ntencane", "albums": 4, "region": "Nkandla"},
    {"initials": "MG", "name": "Mfana Kah Gogo", "albums": 2, "region": "Durban"},
]

events = [
    {"date": "07 Jun 2026", "title": "Khuzani Live at Moses Mabhida Stadium", "location": "Durban, KwaZulu-Natal"},
    {"date": "14 Jun 2026", "title": "Maskandi Nite Jozi Edition", "location": "Johannesburg, Gauteng"},
    {"date": "28 Jun 2026", "title": "Ntencane and Friends Annual Bash", "location": "Nkandla, KwaZulu-Natal"},
    {"date": "02 Aug 2026", "title": "Maskandi Music Festival 2026", "location": "Durban ICC, KwaZulu-Natal"},
]

top10_songs = [
    {"rank": 1, "title": "Ngiyabonga Baba", "artist": "Khuzani", "trend": "up", "weeks": 3},
    {"rank": 2, "title": "Iskhathi Sami", "artist": "Mthandeni SK", "trend": "up", "weeks": 1},
    {"rank": 3, "title": "Impi Yami", "artist": "Ntencane", "trend": "same", "weeks": 5},
    {"rank": 4, "title": "Move On", "artist": "Ojakalasi", "trend": "up", "weeks": 2},
    {"rank": 5, "title": "Uyangidumaza", "artist": "Mfana Kah Gogo", "trend": "down", "weeks": 4},
    {"rank": 6, "title": "Sengiyabona", "artist": "Khuzani", "trend": "up", "weeks": 1},
    {"rank": 7, "title": "Angisekho", "artist": "Ntencane", "trend": "down", "weeks": 6},
    {"rank": 8, "title": "Izinsuku Zami", "artist": "Mthandeni SK", "trend": "up", "weeks": 2},
    {"rank": 9, "title": "Wena Wedwa", "artist": "Mfana Kah Gogo", "trend": "same", "weeks": 3},
    {"rank": 10, "title": "Ubuhle Bakho", "artist": "Ojakalasi", "trend": "up", "weeks": 1},
]

@app.route("/")
def home():
    featured = next((a for a in news_articles if a["featured"]), None)
    latest = [a for a in news_articles if not a["featured"]]
    return render_template("index.html", featured=featured, latest=latest, artists=artists, events=events, top10=top10_songs)

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

if __name__ == "__main__":
    app.run(debug=True)
