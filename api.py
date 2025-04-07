from flask import Flask, request, jsonify
from flask_cors import CORS
# Update the import to use the correct path
from simple_analyzer import SimpleMentalHealthAnalyzer

app = Flask(__name__)
# Enable CORS for all routes with all methods
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Initialize the analyzer
analyzer = SimpleMentalHealthAnalyzer()

@app.route('/analyze', methods=['GET', 'POST', 'OPTIONS'])
def analyze_text():
    # Handle preflight request
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        return response
        
    # Handle GET request with a friendly message
    if request.method == 'GET':
        return jsonify({
            'message': 'Welcome to the MindEase API. Please use POST method to analyze text.',
            'usage': {
                'method': 'POST',
                'endpoint': '/analyze',
                'body': {'message': 'Your text here'}
            }
        })

    # Handle POST request
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided'}), 400
        
        message = data['message']
        print(f"Received message: {message}")  # Add logging
        
        # Analyze the message
        results = analyzer.analyze_text(message)
        print(f"Analysis results: {results}")  # Add logging
        
        # If this is a crisis situation, return the crisis response
        if results.get('crisis', False):
            return jsonify({
                'response': results['response'],
                'analysis': {
                    'sentiment': results['sentiment'],
                    'mental_health_indicator': results['mental_health_indicator'],
                    'crisis': True
                },
                'crisis': True
            })
        
        # Generate a response based on the analysis
        sentiment = results['sentiment']
        mental_health = results['mental_health_indicator']
        
        # Create a response based on the analysis
        if sentiment > 0.7:
            response = "I'm glad to hear you're feeling positive! What's contributing to these good feelings today?"
        elif sentiment < 0.3:
            response = "I hear that you're feeling down. It's okay to feel this way. Would you like to talk more about what's on your mind?"
        else:
            response = "I understand you're sharing your feelings. Can you tell me more about what's going on?"
        
        # Add mental health insights
        if mental_health < 0.4:
            response += " I notice you might be experiencing some challenges. Remember, it's okay to seek support when needed."
        
        return jsonify({
            'response': response,
            'analysis': {
                'sentiment': sentiment,
                'mental_health_indicator': mental_health,
                'crisis': False
            }
        })
    
    except Exception as e:
        print(f"Error processing request: {str(e)}")  # Add logging
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting API server on port 8080...")  # Add logging
    app.run(debug=True, port=8080, host='0.0.0.0')