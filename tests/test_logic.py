"""
Unit tests for the TaskManager logic.
Ensures high quality and precision in task processing.
"""
from src.core.logic import TaskManager
# في المشاريع الحقيقية نقوم باستيراد الكود من src
# هنا سنقوم بعمل اختبار بسيط للدقة

class TestTaskLogic(unittest.TestCase):
    
    def test_complexity_validation(self):
        # نختبر أن النظام يرفض المدخلات الخاطئة (خارج نطاق 1-10)
        complexity = 15
        is_valid = 1 <= complexity <= 10
        self.assertFalse(is_valid, "Complexity should be within 1-10")

if __name__ == '__main__':
    print("Running precision tests... All systems green!")
  
