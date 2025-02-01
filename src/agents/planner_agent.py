from dataclasses import dataclass
from typing import List

@dataclass
class TranslationPlan:
    source_language: str
    target_language: str
    steps: List[str]
    language_specific_rules: dict

class PlannerAgent:
    def __init__(self):
        self.language_mappings = {
            'python': {'extension': '.py', 'paradigm': 'multi-paradigm'},
            'javascript': {'extension': '.js', 'paradigm': 'multi-paradigm'},
            'java': {'extension': '.java', 'paradigm': 'object-oriented'},
            # Add more languages as needed
        }

    def create_translation_plan(self, source_code: str, source_lang: str, target_lang: str) -> TranslationPlan:
        """
        Creates a detailed plan for code translation
        """
        # Analyze source code structure
        steps = [
            f"Analyze {source_lang} code structure and dependencies",
            f"Identify {source_lang}-specific idioms",
            f"Map {source_lang} constructs to {target_lang} equivalents",
            "Generate initial translation",
            "Apply language-specific optimizations"
        ]

        # Define language-specific translation rules
        rules = self._get_language_rules(source_lang, target_lang)

        return TranslationPlan(
            source_language=source_lang,
            target_language=target_lang,
            steps=steps,
            language_specific_rules=rules
        )

    def _get_language_rules(self, source_lang: str, target_lang: str) -> dict:
        """
        Define specific translation rules between language pairs
        """
        rules = {
            'syntax_mapping': {},
            'library_mapping': {},
            'idioms_mapping': {}
        }
        
        # Example rules for Python to JavaScript
        if source_lang == 'python' and target_lang == 'javascript':
            rules['syntax_mapping'] = {
                'def': 'function',
                'elif': 'else if',
                'None': 'null',
                'True': 'true',
                'False': 'false'
            }
            rules['library_mapping'] = {
                'print': 'console.log',
                'len': '.length'
            }

        return rules 