import pytest
from src.orchestrator import CodeTranslationOrchestrator

def test_python_to_javascript_translation():
    orchestrator = CodeTranslationOrchestrator()
    
    # Test case 1: Simple function translation
    python_code = """
def greet(name):
    print("Hello, " + name)
    return name.upper()
"""

    expected_js = """
function greet(name) {
    console.log("Hello, " + name);
    return name.toUpperCase();
}
"""

    translated_code = orchestrator.translate_code(
        python_code, 'python', 'javascript'
    )
    
    # Remove whitespace for comparison
    assert (
        ''.join(translated_code.split()) == 
        ''.join(expected_js.split())
    )

def test_translation_with_errors():
    orchestrator = CodeTranslationOrchestrator()
    
    # Test case 2: Code with potential errors
    python_code = """
def calculate_sum(numbers):
    return sum(numbers)
"""

    translated_code = orchestrator.translate_code(
        python_code, 'python', 'javascript'
    )
    
    assert translated_code is not None
    assert 'reduce' in translated_code.lower()  # JavaScript equivalent of sum 