# FastAPI Applicazione: Cataloghi e Premi

Questa applicazione utilizza il framework FastAPI per fornire un'API per la gestione di cataloghi e premi. È progettata per recuperare premi da cataloghi specifici, con funzionalità di filtraggio e paginazione.

## Struttura del Progetto

- `main.py`: Il file principale che contiene l'implementazione dell'API.
- `models/CatalogsMock.py`: Un modulo che simula un database di cataloghi.
- `models/Prize.py`: Un modulo che definisce il modello `Prize` utilizzando Pydantic.

## Dipendenze
fastapi,uvicorn,pytest

```bash
pip install fastapi uvicorn pytest
```
## Utilizzo

### Avvia l'applicazione: 
```bash
python -m uvicorn sources.Main:app --reload 
```

### Endpoint API:
Percorso principale: GET / - Restituisce un semplice messaggio "Hello, World".
Elenca premi: GET /api/catalogs/{catalog_id}/prizes
Parametro del percorso:
catalog_id: ID del catalogo per cui recuperare i premi.
Parametri di query opzionali (possono essere combinati):
filter.id: Filtra i premi per ID (valore intero).
filter.description: Filtra i premi per descrizione (valore stringa).
pagination.page: Numero di pagina per il recupero dei premi (default: 1).
pagination.per_page: Numero di premi per pagina (default: 10).

## Test unitari
### catalogs mock
```bash
python -m pytest tests/test_catalogs_mock.py
```
### api call
```bash
python -m pytest tests/test_apicall.py
```
