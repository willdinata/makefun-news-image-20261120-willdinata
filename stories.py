# stories.py - Data module for THE MERIDIAN (20 November 2026)

REGION_COLOURS = {
    "EUROPE": (20, 50, 90),       # deep blue
    "ASIA": (150, 40, 40),        # brick red
    "BUSINESS": (20, 100, 100),   # teal
    "US": (80, 90, 110),          # slate
    "AMERICAS": (160, 110, 20),   # ochre
    "AFRICA": (110, 40, 90),      # plum
    "GLOBAL": (60, 70, 80),       # charcoal / dark slate
    "WORLD": (70, 70, 70),        # dark grey
}

MAINS = [
    {
        "n": 1,
        "label": "EUROPE · CONFLICT",
        "icon": "burst",
        "head": "Russia's heaviest barrage in months rains on Ukraine.",
        "desc": "Hours after the Shenzhen peace summit, Moscow fires more than 110 missiles and some 400 drones overnight; 8 people are killed, three Kyiv bridges are hit and Poland scrambles jets as its airspace is violated.",
        "place": "Kyiv",
        "lat": 50.4,
        "lon": 30.5,
    },
    {
        "n": 2,
        "label": "ASIA · WEATHER",
        "icon": "cyclone",
        "head": "Cyclone Akvan slams ashore on India's east coast.",
        "desc": "Landfall near Gopalpur at dawn with winds gusting to 90 km/h; 300,000 people were evacuated to 9,341 shelters ahead of the third cyclone to hit this coast in a month, and no major damage is reported.",
        "place": "Gopalpur, India",
        "lat": 19.3,
        "lon": 85.0,
    },
    {
        "n": 3,
        "label": "BUSINESS · MARKETS",
        "icon": "chart",
        "head": "AI sell-off goes global as the Nikkei plunges 4.8%.",
        "desc": "Doubts over AI valuations sweep Asia on Friday: SoftBank sinks 16%, Seoul's exchange triggers a sell-side halt, AMD slides on a short-seller report and gold drops 4.2%.",
        "place": "Tokyo",
        "lat": 35.7,
        "lon": 139.7,
    },
    {
        "n": 4,
        "label": "EUROPE · PROTESTS",
        "icon": "sign",
        "head": "A generation marches: youth strike sweeps 25+ countries.",
        "desc": "Students and workers fill the streets over living costs, housing and rearmament; in Italy the CGIL union stages a general strike under the banner of schools, not war.",
        "place": "Rome",
        "lat": 41.9,
        "lon": 12.5,
    },
    {
        "n": 5,
        "label": "US · CYBER",
        "icon": "chip",
        "head": "White House fires its cyber chief after a week of outages.",
        "desc": "National cyber director Sean Cairncross is dismissed after failures hit air travel and email services; the Pentagon's chief information officer steps in, and the EU reports an AI-powered cyberattack.",
        "place": "Washington",
        "lat": 38.9,
        "lon": -77.0,
    },
    {
        "n": 6,
        "label": "AMERICAS · SECURITY",
        "icon": "shield",
        "head": "Haiti raid kills 34 in push to retake gang corridor.",
        "desc": "Security forces backed by Salvadoran troops storm Martissant, the corridor linking the capital to the west and south that gangs have held since 2021.",
        "place": "Port-au-Prince",
        "lat": 18.5,
        "lon": -72.3,
    },
    {
        "n": 7,
        "label": "US · TECHNOLOGY",
        "icon": "chip",
        "head": "California subpoenas Nvidia as chip scandal widens.",
        "desc": "The state attorney general probes whether advanced chips or data reached China; chief executive Jensen Huang has resigned, and a House panel says sales of 879,000 AI chips to Chinese firms were approved.",
        "place": "Santa Clara",
        "lat": 37.4,
        "lon": -121.9,
    },
    {
        "n": 8,
        "label": "AFRICA · MIGRATION",
        "icon": "boat",
        "head": "Dozens missing as migrant boat sinks off Senegal.",
        "desc": "A boat carrying 50 to 100 people capsizes off Yenne; four bodies are recovered, dozens are missing, and arrivals in Spain's Canary Islands are up nearly two-thirds this year.",
        "place": "Yenne, Senegal",
        "lat": 14.7,
        "lon": -17.4,
    },
    {
        "n": 9,
        "label": "AMERICAS · POLITICS",
        "icon": "ballot",
        "head": "Bukele files for a third term in El Salvador.",
        "desc": "President Nayib Bukele formally registers his candidacy for a six-year third term after a 2025 constitutional change scrapped term limits; supporters credit his crackdown on gangs.",
        "place": "San Salvador",
        "lat": 13.7,
        "lon": -89.2,
    },
    {
        "n": 10,
        "label": "EUROPE · DIPLOMACY",
        "icon": "flag",
        "head": "UK and EU set to seal a youth mobility deal.",
        "desc": "A Friday summit in Brussels is expected to approve a youth mobility scheme, with deals on food trade and carbon emissions also on the table, as Britain's prime minister reopens the Brexit debate.",
        "place": "Brussels",
        "lat": 50.8,
        "lon": 4.4,
    },
    {
        "n": 11,
        "label": "GLOBAL · CLIMATE",
        "icon": "leaf",
        "head": "COP31 reaches its final day with fossil phase-out off the table.",
        "desc": "The draft deal in Antalya drops any call to phase out fossil fuels and drops net-zero dates; Pacific nations demand a phase-out and African countries press for more climate finance.",
        "place": "Antalya",
        "lat": 36.9,
        "lon": 30.7,
    },
    {
        "n": 12,
        "label": "ASIA · DIPLOMACY",
        "icon": "globe",
        "head": "Xi hosts Albanese in Shenzhen for APEC talks.",
        "desc": "China's president urges a trust-based partnership with Australia as Asia-Pacific leaders gather in Shenzhen; the talks come a day after the first Trump-Xi-Putin summit in the same city.",
        "place": "Shenzhen",
        "lat": 22.5,
        "lon": 114.1,
    },
    {
        "n": 13,
        "label": "AMERICAS · ECONOMY",
        "icon": "coin",
        "head": "Brazil sells a billion dollars to slow the real's slide.",
        "desc": "The central bank sells reserves as the dollar nears 5.93 reais; the real has lost about 18% in a month, pushing up the price of imports for Brazilian households.",
        "place": "Brasilia",
        "lat": -15.8,
        "lon": -47.9,
    },
]

BRIEFS = [
    {
        "n": 14,
        "label": "EUROPE · UKRAINE AID",
        "head": "London: Britain pledges more than 1,000 drones for Ukraine in a 260-million-pound package",
    },
    {
        "n": 15,
        "label": "EUROPE · SECURITY",
        "head": "Warsaw: Poland investigates unknown objects after its airspace was violated during the barrage",
    },
    {
        "n": 16,
        "label": "US · SANCTIONS",
        "head": "Washington: United States sanctions the Comancheros and 'Ndrangheta crime networks",
    },
    {
        "n": 17,
        "label": "US · POLITICS",
        "head": "Washington: Trump posthumously pardons baseball legend Pete Rose",
    },
    {
        "n": 18,
        "label": "US · JUSTICE",
        "head": "Florida carries out a record 20th execution of the year; Texas executes a 70-year-old man",
    },
    {
        "n": 19,
        "label": "ASIA · DIPLOMACY",
        "head": "Kathmandu: Nepal's prime minister Balendra Shah will make his first state visit to India",
    },
    {
        "n": 20,
        "label": "ASIA · ECONOMY",
        "head": "New Delhi: Modi urges Indian industry to cut imports and create jobs",
    },
    {
        "n": 21,
        "label": "ASIA · DIPLOMACY",
        "head": "Shenzhen: Japan's prime minister Takaichi receives a cool reception at APEC in China",
    },
    {
        "n": 22,
        "label": "ASIA · ECONOMY",
        "head": "Tokyo: core inflation hits the year's high, keeping a central bank rate hike on track",
    },
    {
        "n": 23,
        "label": "AMERICAS · POLITICS",
        "head": "Buenos Aires: the Senate unanimously approves a permanent disability framework, 71 to 0",
    },
    {
        "n": 24,
        "label": "AMERICAS · PROTESTS",
        "head": "Bogota: thousands march against tax plans as unions call a national strike",
    },
    {
        "n": 25,
        "label": "GLOBAL · POLITICS",
        "head": "New York: the race to succeed Guterres as UN chief stalls after eight deadlocked votes",
    },
    {
        "n": 26,
        "label": "EUROPE · MEDIA",
        "head": "London: the prime minister presses Google to remove a Russell Brand video",
    },
    {
        "n": 27,
        "label": "BUSINESS · CLIMATE",
        "head": "Meta rethinks its 2030 climate goals as AI data centres drive its emissions up",
    },
    {
        "n": 28,
        "label": "AFRICA · ECONOMY",
        "head": "Lilongwe: Malawi's fuel crisis deepens into chaos",
    },
    {
        "n": 29,
        "label": "GLOBAL · GAMES",
        "head": "Sales trackers estimate GTA VI took 2.36 billion dollars on its first day, an entertainment record",
    },
    {
        "n": 30,
        "label": "WORLD · SPORT",
        "head": "Las Vegas: Formula 1 takes over the Strip for its night-race weekend",
    },
    {
        "n": 31,
        "label": "AFRICA · SOCIETY",
        "head": "Harare: the HALO Trust destroys its 250,000th landmine in Zimbabwe",
    },
    {
        "n": 32,
        "label": "WORLD · SPORT",
        "head": "Sydney: marathon champion Jepchirchir is banned for three years over doping",
    },
    {
        "n": 33,
        "label": "ASIA · UNREST",
        "head": "Dhaka: fresh arson and protests as Bangladesh braces for Hasina's planned return",
    },
]

NUMBERS = [
    ("110+", "missiles fired at Ukraine overnight"),
    ("300,000", "people evacuated before Cyclone Akvan"),
    ("-4.8%", "the Nikkei's fall on Friday"),
    ("25+", "countries in the youth day of action"),
    ("90.05", "dollars for a barrel of Brent crude"),
    ("2.36bn", "dollars of GTA VI sales on day one"),
]
