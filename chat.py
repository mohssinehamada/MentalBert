from simple_analyzer import SimpleMentalHealthAnalyzer

def main():
    print("Welcome to the Mental Health Chat!")
    print("Type 'quit' to exit")
    print("-" * 50)
    
    analyzer = SimpleMentalHealthAnalyzer()
    
    while True:
        user_input = input("\nHow are you feeling today? ")
        
        if user_input.lower() == 'quit':
            print("\nThank you for chatting! Take care!")
            break
            
        try:
            results = analyzer.analyze_text(user_input)
            
            print("\nAnalysis Results:")
            print(f"Sentiment: {(results['sentiment'] * 100):.2f}% positive")
            print(f"Mental Health Indicator: {(results['mental_health_indicator'] * 100):.2f}%")
            
            # Provide some feedback based on the scores
            if results['sentiment'] > 0.6:
                print("You seem to be in a positive mood! That's great!")
            elif results['sentiment'] < 0.4:
                print("I notice you might be feeling down. Remember, it's okay to not be okay.")
            
            if results['mental_health_indicator'] > 0.6:
                print("Your mental health indicators are positive. Keep maintaining healthy habits!")
            elif results['mental_health_indicator'] < 0.4:
                print("I'm here to listen. Would you like to talk more about what's on your mind?")
                
        except Exception as e:
            print(f"Sorry, I encountered an error: {str(e)}")
            print("Please try rephrasing your message.")

if __name__ == "__main__":
    main() 