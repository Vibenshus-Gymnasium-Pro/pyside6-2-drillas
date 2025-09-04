# [[file:README.org::*Udvikling af logik][Udvikling af logik:1]]
# Dette er et modul til oversættelse mellem almindelige sprog og røversprog

def oversaet_til_roeversprog(inputtekst):

    vokaler = "aeiouyæøåAEIOUYÆØÅ"
    outputtekst = ""

    for bogstav in inputtekst:
        if bogstav.isalpha() and bogstav not in vokaler:
            outputtekst += bogstav + "o" + bogstav.lower()
        else:
            outputtekst += bogstav

    return outputtekst


def oversaet_fra_roeversprog_til_andet_sprog(inputtekst):

    vokaler = "aeiouyæøåAEIOUYÆØÅ"
    outputtekst = ""
    i = 0

    while i < len(inputtekst):
        bogstav = inputtekst[i]

        if bogstav.isalpha() and bogstav not in vokaler:
            if i + 2 < len(inputtekst):
                if inputtekst[i+1] == "o" and inputtekst[i+2].lower() == bogstav.lower():
                    outputtekst += bogstav
                    i += 3
                else:
                    return "Fejl: Ugyldigt røversprog ved position " + str(i) + "."
            else:
                return "Fejl: Ufuldstændigt røversprog ved slutningen af teksten."
        else:
            outputtekst += bogstav
            i += 1

    return outputtekst