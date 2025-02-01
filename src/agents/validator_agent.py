import subprocess
from typing import Tuple, List
from dataclasses import dataclass

@dataclass
class ValidationResult:
    is_valid: bool
    errors: List[str]
    suggestions: List[str]

class ValidatorAgent:
    def __init__(self):
        self.error_patterns = {
            'python': {
                'syntax_error': 'SyntaxError',
                'name_error': 'NameError',
                'type_error': 'TypeError'
            },
            'javascript': {
                'syntax_error': 'SyntaxError',
                'reference_error': 'ReferenceError',
                'type_error': 'TypeError'
            }
        }

    def validate_translation(self, translated_code: str, language: str) -> ValidationResult:
        """
        Validates the translated code by attempting to run it
        """
        execution_result = self._execute_code(translated_code, language)
        errors = self._analyze_errors(execution_result, language)
        suggestions = self._generate_suggestions(errors, language)

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            suggestions=suggestions
        )

    def _execute_code(self, code: str, language: str) -> Tuple[int, str, str]:
        """
        Executes the code and returns the result
        """
        if language == 'python':
            process = subprocess.Popen(
                ['python', '-c', code],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
        elif language == 'javascript':
            process = subprocess.Popen(
                ['node', '-e', code],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
        
        stdout, stderr = process.communicate()
        return (process.returncode, stdout.decode(), stderr.decode())

    def _analyze_errors(self, execution_result: Tuple[int, str, str], language: str) -> List[str]:
        """
        Analyzes execution errors and returns a list of error messages
        """
        returncode, stdout, stderr = execution_result
        errors = []

        if returncode != 0:
            for line in stderr.split('\n'):
                for error_type, pattern in self.error_patterns[language].items():
                    if pattern in line:
                        errors.append(f"{error_type}: {line}")

        return errors

    def _generate_suggestions(self, errors: List[str], language: str) -> List[str]:
        """
        Generates suggestions for fixing the errors
        """
        suggestions = []
        for error in errors:
            if 'SyntaxError' in error:
                suggestions.append("Check for missing brackets, parentheses, or semicolons")
            elif 'NameError' in error or 'ReferenceError' in error:
                suggestions.append("Verify all variables are properly declared and in scope")
            elif 'TypeError' in error:
                suggestions.append("Ensure proper type conversions and method compatibility")

        return suggestions 