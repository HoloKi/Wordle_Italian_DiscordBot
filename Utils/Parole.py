import discord
import logging

logger = logging.getLogger('wordle')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='wordle.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))

WHITE_MEDIUM_BLOCK = "<:white_medium_square:943849495861534790>"
EMOJI_CODES = {
    "green": {
        "a": "<:1f1e6:943856476282298368>",
        "b": "<:1f1e7:943856476387180614>",
        "c": "<:1f1e8:943856476131299329>",
        "d": "<:1f1e9:943856476760461322>",
        "e": "<:1f1ea:943856476399751208>",
        "f": "<:1f1eb:943856476538159124>",
        "g": "<:1f1ec:943856476299067462>",
        "h": "<:1f1ed:943856476345229312>",
        "i": "<:1f1ee:943856476265517146>",
        "j": "<:1f1ef:943856476441686096>",
        "k": "<:1f1f0:943856476336848916>",
        "l": "<:1f1f1:943856476303273985>",
        "m": "<:1f1f2:943856476257148981>",
        "n": "<:1f1f3:943856476273926184>",
        "o": "<:1f1f4:943856476420718672>",
        "p": "<:1f1f5:943856476412342282>",
        "q": "<:1f1f6:943856476437491742>",
        "r": "<:1f1f7:943856476282306581>",
        "s": "<:1f1f8:943856476009676831>",
        "t": "<:1f1f9:943856476429107200>",
        "u": "<:1f1fa:943856476290682890>",
        "v": "<:1f1fb:943856476416516116>",
        "w": "<:1f1fc:943856475992911903>",
        "x": "<:1f1fd:943856476382978098>",
        "y": "<:1f1fe:943856476336832532>",
        "z": "<:1f1ff:943856476437499954>",
    },
    "yellow": {
        "a": "<:1f1e6:943856348783845466>",
        "b": "<:1f1e7:943856348347654146>",
        "c": "<:1f1e8:943856348486045697>",
        "d": "<:1f1e9:943856348406353981>",
        "e": "<:1f1ea:943856348695769118>",
        "f": "<:1f1eb:943856348729327666>",
        "g": "<:1f1ec:943856348720922624>",
        "h": "<:1f1ed:943856348800618496>",
        "i": "<:1f1ee:943856348737724416>",
        "j": "<:1f1ef:943856348842586142>",
        "k": "<:1f1f0:943856348423155793>",
        "l": "<:1f1f1:943856348439908384>",
        "m": "<:1f1f2:943856348444119051>",
        "n": "<:1f1f3:943856348683178004>",
        "o": "<:1f1f4:943856348754501694>",
        "p": "<:1f1f5:943856349287186473>",
        "q": "<:1f1f6:943856348720951347>",
        "r": "<:1f1f7:943856348741910628>",
        "s": "<:1f1f8:943856348695760916>",
        "t": "<:1f1f9:943856349001973772>",
        "u": "<:1f1fa:943856348448321578>",
        "v": "<:1f1fb:943856348897116170>",
        "w": "<:1f1fc:943856348607676449>",
        "x": "<:1f1fd:943856348548964373>",
        "y": "<:1f1fe:943856348649644063>",
        "z": "<:1f1ff:943856348800647218>",
    },
    "gray": {
        "a": "<:1f1e6:943881512548462623>",
        "b": "<:1f1e7:943881512942719026>",
        "c": "<:1f1e8:943881512892383242>",
        "d": "<:1f1e9:943881512628158514>",
        "e": "<:1f1ea:943881512691052664>",
        "f": "<:1f1eb:943881512758153236>",
        "g": "<:1f1ec:943881512716210176>",
        "h": "<:1f1ed:943881512607158322>",
        "i": "<:1f1ee:943881512644923462>",
        "j": "<:1f1ef:943881512292610219>",
        "k": "<:1f1f0:943881512313577554>",
        "l": "<:1f1f1:943881512665907220>",
        "m": "<:1f1f2:943881512812695552>",
        "n": "<:1f1f3:943881512619769876>",
        "o": "<:1f1f4:943881512376475770>",
        "p": "<:1f1f5:943881512678473738>",
        "q": "<:1f1f6:943881512598798396>",
        "r": "<:1f1f7:943881512653316136>",
        "s": "<:1f1f8:943881512602959872>",
        "t": "<:1f1f9:943881512598794270>",
        "u": "<:1f1fa:943881512250667109>",
        "v": "<:1f1fb:943881512535883836>",
        "w": "<:1f1fc:943881512590397480>",
        "x": "<:1f1fd:943881512577798214>",
        "y": "<:1f1fe:943881512724594789>",
        "z": "<:1f1ff:943881512816869396>",
    },
}

def parola_esistente(parola):
        dizionario = open(r'dict\big5.txt', "r")
        for line in dizionario:
            if parola in line:
                dizionario.close()
                return True
        dizionario.close()
        return False

    # Funzione che mi setta a bianco una linea
def blank_block():
    return f"{WHITE_MEDIUM_BLOCK * 5}"

    # Funzione che modifica le parole e le inserisce
def posiziona_parola(parola, controllo):
    # anima
    # a -> [EMOJI_CODES['gray']["a"]]
    num = 0
    # Array di supporto
    pos = []
    for k in range(5):
        pos.append('gray')
    # controllo parola[i] -> posso usare la funzione controllo.find() ma torna un array
    for i in range(5):
        # mi sposto con g
        for g in parola:
            if g == controllo[i]:
                pos[num] = 'yellow'
            num += 1
        num = 0

    if controllo[0] == parola[0]: pos[0] = 'green'
    if controllo[1] == parola[1]: pos[1] = 'green'
    if controllo[2] == parola[2]: pos[2] = 'green'
    if controllo[3] == parola[3]: pos[3] = 'green'
    if controllo[4] == parola[4]: pos[4] = 'green'
    #for i in range(5):
    #    print(pos[i])
    # Vado a prendere in EMOJI_CODES['gray']["a"] il valore in emoji di a di tipo gray
    return F"{EMOJI_CODES[pos[0]][parola[0]]}{EMOJI_CODES[pos[1]][parola[1]]}" \
           F"{EMOJI_CODES[pos[2]][parola[2]]}{EMOJI_CODES[pos[3]][parola[3]]}" \
           F"{EMOJI_CODES[pos[4]][parola[4]]}\n"

# Funzione che genera da 0 i blocchi quindi tutti bianchi
# TODO togliere titolo dalla funzione, serve per debug
def genera_blocchi():
    embed = discord.Embed(title="Wordle Discord")
    embed.description = "\n".join([blank_block()] * 6)
    embed.set_footer(text="Wordle per principianti con un dizionario del cazzo.")
    return embed

# aggiorna l'embed del worlde
# TODO posso far si che aggiorni il primo messaggio senza continui spam
def update_embed(parola, linea, arr, controllo):
    logger.info(f'parola inserita: {parola}, da controllare: {controllo} ')
    testo = ""
    # mi salvo nelle varie righe la parola
    arr.append(parola)
    embed = discord.Embed(title='Wordle Discord')
    for i in range(linea + 1):
        # print(f'posizione -> parola {i}')
        testo += f'{posiziona_parola(arr[i], controllo)}'
    testo += "\n".join([blank_block()] * (5 - int(linea)))
    #print(testo)
    print("debug")
    embed.description = testo
    pos=linea
    # embed.description = f'{self.posiziona_parola(parola)}' + "\n".join([self.blank_block()] * 5)
    embed.set_footer(text=f'Hai usato la parola: "{parola}". Tentativo n {pos+1}/6')
    return embed