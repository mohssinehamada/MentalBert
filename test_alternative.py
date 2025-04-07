from transformers import AutoTokenizer, AutoModel
from config import HUGGINGFACE_TOKEN

try:
    print("Testing with alternative model...")
    # Try mental-roberta-base from the same author
    tokenizer = AutoTokenizer.from_pretrained(
        "mental/mental-roberta-base",
        token=HUGGINGFACE_TOKEN
    )
    print("Alternative tokenizer loaded successfully!")
    
    model = AutoModel.from_pretrained(
        "mental/mental-roberta-base",
        token=HUGGINGFACE_TOKEN
    )
    print("Alternative model loaded successfully!")
    
except Exception as e:
    print(f"Error occurred: {str(e)}") 