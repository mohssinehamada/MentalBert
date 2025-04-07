import re
import random

class SimpleMentalHealthAnalyzer:
    """
    A simple mental health analyzer that doesn't rely on external libraries.
    This is a placeholder for demonstration purposes.
    """
    
    def __init__(self):
        # Crisis keywords that should trigger immediate support responses
        self.crisis_keywords = [
            'suicide', 'kill myself', 'end my life', 'want to die', 'wanna die',
            'kill me', 'better off dead', 'no reason to live', 'can\'t go on'
        ]
        
        # Severe negative mental health indicators
        self.severe_negative_indicators = [
            'hopeless', 'worthless', 'empty', 'desperate', 'trapped',
            'burden', 'pain', 'hurt', 'alone', 'lonely', 'never get better'
        ]
        
        # Regular negative keywords
        self.negative_keywords = [
            'sad', 'depressed', 'anxious', 'worried', 'scared',
            'stressed', 'angry', 'upset', 'tired', 'exhausted',
            'frustrated', 'overwhelmed', 'confused', 'lost'
        ]
        
        # Positive keywords
        self.positive_keywords = [
            'happy', 'good', 'great', 'awesome', 'wonderful',
            'excited', 'peaceful', 'calm', 'relaxed', 'blessed',
            'grateful', 'thankful', 'loved', 'supported', 'strong'
        ]
    
    def is_in_crisis(self, text):
        """Check if the text contains any crisis keywords."""
        text = text.lower()
        return any(keyword in text for keyword in self.crisis_keywords)

    def analyze_text(self, text):
        """
        Analyze text for sentiment and mental health indicators.
        Returns a dictionary with sentiment and mental health scores.
        """
        text = text.lower()
        
        # Crisis detection - immediately return severe scores
        if self.is_in_crisis(text):
            return {
                'sentiment': 0.0,  # Lowest possible sentiment
                'mental_health_indicator': 0.1,  # Critical mental health score
                'crisis': True,
                'response': self._get_crisis_response()
            }
        
        # Count occurrences of different types of keywords
        severe_negative_count = sum(1 for word in self.severe_negative_indicators if word in text)
        negative_count = sum(1 for word in self.negative_keywords if word in text)
        positive_count = sum(1 for word in self.positive_keywords if word in text)
        
        # Calculate sentiment (0 to 1)
        total_sentiment_words = positive_count + negative_count + severe_negative_count
        if total_sentiment_words == 0:
            sentiment = 0.5  # Neutral if no sentiment words found
        else:
            # Severe negative words count double
            sentiment = positive_count / (positive_count + negative_count + (2 * severe_negative_count))
        
        # Calculate mental health indicator (0 to 1)
        # Severe negative indicators have more impact
        total_indicators = positive_count + negative_count + (3 * severe_negative_count)
        if total_indicators == 0:
            mental_health = 0.5  # Neutral if no indicators found
        else:
            mental_health = max(0.1, min(1.0, 
                (positive_count) / (positive_count + negative_count + (3 * severe_negative_count))
            ))
        
        return {
            'sentiment': sentiment,
            'mental_health_indicator': mental_health,
            'crisis': False
        }

    def _get_crisis_response(self):
        """Return an appropriate response for crisis situations."""
        return (
            "I'm very concerned about what you're saying and I want you to know that your life has value. "
            "Please reach out for immediate help:\n\n"
            "1. National Suicide Prevention Lifeline (US): 988 or 1-800-273-8255\n"
            "2. Crisis Text Line: Text HOME to 741741\n"
            "3. Emergency Services: 911 (US) or your local emergency number\n\n"
            "Would you be willing to talk to a counselor or mental health professional? "
            "They are trained to help and want to support you through this."
        )

# Test the analyzer
if __name__ == "__main__":
    analyzer = SimpleMentalHealthAnalyzer()
    
    test_messages = [
        "I am feeling really happy today! Everything is going great.",
        "I'm feeling a bit anxious about my upcoming presentation.",
        "I've been feeling down lately and don't know why.",
        "I'm practicing mindfulness and meditation to improve my mental health.",
        "I'm feeling overwhelmed with work and need to take a break."
    ]
    
    print("Simple Mental Health Analyzer Test")
    print("-" * 50)
    
    for message in test_messages:
        results = analyzer.analyze_text(message)
        print(f"\nMessage: '{message}'")
        print(f"Sentiment: {(results['sentiment'] * 100):.2f}% positive")
        print(f"Mental Health Indicator: {(results['mental_health_indicator'] * 100):.2f}%")
        print(f"Crisis: {results['crisis']}")
        print(f"Response: {results['response']}") 