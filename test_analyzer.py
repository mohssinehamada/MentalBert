from mindgpt.core.analyzer import MentalHealthAnalyzer

def main():
    # Initialize the analyzer
    analyzer = MentalHealthAnalyzer()
    
    # Test texts
    texts = [
        "I'm feeling very happy and optimistic today!",
        "I've been feeling down and anxious lately, and I don't know why."
    ]
    
    # Analyze each text
    for text in texts:
        print(f"\nAnalyzing text: {text}")
        results = analyzer.analyze_text(text)
        print("Results:")
        print(f"- Sentiment score: {results['sentiment']:.3f}")
        print(f"- Mental health indicator: {results['mental_health_indicator']:.3f}")

if __name__ == "__main__":
    main() 