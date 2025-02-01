from typing import Optional
from .planner_agent import TranslationPlan

class TranslatorAgent:
    def __init__(self):
        self.translation_cache = {}

    def translate_code(self, source_code: str, translation_plan: TranslationPlan) -> str:
        """
        Translates code based on the provided translation plan
        """
        # Check cache first
        cache_key = f"{source_code}_{translation_plan.source_language}_{translation_plan.target_language}"
        if cache_key in self.translation_cache:
            return self.translation_cache[cache_key]

        translated_code = self._execute_translation(source_code, translation_plan)
        
        # Cache the result
        self.translation_cache[cache_key] = translated_code
        return translated_code

    def _execute_translation(self, source_code: str, plan: TranslationPlan) -> str:
        """
        Executes the actual translation based on the plan
        """
        # Apply syntax mappings
        translated_code = source_code
        for source_syntax, target_syntax in plan.language_specific_rules['syntax_mapping'].items():
            translated_code = translated_code.replace(source_syntax, target_syntax)

        # Apply library mappings
        for source_lib, target_lib in plan.language_specific_rules['library_mapping'].items():
            translated_code = translated_code.replace(source_lib, target_lib)

        return self._post_process_translation(translated_code, plan)

    def _post_process_translation(self, code: str, plan: TranslationPlan) -> str:
        """
        Applies post-processing rules specific to the target language
        """
        if plan.target_language == 'javascript':
            # Add semicolons if needed
            code = self._add_semicolons(code)
        
        return code

    def _add_semicolons(self, code: str) -> str:
        """
        Adds semicolons to JavaScript code
        """
        lines = code.split('\n')
        processed_lines = []
        
        for line in lines:
            line = line.strip()
            if line and not line.endswith('{') and not line.endswith('}') and not line.endswith(';'):
                line += ';'
            processed_lines.append(line)
            
        return '\n'.join(processed_lines) 