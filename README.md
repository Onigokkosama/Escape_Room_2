# Avventura-Testuale-Python-
- Motore di avventura testuale modulare
- Supporto multi-lingua (IT/EN)
- Separazione chiara tra logica, dati e rendering
- Sistema di eventi dichiarativo.

## Obiettivi del progetto

- Creare un motore modulare per avventure testuali in Python  
- Separare chiaramente **logica**, **stato**, **rendering** e **dati**  
- Supportare la **localizzazione** (i18n) per italiano e inglese  
- Implementare un **sistema di eventi dichiarativo** con trigger, condizioni ed effetti  
- Rendere il motore facilmente estendibile per nuove stanze, oggetti, comandi e lingue

## Struttura dei moduli

| Modulo / File         | Responsabilità                                                | Stato         |
|----------------------|---------------------------------------------------------------|---------------|
| `main.py`            | Entry point, coordina il game loop                             | In costruzione |
| `game_engine.py`     | Gestisce loop principale, coordina moduli                     | In costruzione |
| `game_state.py`      | Memorizza stato di gioco (stanza, inventario, flag, lingua)   | In costruzione |
| `world_loader.py`    | Carica il JSON del mondo e costruisce oggetti interni         | In costruzione |
| `command_handler.py` | Interpreta input player e aggiorna GameState                  | In costruzione |
| `event_manager.py`   | Gestisce trigger, valuta condizioni, applica effetti          | In costruzione |
| `renderer.py`        | Mostra output e risolve chiavi per la lingua selezionata      | In costruzione |
| `data/world.json`    | Definizione delle stanze, oggetti, eventi                     | In costruzione |
| `data/locale/it.json`| Traduzioni italiane                                           | In costruzione |
| `data/locale/en.json`| Traduzioni inglesi                                           | In costruzione |

---

## Funzionalità previste

- Ciclo di gioco modulare e chiaro  
- Interpretazione dei comandi del giocatore separata dal motore  
- Sistema di eventi dichiarativo (trigger → condizione → effetto → messaggio)  
- Supporto multi-lingua tramite file di localizzazione (IT/EN)  
- Facilità di aggiunta di nuove stanze, oggetti ed eventi senza modificare il motore 
