from typing import Optional
from .agents.planner_agent import PlannerAgent
from .agents.translator_agent import TranslatorAgent
from .agents.validator_agent import ValidatorAgent, ValidationResult

class CodeTranslationOrchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.translator = TranslatorAgent()
        self.validator = ValidatorAgent()
        self.max_correction_attempts = 3

    def translate_code(self, 
                      source_code: str, 
                      source_lang: str, 
                      target_lang: str) -> Optional[str]:
        """
        Orchestrates the entire translation process
        """
        # Step 1: Create translation plan
        translation_plan = self.planner.create_translation_plan(
            source_code, source_lang, target_lang
        )

        # Step 2: Perform initial translation
        translated_code = self.translator.translate_code(
            source_code, translation_plan
        )

        # Step 3: Validate and correct
        attempts = 0
        while attempts < self.max_correction_attempts:
            validation_result = self.validator.validate_translation(
                translated_code, target_lang
            )

            if validation_result.is_valid:
                return translated_code

            # Apply corrections based on validation feedback
            translated_code = self._apply_corrections(
                translated_code, validation_result, translation_plan
            )
            attempts += 1

        return translated_code if attempts < self.max_correction_attempts else None

    def _apply_corrections(self, 
                         code: str, 
                         validation_result: ValidationResult, 
                         translation_plan: dict) -> str:
        """
        Applies corrections based on validation feedback
        """
        corrected_code = code
        
        for suggestion in validation_result.suggestions:
            if "semicolons" in suggestion.lower():
                corrected_code = self.translator._add_semicolons(corrected_code)
            # Add more correction rules based on suggestions
            
        return corrected_code 