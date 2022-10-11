import json

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

manual_data = json.loads(org_json)[0]
# read the json file and convert it to a dictionary
with open('result_from_query.json', 'r') as f:
    github_data = json.load(f)[0]["data"]

result = {}
for k in manual_data.keys():
    result[k] = {**manual_data[k], **github_data[k]}

with open('python-org-data.json', 'w') as f:
    json.dump([result], f, indent=4)
# print(result)
