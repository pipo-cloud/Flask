# Flask Sentiment Analysis API

Eine Flask-API zur Durchführung von Sentiment-Analyse auf Textinhalten mit TextBlob.

## Installation

1. Python Virtual Environment erstellen:
```bash
python -m venv venv
```

2. Virtual Environment aktivieren:
   - **Windows (PowerShell):**
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD):**
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

## Anwendung starten

```bash
python app.py
```

Die API ist dann unter `http://localhost:5000` verfügbar.

## Endpoints

### POST /analyze
Analysiert den Sentiment eines Textes.

**Request:**
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "Ich liebe diese großartige Lösung!"}'
```

**Beispiel JSON Body:**
```json
{
  "text": "Das ist ein fantastischer Tag!"
}
```

**Response:**
```json
{
  "sentiment": "Positiv",
  "polarity": 0.85,
  "subjectivity": 0.75,
  "text": "Das ist ein fantastischer Tag!"
}
```

### GET /health
Health Check Endpoint.

**Request:**
```bash
curl http://localhost:5000/health
```

**Response:**
```json
{
  "status": "ok"
}
```

## Sentiment-Klassifizierung

- **Positiv**: polarity > 0.1
- **Neutral**: -0.1 ≤ polarity ≤ 0.1
- **Negativ**: polarity < -0.1

### Rückgabewerte erklären:
- `sentiment`: Die Klassifizierung ("Positiv", "Neutral", "Negativ")
- `polarity`: Wert zwischen -1 (sehr negativ) und 1 (sehr positiv)
- `subjectivity`: Wert zwischen 0 (sehr objektiv) und 1 (sehr subjektiv)
- `text`: Der analysierte Text

## Beispiele

### Positiver Text
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "Das ist hervorragend und fantastisch!"}'
```

**Response:**
```json
{
  "sentiment": "Positiv",
  "polarity": 0.95,
  "subjectivity": 0.9,
  "text": "Das ist hervorragend und fantastisch!"
}
```

### Negativer Text
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "Das ist furchtbar und schlecht."}'
```

**Response:**
```json
{
  "sentiment": "Negativ",
  "polarity": -0.9,
  "subjectivity": 0.75,
  "text": "Das ist furchtbar und schlecht."
}
```

### Neutraler Text
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "Das ist ein Tisch."}'
```

**Response:**
```json
{
  "sentiment": "Neutral",
  "polarity": 0.0,
  "subjectivity": 0.0,
  "text": "Das ist ein Tisch."
}
```

## Fehlerverwaltung

Die API gibt aussagekräftige Fehlermeldungen zurück:

- **400 Bad Request**: Wenn `text` Feld fehlt oder leer ist
- **500 Internal Server Error**: Bei unerwarteten Fehlern

**Beispiel Fehlermeldung:**
```json
{
  "error": "Missing 'text' field in request body"
}
```

## Hinweise

- Die Sentiment-Analyse funktioniert auf Englisch optimaler, funktioniert aber auch auf anderen Sprachen
- TextBlob verwendet unter der Haube NLTK für die Analyse
- Für längere Texte können die Ergebnisse weniger präzise sein
