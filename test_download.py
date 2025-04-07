from huggingface_hub import snapshot_download
from config import HUGGINGFACE_TOKEN
import os

try:
    print("Starting model download...")
    local_path = snapshot_download(
        repo_id="mental/mental-bert-base-uncased",
        token=HUGGINGFACE_TOKEN,
        local_dir="./model_cache"
    )
    print(f"Model downloaded successfully to {local_path}")
    
    # Now try to load it from local path
    from transformers import AutoTokenizer, AutoModel
    
    tokenizer = AutoTokenizer.from_pretrained(local_path)
    print("Tokenizer loaded successfully!")
    
    model = AutoModel.from_pretrained(local_path)
    print("Model loaded successfully!")
    
except Exception as e:
    print(f"Error occurred: {str(e)}") 