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
    outputtekst = "Her skal røversproget fjernes og almindeligt sprog skal returneres.\nGiv gerne fejlmeddelelser, hvis røversproget ikke er korrekt."
    return outputtekst
# Udvikling af logik:1 ends here
