# WordleIta-Discord-Bot

Bot ispirato da PAr(it)le di Pietroppeter
https://pietroppeter.github.io/wordle-it/

Discord bot per giocare a Wordle con i vocaboli italiani

### Come installarlo
Segui le dipendenze del file "requirement.txt"
Creare un file .env da mettere nella root principale con "TOKEN={token}"
Runnare il bot

DA  TESTARE(in caso desse errore per mancanza di un file data.json)
creare un file data.json sempre nella root directory
e mettere il seguente codice

    {  
    "wordle": [  
        {  
            "id": il tuo id discord,  
			  "nickname": "il tuo nickname",  
			  "punti": 0  
		}
		]  
	}

## Comandi
### ;wordle  
Permette di giocare al gioco, basta scrivere una parola da 5 lettere successivamente alla comparsa della tabella di gioco.
(Possibilità di bug)

 - [ ] possibilità di usare ;wordle all'avvio di una partita in esecuzione dello stesso utente
 - [ ] La partita non termina (realmente ps: vedi console "debug" ) quando si indovina la parola prima della sesta casella

## ;classifica
Ritorna un embed con tutta la lista dei giocatori (che hanno in precedenza giocato e vinto) sortato in base ai punti (dal piu grande al piu piccolo)

## ;info
Ritorna un embed con l'immagine di come giocare a wordle preso dal wordle di Pietroppeter

:)