# Code Translation Engine

A sophisticated code translation system that automatically converts source code between different programming languages while preserving functionality and idiomatic patterns.

## Overview

This project provides an intelligent code translation service that helps developers convert code between different programming languages. Unlike simple syntax converters, this system understands language-specific idioms, best practices, and maintains the original code's intent while producing natural, idiomatic code in the target language.

## Why It Matters

- **Developer Productivity**: Saves significant time when porting applications between languages or modernizing legacy codebases
- **Learning Tool**: Helps developers learn new languages by seeing how familiar code patterns translate
- **Cross-Platform Development**: Facilitates maintaining multiple language implementations of libraries and services
- **Legacy Code Migration**: Assists in modernizing legacy systems by translating them to modern languages

## Architecture

The system uses a multi-agent architecture with three specialized components:

1. **Planner Agent**: Analyzes source code and creates detailed translation strategies
   - Maps language-specific constructs
   - Identifies idiomatic patterns
   - Creates step-by-step translation plans

2. **Translator Agent**: Executes the translation with:
   - Syntax mapping
   - Library/API translations
   - Caching for performance
   - Post-processing optimizations

3. **Validator Agent**: Ensures translation quality through:
   - Syntax validation
   - Runtime execution testing
   - Error analysis
   - Correction suggestions

## Features

- 🔄 Bidirectional translation between supported languages
- 🧠 Intelligent handling of language-specific idioms
- ⚡ Performance optimization through translation caching
- 🔍 Validation and error correction
- 📚 Extensible language support system

## Technical Stack

- **Language**: Python 3.x
- **Architecture**: Multi-agent system
- **Design Patterns**: 
  - Factory Pattern
  - Strategy Pattern
  - Observer Pattern
- **Key Technologies**:
  - Type hints for code safety
  - Dataclasses for clean data structures
  - Subprocess management for code validation
  - Caching for performance optimization

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Basic usage:
```python
from src.orchestrator import CodeTranslationOrchestrator

orchestrator = CodeTranslationOrchestrator()
translated_code = orchestrator.translate_code(
    source_code="your_code_here",
    source_lang="python",
    target_lang="javascript"
)
```

## Currently Supported Languages

- Python
- JavaScript
- Java (partial support)

## Future Enhancements

- [ ] Support for additional programming languages
- [ ] Enhanced error correction capabilities
- [ ] Integration with popular IDEs
- [ ] Web API for remote translation services
- [ ] Support for translating entire projects/codebases

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 