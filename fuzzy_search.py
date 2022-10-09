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
    {"gvanrossum": 
        {
            "employment_type": "employee",
            "name": "Guido van Rossum",
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "freddrake": 
        {
            "manager": "gvanrossum",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "birkenfeld": 
        {
            "manager": "gvanrossum",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "vstinner": 
        {
            "manager": "gvanrossum",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "benjaminp": 
        {
            "manager": "gvanrossum",
            "employment_type": "employee", 
            "name": "Benjamin", 
            "email": "test@test.com",
            "title": "Product Manager",
            "cost_center": "1234",
            "country": "USA"
        },
    "rhettinger": 
        {
            "manager": "gvanrossum",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "pitrou": 
        {
            "manager": "gvanrossum",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "jackjansen": 
        {
            "manager": "gvanrossum",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "serhiy-storchaka": 
        {
            "manager": "gvanrossum",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "loewis": 
        {
            "manager": "gvanrossum",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "tim-one": 
        {
            "manager": "freddrake",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "akuchling": 
        {
            "manager": "freddrake",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "warsaw": 
        {
            "manager": "freddrake",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "brettcannon": 
        {
            "manager": "freddrake",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "nnorwitz": 
        {
            "manager": "freddrake",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "mdickinson": 
        {
            "manager": "freddrake",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "tiran": 
        {
            "manager": "freddrake",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "bitdancer": 
        {
            "manager": "freddrake",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "ezio-melotti": 
        {
            "manager": "freddrake",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "gpshead": 
        {
            "manager": "freddrake",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "jeremyhylton": 
        {
            "manager": "birkenfeld",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "vsajip": 
        {
            "manager": "birkenfeld",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "orsenthil": 
        {
            "manager": "birkenfeld",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "terryjreedy": 
        {
            "manager": "birkenfeld",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "gward": 
        {
            "manager": "birkenfeld",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "merwok": 
        {
            "manager": "birkenfeld",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "zooba": 
        {
            "manager": "birkenfeld",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "ned-deily": 
        {
            "manager": "birkenfeld",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "ncoghlan": 
        {
            "manager": "birkenfeld",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "pablogsal": 
        {
            "manager": "birkenfeld",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "1st1": 
        {
            "manager": "vstinner",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "ronaldoussoren": 
        {
            "manager": "vstinner",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "berkerpeksag": 
        {
            "manager": "vstinner",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "doerwalter": 
        {
            "manager": "vstinner",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "kbkaiser": 
        {
            "manager": "vstinner",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "amauryfa": 
        {
            "manager": "vstinner",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "zware": 
        {
            "manager": "vstinner",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "ericvsmith": 
        {
            "manager": "vstinner",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "asvetlov": 
        {
            "manager": "vstinner",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "vadmium": 
        {
            "manager": "vstinner",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "erlend-aasland": 
        {
            "manager": "benjaminp",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "briancurtin": 
        {
            "manager": "benjaminp",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "skrah": 
        {
            "manager": "benjaminp",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "florentx": 
        {
            "manager": "benjaminp",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "abalkin": 
        {
            "manager": "benjaminp",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "Yhg1s": 
        {
            "manager": "benjaminp",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "larryhastings": 
        {
            "manager": "benjaminp",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "malemburg": 
        {
            "manager": "benjaminp",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "nascheme": 
        {
            "manager": "benjaminp",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "methane": 
        {
            "manager": "benjaminp",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "doko42": 
        {
            "manager": "rhettinger",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "avassalotti": 
        {
            "manager": "rhettinger",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "eliben": 
        {
            "manager": "rhettinger",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "ZackerySpytz": 
        {
            "manager": "rhettinger",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "markshannon": 
        {
            "manager": "rhettinger",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "ericsnowcurrently": 
        {
            "manager": "rhettinger",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "corona10": 
        {
            "manager": "rhettinger",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "voidspace": 
        {
            "manager": "rhettinger",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "giampaolo": 
        {
            "manager": "rhettinger",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "jcea": 
        {
            "manager": "rhettinger",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "iritkatriel": 
        {
            "manager": "pitrou",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "ethanfurman": 
        {
            "manager": "pitrou",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "sandrotosi": 
        {
            "manager": "pitrou",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "jaraco": 
        {
            "manager": "pitrou",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "anthonybaxter": 
        {
            "manager": "pitrou",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "collinw": 
        {
            "manager": "pitrou",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "ambv": 
        {
            "manager": "pitrou",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "nvawda": 
        {
            "manager": "pitrou",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "andresdelfino": 
        {
            "manager": "pitrou",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "facundobatista": 
        {
            "manager": "pitrou",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "shibturn": 
        {
            "manager": "jackjansen",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "mhammond": 
        {
            "manager": "jackjansen",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "sjoerdmullender": 
        {
            "manager": "jackjansen",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "gustaebel": 
        {
            "manager": "jackjansen",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "hyeshik": 
        {
            "manager": "jackjansen",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "csabella": 
        {
            "manager": "jackjansen",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "isidentical": 
        {
            "manager": "jackjansen",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "brandtbucher": 
        {
            "manager": "jackjansen",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "sobolevn": 
        {
            "manager": "jackjansen",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "JulienPalard": 
        {
            "manager": "jackjansen",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "shihai1991": 
        {
            "manager": "serhiy-storchaka",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "akheron": 
        {
            "manager": "serhiy-storchaka",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "Fidget-Spinner": 
        {
            "manager": "serhiy-storchaka",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "kumaraditya303": 
        {
            "manager": "serhiy-storchaka",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "zestyping": 
        {
            "manager": "serhiy-storchaka",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "jnoller": 
        {
            "manager": "serhiy-storchaka",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "cjerdonek": 
        {
            "manager": "serhiy-storchaka",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "encukou": 
        {
            "manager": "serhiy-storchaka",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "eric-s-raymond": 
        {
            "manager": "serhiy-storchaka",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "cloud-tester": 
        {
            "manager": "serhiy-storchaka",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "sweeneyde": 
        {
            "manager": "loewis",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "jyasskin": 
        {
            "manager": "loewis",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "cf-natali": 
        {
            "manager": "loewis",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "tirkarthi": 
        {
            "manager": "loewis",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "gpolo": 
        {
            "manager": "loewis",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "zhangyangyu": 
        {
            "manager": "loewis",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "lysnikolaou": 
        {
            "manager": "loewis",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "tpn": 
        {
            "manager": "loewis",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "Mariatta": 
        {
            "manager": "loewis",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
        },
    "taleinat": 
        {
            "manager": "loewis",
            "employment_type": "employee", 
            "name": "Guido van Rossum", 
            "email": "test@test.com",
            "title": "BDFL",
            "cost_center": "1234",
            "country": "Netherlands"
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
            exact_match_clone.getElementById('name').textContent = data[best_name]['name']
            exact_match_clone.getElementById('title').textContent = data[best_name]['title']
            exact_match_clone.getElementById('email').textContent = data[best_name]['email']
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
            exact_match_clone.getElementById('cost-center').textContent = data[best_name]['cost_center']
            exact_match_clone.getElementById('country').textContent = data[best_name]['country']
            exact_match_clone.getElementById('employment-type').textContent = data[best_name]['employment_type']
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
