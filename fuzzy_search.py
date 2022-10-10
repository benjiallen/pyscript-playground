"""
Example of using a module from pypi.

I want to use https://pypi.org/project/fuzzywuzzy/ to do fuzzy matching.

Useful article on using events in pyscript:
https://www.jhanley.com/blog/pyscript-javascript-callbacks/

Articles on loading 3rd party packages:
* https://pyodide.org/en/stable/usage/loading-packages.html#loading-packages
* https://docs.pyscript.net/latest/tutorials/getting-started.html#the-py-config-tag

TODO:
* Deploy to GitHub pages
* Get feedback on what i've built so far!
* Search by name and handle
* Work out how to add searches to browser history
* Add python typing information
* Add an "upload file" mode where you can upload a YAML file with the org chart
* Write some playwright tests

handle:
    - name: full name
    - title: job title
    - email: email address
    - manager: handle
    - employment_type: employee
    - cost_center: cost center
    - country: country
"""
import json
from js import document
from pyodide.ffi import create_proxy
from thefuzz import process

org_json: str = """
[
    {
        "gvanrossum": {
            "employment_type": "employee",
            "name": "Guido van Rossum",
            "email": "",
            "title": "BDFL",
            "cost_center": "Microsoft",
            "country": "San Francisco Bay Area"
        },
        "freddrake": {
            "manager": "gvanrossum",
            "employment_type": "employee",
            "name": "Fred Drake",
            "email": "fred@fdrake.net",
            "title": "BDFL",
            "cost_center": "@keepertech ",
            "country": "Reston, VA"
        },
        "birkenfeld": {
            "manager": "gvanrossum",
            "employment_type": "employee",
            "name": "Georg Brandl",
            "email": "georg@python.org",
            "title": "BDFL",
            "cost_center": "FZ J\u00fclich",
            "country": "M\u00fcnchen"
        },
        "vstinner": {
            "manager": "gvanrossum",
            "employment_type": "employee",
            "name": "Victor Stinner",
            "email": "vstinner@python.org",
            "title": "BDFL",
            "cost_center": "@RedHatOfficial",
            "country": "France"
        },
        "benjaminp": {
            "manager": "gvanrossum",
            "employment_type": "employee",
            "name": "Benjamin Peterson",
            "email": "",
            "title": "Product Manager",
            "cost_center": null,
            "country": null
        },
        "rhettinger": {
            "manager": "gvanrossum",
            "employment_type": "employee",
            "name": "Raymond Hettinger",
            "email": "",
            "title": "BDFL",
            "cost_center": "Mutable Minds, Inc.",
            "country": "Santa Clara, California"
        },
        "pitrou": {
            "manager": "gvanrossum",
            "employment_type": "employee",
            "name": "Antoine Pitrou",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "jackjansen": {
            "manager": "gvanrossum",
            "employment_type": "employee",
            "name": "Jack Jansen",
            "email": "Jack.Jansen@cwi.nl",
            "title": "BDFL",
            "cost_center": "Centrum voor Wiskunde en Informatica",
            "country": "Amsterdam, the Netherlands"
        },
        "serhiy-storchaka": {
            "manager": "gvanrossum",
            "employment_type": "employee",
            "name": "Serhiy Storchaka",
            "email": "",
            "title": "BDFL",
            "cost_center": "Neu.ro",
            "country": "Ukraine"
        },
        "loewis": {
            "manager": "gvanrossum",
            "employment_type": "employee",
            "name": "Martin v. L\u00f6wis",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "tim-one": {
            "manager": "freddrake",
            "employment_type": "employee",
            "name": "Tim Peters",
            "email": "tim.peters@gmail.com",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "akuchling": {
            "manager": "freddrake",
            "employment_type": "employee",
            "name": "Andrew Kuchling",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "warsaw": {
            "manager": "freddrake",
            "employment_type": "employee",
            "name": "Barry Warsaw",
            "email": "barry@python.org",
            "title": "BDFL",
            "cost_center": "LinkedIn",
            "country": null
        },
        "brettcannon": {
            "manager": "freddrake",
            "employment_type": "employee",
            "name": "Brett Cannon",
            "email": "",
            "title": "BDFL",
            "cost_center": "@microsoft ",
            "country": "Vancouver, BC, Canada"
        },
        "nnorwitz": {
            "manager": "freddrake",
            "employment_type": "employee",
            "name": null,
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "mdickinson": {
            "manager": "freddrake",
            "employment_type": "employee",
            "name": "Mark Dickinson",
            "email": "dickinsm@gmail.com",
            "title": "BDFL",
            "cost_center": "Enthought",
            "country": "Cambridge, UK"
        },
        "tiran": {
            "manager": "freddrake",
            "employment_type": "employee",
            "name": "Christian Heimes",
            "email": "christian@python.org",
            "title": "BDFL",
            "cost_center": "Red Hat",
            "country": "Hamburg, Germany"
        },
        "bitdancer": {
            "manager": "freddrake",
            "employment_type": "employee",
            "name": "R. David Murray",
            "email": "rdmurray@bitdance.com",
            "title": "BDFL",
            "cost_center": "Murray and Walker, Inc",
            "country": "MA USA"
        },
        "ezio-melotti": {
            "manager": "freddrake",
            "employment_type": "employee",
            "name": "Ezio Melotti",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "gpshead": {
            "manager": "freddrake",
            "employment_type": "employee",
            "name": "Gregory P. Smith",
            "email": "greg@krypto.org",
            "title": "BDFL",
            "cost_center": "Google",
            "country": "Menlo Park, CA"
        },
        "jeremyhylton": {
            "manager": "birkenfeld",
            "employment_type": "employee",
            "name": "Jeremy Hylton",
            "email": "",
            "title": "BDFL",
            "cost_center": "@google",
            "country": null
        },
        "vsajip": {
            "manager": "birkenfeld",
            "employment_type": "employee",
            "name": "Vinay Sajip",
            "email": "vinay_sajip@yahoo.co.uk",
            "title": "BDFL",
            "cost_center": null,
            "country": "United Kingdom"
        },
        "orsenthil": {
            "manager": "birkenfeld",
            "employment_type": "employee",
            "name": "Senthil Kumaran",
            "email": "senthil@python.org",
            "title": "BDFL",
            "cost_center": "AWS",
            "country": "San Francisco"
        },
        "terryjreedy": {
            "manager": "birkenfeld",
            "employment_type": "employee",
            "name": "Terry Jan Reedy",
            "email": "tjreedy@udel.edu",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "gward": {
            "manager": "birkenfeld",
            "employment_type": "employee",
            "name": "Greg Ward",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": "Montreal, Canada"
        },
        "merwok": {
            "manager": "birkenfeld",
            "employment_type": "employee",
            "name": "\u00c9ric",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "zooba": {
            "manager": "birkenfeld",
            "employment_type": "employee",
            "name": "Steve Dower",
            "email": "steve.dower@microsoft.com",
            "title": "BDFL",
            "cost_center": "Microsoft",
            "country": null
        },
        "ned-deily": {
            "manager": "birkenfeld",
            "employment_type": "employee",
            "name": "Ned Deily",
            "email": "nad@python.org",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "ncoghlan": {
            "manager": "birkenfeld",
            "employment_type": "employee",
            "name": "Nick Coghlan",
            "email": "",
            "title": "BDFL",
            "cost_center": "@tritiumdev ",
            "country": "Australia"
        },
        "pablogsal": {
            "manager": "birkenfeld",
            "employment_type": "employee",
            "name": "Pablo Galindo Salgado",
            "email": "Pablogsal@gmail.com",
            "title": "BDFL",
            "cost_center": "@Bloomberg",
            "country": "London, United Kingdom"
        },
        "1st1": {
            "manager": "vstinner",
            "employment_type": "employee",
            "name": "Yury Selivanov",
            "email": "yury@edgedb.com",
            "title": "BDFL",
            "cost_center": "@edgedb",
            "country": "San Francisco"
        },
        "ronaldoussoren": {
            "manager": "vstinner",
            "employment_type": "employee",
            "name": "Ronald Oussoren",
            "email": "ronaldoussoren@mac.com",
            "title": "BDFL",
            "cost_center": null,
            "country": "Amsterdam"
        },
        "berkerpeksag": {
            "manager": "vstinner",
            "employment_type": "employee",
            "name": "Berker Peksag",
            "email": "berker.peksag@gmail.com",
            "title": "BDFL",
            "cost_center": null,
            "country": "Helsinki, Finland"
        },
        "doerwalter": {
            "manager": "vstinner",
            "employment_type": "employee",
            "name": "Walter D\u00f6rwald",
            "email": "",
            "title": "BDFL",
            "cost_center": "LivingLogic AG",
            "country": "Bayreuth/Germany"
        },
        "kbkaiser": {
            "manager": "vstinner",
            "employment_type": "employee",
            "name": "Kurt B. Kaiser",
            "email": "kbk@shore.net",
            "title": "BDFL",
            "cost_center": "Python Software Foundation",
            "country": null
        },
        "amauryfa": {
            "manager": "vstinner",
            "employment_type": "employee",
            "name": "Amaury Forgeot d'Arc",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "zware": {
            "manager": "vstinner",
            "employment_type": "employee",
            "name": "Zachary Ware",
            "email": "zachary.ware@gmail.com",
            "title": "BDFL",
            "cost_center": null,
            "country": "Missouri, USA"
        },
        "ericvsmith": {
            "manager": "vstinner",
            "employment_type": "employee",
            "name": "Eric V. Smith",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "asvetlov": {
            "manager": "vstinner",
            "employment_type": "employee",
            "name": "Andrew Svetlov",
            "email": "andrew.svetlov@gmail.com",
            "title": "BDFL",
            "cost_center": "Neu.ro",
            "country": "Gijon"
        },
        "vadmium": {
            "manager": "vstinner",
            "employment_type": "employee",
            "name": "Martin Panter",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": "Melbourne, Australia"
        },
        "erlend-aasland": {
            "manager": "benjaminp",
            "employment_type": "employee",
            "name": "Erlend E. Aasland",
            "email": "erlend.aasland@protonmail.com",
            "title": "BDFL",
            "cost_center": "Innova AS",
            "country": "Sandnes, Norway"
        },
        "briancurtin": {
            "manager": "benjaminp",
            "employment_type": "employee",
            "name": "Brian Curtin",
            "email": "brian@python.org",
            "title": "BDFL",
            "cost_center": "@elastic",
            "country": "Lakewood, Colorado"
        },
        "skrah": {
            "manager": "benjaminp",
            "employment_type": "employee",
            "name": "Stefan Krah",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "florentx": {
            "manager": "benjaminp",
            "employment_type": "employee",
            "name": "Florent Xicluna",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "abalkin": {
            "manager": "benjaminp",
            "employment_type": "employee",
            "name": "Alexander Belopolsky",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": "New York"
        },
        "Yhg1s": {
            "manager": "benjaminp",
            "employment_type": "employee",
            "name": "T. Wouters",
            "email": "thomas@python.org",
            "title": "BDFL",
            "cost_center": "@google",
            "country": null
        },
        "larryhastings": {
            "manager": "benjaminp",
            "employment_type": "employee",
            "name": null,
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "malemburg": {
            "manager": "benjaminp",
            "employment_type": "employee",
            "name": "Marc-Andre Lemburg",
            "email": "",
            "title": "BDFL",
            "cost_center": "@malemburg",
            "country": "D\u00fcsseldorf, Germany"
        },
        "nascheme": {
            "manager": "benjaminp",
            "employment_type": "employee",
            "name": "Neil Schemenauer",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "methane": {
            "manager": "benjaminp",
            "employment_type": "employee",
            "name": "Inada Naoki",
            "email": "songofacandy@gmail.com",
            "title": "BDFL",
            "cost_center": null,
            "country": "Japan"
        },
        "doko42": {
            "manager": "rhettinger",
            "employment_type": "employee",
            "name": "Matthias Klose",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": "Berlin"
        },
        "avassalotti": {
            "manager": "rhettinger",
            "employment_type": "employee",
            "name": "Alexandre Vassalotti",
            "email": "alexandre@peadrop.com",
            "title": "BDFL",
            "cost_center": "Google",
            "country": null
        },
        "eliben": {
            "manager": "rhettinger",
            "employment_type": "employee",
            "name": "Eli Bendersky",
            "email": "",
            "title": "BDFL",
            "cost_center": "@google ",
            "country": "California"
        },
        "ZackerySpytz": {
            "manager": "rhettinger",
            "employment_type": "employee",
            "name": "Zackery Spytz",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "markshannon": {
            "manager": "rhettinger",
            "employment_type": "employee",
            "name": "Mark Shannon",
            "email": "mark@hotpy.org",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "ericsnowcurrently": {
            "manager": "rhettinger",
            "employment_type": "employee",
            "name": "Eric Snow",
            "email": "ericsnowcurrently@gmail.com",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "corona10": {
            "manager": "rhettinger",
            "employment_type": "employee",
            "name": "Dong-hee Na",
            "email": "donghee.na@python.org",
            "title": "BDFL",
            "cost_center": "@line",
            "country": "Seoul, South Korea"
        },
        "voidspace": {
            "manager": "rhettinger",
            "employment_type": "employee",
            "name": "Michael Foord",
            "email": "",
            "title": "BDFL",
            "cost_center": "Agile Abstractions",
            "country": "Northampton, UK"
        },
        "giampaolo": {
            "manager": "rhettinger",
            "employment_type": "employee",
            "name": "Giampaolo Rodola",
            "email": "g.rodola@gmail.com",
            "title": "BDFL",
            "cost_center": null,
            "country": "Italy"
        },
        "jcea": {
            "manager": "rhettinger",
            "employment_type": "employee",
            "name": "Jes\u00fas Cea",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "iritkatriel": {
            "manager": "pitrou",
            "employment_type": "employee",
            "name": "Irit Katriel",
            "email": "",
            "title": "BDFL",
            "cost_center": "Microsoft",
            "country": "London"
        },
        "ethanfurman": {
            "manager": "pitrou",
            "employment_type": "employee",
            "name": "Ethan Furman",
            "email": "ethan@stoneleaf.us",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "sandrotosi": {
            "manager": "pitrou",
            "employment_type": "employee",
            "name": "Sandro Tosi",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": "New York"
        },
        "jaraco": {
            "manager": "pitrou",
            "employment_type": "employee",
            "name": "Jason R. Coombs",
            "email": "jaraco@jaraco.com",
            "title": "BDFL",
            "cost_center": "Google",
            "country": "Pittsburgh, PA, USA"
        },
        "anthonybaxter": {
            "manager": "pitrou",
            "employment_type": "employee",
            "name": null,
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "collinw": {
            "manager": "pitrou",
            "employment_type": "employee",
            "name": "Collin Winter",
            "email": "",
            "title": "BDFL",
            "cost_center": "Google",
            "country": null
        },
        "ambv": {
            "manager": "pitrou",
            "employment_type": "employee",
            "name": "\u0141ukasz Langa",
            "email": "",
            "title": "BDFL",
            "cost_center": "@psf",
            "country": "Pozna\u0144, Poland"
        },
        "nvawda": {
            "manager": "pitrou",
            "employment_type": "employee",
            "name": null,
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "andresdelfino": {
            "manager": "pitrou",
            "employment_type": "employee",
            "name": "Andre Delfino",
            "email": "adelfino@gmail.com",
            "title": "BDFL",
            "cost_center": "Onapsis",
            "country": "Argentina"
        },
        "facundobatista": {
            "manager": "pitrou",
            "employment_type": "employee",
            "name": "Facundo Batista",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": "Argentina"
        },
        "shibturn": {
            "manager": "jackjansen",
            "employment_type": "employee",
            "name": "Richard Oudkerk",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "mhammond": {
            "manager": "jackjansen",
            "employment_type": "employee",
            "name": "Mark Hammond",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": "Melbourne, Australia"
        },
        "sjoerdmullender": {
            "manager": "jackjansen",
            "employment_type": "employee",
            "name": "Sjoerd Mullender",
            "email": "",
            "title": "BDFL",
            "cost_center": "@MonetDBSolutions @MonetDB ",
            "country": "Amsterdam"
        },
        "gustaebel": {
            "manager": "jackjansen",
            "employment_type": "employee",
            "name": "Lars Gust\u00e4bel",
            "email": "lars@gustaebel.de",
            "title": "BDFL",
            "cost_center": null,
            "country": "Germany"
        },
        "hyeshik": {
            "manager": "jackjansen",
            "employment_type": "employee",
            "name": "Hyeshik Chang",
            "email": "hyeshik@snu.ac.kr",
            "title": "BDFL",
            "cost_center": "Seoul National University",
            "country": "Seoul, South Korea"
        },
        "csabella": {
            "manager": "jackjansen",
            "employment_type": "employee",
            "name": "Cheryl Sabella",
            "email": "cheryl.sabella@gmail.com",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "isidentical": {
            "manager": "jackjansen",
            "employment_type": "employee",
            "name": "Batuhan Taskaya",
            "email": "batuhan@python.org",
            "title": "BDFL",
            "cost_center": "@fal-ai",
            "country": null
        },
        "brandtbucher": {
            "manager": "jackjansen",
            "employment_type": "employee",
            "name": "Brandt Bucher",
            "email": "brandt@python.org",
            "title": "BDFL",
            "cost_center": "@microsoft",
            "country": "Irvine, California"
        },
        "sobolevn": {
            "manager": "jackjansen",
            "employment_type": "employee",
            "name": "Nikita Sobolev",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "JulienPalard": {
            "manager": "jackjansen",
            "employment_type": "employee",
            "name": "Julien Palard",
            "email": "julien@palard.fr",
            "title": "BDFL",
            "cost_center": null,
            "country": "Paris, France"
        },
        "shihai1991": {
            "manager": "serhiy-storchaka",
            "employment_type": "employee",
            "name": "Hai Shi",
            "email": "shihai1992@gmail.com",
            "title": "BDFL",
            "cost_center": "PE",
            "country": "Hangzhou, China"
        },
        "akheron": {
            "manager": "serhiy-storchaka",
            "employment_type": "employee",
            "name": "Petri Lehtinen",
            "email": "petri@digip.org",
            "title": "BDFL",
            "cost_center": "@reaktor ",
            "country": "Turku, Finland"
        },
        "Fidget-Spinner": {
            "manager": "serhiy-storchaka",
            "employment_type": "employee",
            "name": "Ken Jin",
            "email": "kenjin@python.org",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "kumaraditya303": {
            "manager": "serhiy-storchaka",
            "employment_type": "employee",
            "name": "Kumar Aditya",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": "Earth"
        },
        "zestyping": {
            "manager": "serhiy-storchaka",
            "employment_type": "employee",
            "name": "Ka-Ping Yee",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": "Berkeley, California"
        },
        "jnoller": {
            "manager": "serhiy-storchaka",
            "employment_type": "employee",
            "name": "Jesse Noller",
            "email": "jnoller@gmail.com",
            "title": "BDFL",
            "cost_center": "The Humble Fungus",
            "country": "United States"
        },
        "cjerdonek": {
            "manager": "serhiy-storchaka",
            "employment_type": "employee",
            "name": "Chris Jerdonek",
            "email": "chris.jerdonek@gmail.com",
            "title": "BDFL",
            "cost_center": "Shotwell Labs, Inc.",
            "country": "San Francisco, CA"
        },
        "encukou": {
            "manager": "serhiy-storchaka",
            "employment_type": "employee",
            "name": "Petr Viktorin",
            "email": "encukou@gmail.com",
            "title": "BDFL",
            "cost_center": "Red Hat",
            "country": "Czech Republic"
        },
        "eric-s-raymond": {
            "manager": "serhiy-storchaka",
            "employment_type": "employee",
            "name": "Eric S. Raymond",
            "email": "esr@thyrsus.com",
            "title": "BDFL",
            "cost_center": null,
            "country": "Malvern, PA, USA"
        },
        "cloud-tester": {
            "manager": "serhiy-storchaka",
            "employment_type": "employee",
            "name": null,
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "sweeneyde": {
            "manager": "loewis",
            "employment_type": "employee",
            "name": "Dennis Sweeney",
            "email": "",
            "title": "BDFL",
            "cost_center": "The Ohio State University",
            "country": "Columbus, Ohio"
        },
        "jyasskin": {
            "manager": "loewis",
            "employment_type": "employee",
            "name": "Jeffrey Yasskin",
            "email": "jyasskin@gmail.com",
            "title": "BDFL",
            "cost_center": "@google",
            "country": "Portland, OR"
        },
        "cf-natali": {
            "manager": "loewis",
            "employment_type": "employee",
            "name": null,
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "tirkarthi": {
            "manager": "loewis",
            "employment_type": "employee",
            "name": "Karthikeyan Singaravelan",
            "email": "tir.karthi@gmail.com",
            "title": "BDFL",
            "cost_center": "Visa Inc.",
            "country": "Bangalore, India"
        },
        "gpolo": {
            "manager": "loewis",
            "employment_type": "employee",
            "name": "Guilherme Polo",
            "email": "ggpolo@gmail.com",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "zhangyangyu": {
            "manager": "loewis",
            "employment_type": "employee",
            "name": "Xiang Zhang",
            "email": "angwerzx@126.com",
            "title": "BDFL",
            "cost_center": "@pingcap ",
            "country": "Hangzhou, China"
        },
        "lysnikolaou": {
            "manager": "loewis",
            "employment_type": "employee",
            "name": "Lysandros Nikolaou",
            "email": "lisandrosnik@gmail.com",
            "title": "BDFL",
            "cost_center": "@Seafair ",
            "country": "Berlin"
        },
        "tpn": {
            "manager": "loewis",
            "employment_type": "employee",
            "name": "Trent Nelson",
            "email": "trent@trent.me",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        },
        "Mariatta": {
            "manager": "loewis",
            "employment_type": "employee",
            "name": "Mariatta Wijaya",
            "email": "",
            "title": "BDFL",
            "cost_center": "Google",
            "country": "Canada"
        },
        "taleinat": {
            "manager": "loewis",
            "employment_type": "employee",
            "name": "Tal Einat",
            "email": "",
            "title": "BDFL",
            "cost_center": null,
            "country": null
        }
    }
]
"""

data = json.loads(org_json)[0]
results = document.getElementById('results')
no_result = document.getElementById('no-results')
exact_match = document.getElementById('exact-match')
close_match = document.getElementById('close-match')
close_match_item = document.getElementById('close-match-item')

def search_handler(event, search_term:str='', focus_target_id:str=''):
    """Does something when the search button is activated.
    proccess module within thefuzz package seems like a great fit!
    https://github.com/seatgeek/thefuzz/blob/master/thefuzz/process.py#L175
    """
    # don't send the form over the network!
    event.preventDefault()
    if not search_term:
        search_term:str = document.getElementById("search").value
    else:
        document.getElementById("search").value = search_term
    # returns a list of tuples
    extracted:list[tuple[str,int]] = process.extractBests(search_term, data.keys(),
                                     score_cutoff=60, limit=5)
    results.innerHTML = ''
    """
    Different cases to think of:
    1. No results
    2. Exact match only
    3. Exact match and close matches
    4. Close matches only
    """
    if extracted:
        best_name, best_score = extracted[0]
        if best_score == 100:
            extracted.pop(0)
            exact_match_clone = exact_match.content.cloneNode(True)
            exact_match_clone.querySelectorAll('p')[0].textContent = best_name
            # populate the rest of the data
            exact_match_clone.getElementById('name').textContent = data[best_name]['name'] if data[best_name]['name'] else 'No name available'
            exact_match_clone.getElementById('title').textContent = data[best_name]['title'] if data[best_name]['title'] else 'No title available'
            exact_match_clone.getElementById('email').textContent = data[best_name]['email'] if data[best_name]['email'] else 'No email available'
            if 'manager' in data[best_name]:
                button = exact_match_clone.querySelectorAll('#manager button')[0]
                button.textContent = data[best_name]['manager']
                click_proxy = create_proxy(search_from_button)
                button.addEventListener("click", click_proxy)
            else:
                exact_match_clone.getElementById('manager').textContent = 'No manager'
            # TODO: move the find_directs call to setup()
            reports = find_directs(best_name)
            reports_out = exact_match_clone.getElementById('reports')
            if reports:
                list_of_reports = document.createElement('ol')
                for report in reports:
                    report_item = close_match_item.content.cloneNode(True)
                    report_button = report_item.querySelectorAll('button')[0]
                    report_button.textContent = report
                    click_proxy = create_proxy(search_from_button)
                    report_button.addEventListener("click", click_proxy)
                    list_of_reports.appendChild(report_item)
                reports_out.appendChild(list_of_reports)
            else:
                message = document.createElement('p')
                message.textContent = 'No reports'
                reports_out.appendChild(message)
            exact_match_clone.getElementById('cost-center').textContent = data[best_name]['cost_center'] if data[best_name]['cost_center'] else 'No cost center available'
            exact_match_clone.getElementById('country').textContent = data[best_name]['country'] if data[best_name]['country'] else 'No country available'
            exact_match_clone.getElementById('employment-type').textContent = data[best_name]['employment_type'] if data[best_name]['employment_type'] else 'No employment type available'
            results.appendChild(exact_match_clone)
            results.appendChild(exact_match_clone)
        # TODO: need to refactor if possible, prefer to not have 2 checks for extracted
        if extracted:
            close_match_clone = close_match.content.cloneNode(True)
            list_parent = close_match_clone.querySelectorAll('ul')[0]
            for name, score in extracted:
                close_match_item_clone = close_match_item.content.cloneNode(True)
                button = close_match_item_clone.querySelectorAll('button')[0]
                # button.textContent = f'{name}, {score}'
                button.textContent = name
                click_proxy = create_proxy(search_from_button)
                button.addEventListener("click", click_proxy)
                list_parent.appendChild(close_match_item_clone)
            results.appendChild(close_match_clone)
    else:
        results.appendChild(no_result.content.cloneNode(True))
    if focus_target_id:
        document.getElementById(focus_target_id).focus()

def search_from_button(event):
    """Search from the button."""
    search_term:str = event.target.textContent
    search_handler(event,
                   search_term=search_term,
                   focus_target_id='exact-match-heading')

def find_directs(handle:str) -> list[str]:
    """Find the direct reports for a given handle."""
    return [k for k, v in data.items() if v.get('manager', '') == handle]

def setup():
    """Setup the page."""
    # TODO: find all the directs for each handle and store in a dict
    # Set the listener to the callback
    document.getElementById("search-action").addEventListener("click",
                                                              create_proxy(search_handler))

setup()
