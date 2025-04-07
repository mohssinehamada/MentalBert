from huggingface_hub import login
from config import HUGGINGFACE_TOKEN

def test_huggingface_token():
    try:
        # Attempt to login with the token
        login(token=HUGGINGFACE_TOKEN)
        print("✅ Successfully authenticated with Hugging Face!")
        
        # Try to access a common public model
        from transformers import AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        print("✅ Successfully accessed the model!")
        
        return True
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_huggingface_token() 