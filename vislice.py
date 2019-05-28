import bottle
import model

vislice = model.Vislice("stanje.json")
#id = vislice.nova_igra()
#igra, stanje = vislice.igre[id]
#vislice.ugibaj(id, "A")
#vislice.ugibaj(id, "C")
#vislice.ugibaj(id, "R")
#vislice.ugibaj(id, "U")

@bottle.get("/")
def index():
    return bottle.template("index.html")

#@bottle.get("/igra/")
#def testigra():
 #   return bottle.template("igra.html", id_igra = id, igra = igra, stanje = stanje)

@bottle.get("/img/<ime>")
def slike(ime):
    return bottle.static_file(ime, root = "img")


#cookies:

@bottle.post("/nova_igra/")
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie("id_igre", str(id_igre), path= "/")
    bottle.redirect("/igra/")


@bottle.get("/igra/")
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie("id_igre"))
    igra, stanje = vislice.igre[id_igre]
    return bottle.template("igra.html", id_igre = id_igre, igra = igra, stanje = stanje)



@bottle.post("/igra/")
def ugibaj():
    id_igre = int(bottle.request.get_cookie("id_igre"))
    crka = bottle.request.forms.getunicode("crka")
    vislice.ugibaj(id_igre, crka)
    bottle.redirect("/igra/")



bottle.run(reloader=True, debug=True)


