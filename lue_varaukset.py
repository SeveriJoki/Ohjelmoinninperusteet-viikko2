"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""
from datetime import datetime
def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    # Tulostetaan varaus konsoliin
    varaus = varaus.split('|')

    varausnumero = int(varaus[0])
    varaaja = str(varaus[1])
    paivamaara = datetime.strptime(varaus[2], "%Y-%m-%d").date()
    aloitusaika =  datetime.strptime(varaus[3], "%H:%M").time()
    tuntimaara = int(varaus[4])
    tuntihinta = float(varaus[5])
    kokonaishinta = tuntimaara * tuntihinta
    maksettu = bool(varaus[6])
    kohde = str(varaus[7])
    puhelin = int(varaus[8])
    sahkoposti = str(varaus[9])

    print(f"Varausnumero: {varausnumero}")
    print(f"Varaaja: {varaaja}")
    print(f"Päivämäärä: {paivamaara}")
    print(f"Aloitusaika: {aloitusaika}")
    print(f"Tuntimäärä: {tuntimaara}")
    print(f"Tuntihinta: {tuntihinta}€".replace('.', ','))
    print(f"Kokonaishinta: {kokonaishinta}€".replace('.', ','))
    print(f"Maksettu: {maksettu}")
    print(f"Kohde: {kohde}")
    print(f"Puhelin: {puhelin}")
    print(f"Sähköposti: {sahkoposti}")
    # Kokeile näitä
    #print(varaus.split('|'))
    #varausId = varaus.split('|')[0]
    #print(varausId)
    #print(type(varausId))
    """
    Edellisen olisi pitänyt tulostaa numeron 123, joka
    on oletuksena tekstiä.

    Voit kokeilla myös vaihtaa kohdan [0] esim. seuraavaksi [1]
    ja testata mikä muuttuu
    """

if __name__ == "__main__":
    main()