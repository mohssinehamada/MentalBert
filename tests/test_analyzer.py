"""
Tests for the MentalHealthAnalyzer class.
"""
import pytest
import torch

from mindgpt.core.analyzer import MentalHealthAnalyzer

def test_analyzer_initialization():
    """Test that the analyzer initializes correctly."""
    analyzer = MentalHealthAnalyzer()
    assert analyzer.model_name == "microsoft/deberta-v3-base"
    assert analyzer.device in ["cuda", "cpu"]
    assert analyzer.model is not None
    assert analyzer.tokenizer is not None

def test_analyze_text_single():
    """Test analyzing a single text input."""
    analyzer = MentalHealthAnalyzer()
    text = "I'm feeling very happy today!"
    
    result = analyzer.analyze_text(text)
    
    assert isinstance(result, dict)
    assert "sentiment" in result
    assert "mental_health_indicator" in result
    assert 0 <= result["sentiment"] <= 1
    assert 0 <= result["mental_health_indicator"] <= 1

def test_analyze_text_batch():
    """Test analyzing multiple texts at once."""
    analyzer = MentalHealthAnalyzer()
    texts = [
        "I'm feeling very happy today!",
        "I've been feeling down lately."
    ]
    
    result = analyzer.analyze_text(texts)
    
    assert isinstance(result, dict)
    assert "sentiment" in result
    assert "mental_health_indicator" in result
    assert 0 <= result["sentiment"] <= 1
    assert 0 <= result["mental_health_indicator"] <= 1

def test_device_selection():
    """Test that device selection works correctly."""
    # Test CPU
    analyzer_cpu = MentalHealthAnalyzer(device="cpu")
    assert analyzer_cpu.device == "cpu"
    assert next(analyzer_cpu.model.parameters()).device.type == "cpu"
    
    # Test CUDA if available
    if torch.cuda.is_available():
        analyzer_cuda = MentalHealthAnalyzer(device="cuda")
        assert analyzer_cuda.device == "cuda"
        assert next(analyzer_cuda.model.parameters()).device.type == "cuda" 