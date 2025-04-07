import os
import sys

# Add the MindGPT directory to the Python path
mindgpt_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "MindGPT")
sys.path.insert(0, mindgpt_dir)

try:
    from mindgpt.core.analyzer import MentalHealthAnalyzer
    print("Successfully imported MentalHealthAnalyzer")
    
    # Initialize the analyzer
    analyzer = MentalHealthAnalyzer()
    print("Successfully initialized analyzer")
    
    # Test with a simple message
    test_message = "I am feeling happy today!"
    print(f"\nTesting with message: '{test_message}'")
    
    results = analyzer.analyze_text(test_message)
    print("\nAnalysis Results:")
    print(f"Sentiment: {(results['sentiment'] * 100):.2f}% positive")
    print(f"Confidence: {(results['confidence'] * 100):.2f}%")
    print(f"Text Length: {results['text_length']} words")
    
    print("\nTest completed successfully!")
    
except Exception as e:
    print(f"Error: {str(e)}")
    print(f"Current directory: {os.path.dirname(os.path.abspath(__file__))}")
    print(f"MindGPT directory: {mindgpt_dir}")
    print(f"Python path: {sys.path}") 