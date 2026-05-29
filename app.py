from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)


@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Analyzes the sentiment of a provided text using TextBlob.
    
    Expected JSON body:
    {
        "text": "your text here"
    }
    
    Returns:
    {
        "sentiment": "Positiv", "Neutral", or "Negativ",
        "polarity": float between -1 and 1,
        "subjectivity": float between 0 and 1
    }
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({"error": "Missing 'text' field in request body"}), 400
        
        text = data['text'].strip()
        
        if not text:
            return jsonify({"error": "Text field cannot be empty"}), 400
        
        # Perform sentiment analysis using TextBlob
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        # Classify sentiment based on polarity
        if polarity > 0.1:
            sentiment = "Positiv"
        elif polarity < -0.1:
            sentiment = "Negativ"
        else:
            sentiment = "Neutral"
        
        return jsonify({
            "sentiment": sentiment,
            "polarity": polarity,
            "subjectivity": subjectivity,
            "text": text
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
