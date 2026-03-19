import unittest
from emotion_detection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_valid_input(self):
        result = emotion_detector("I am happy")
        self.assertIn("dominant_emotion", result)

    def test_empty_input(self):
        result = emotion_detector("")
        self.assertIn("error", result)

    def test_no_text_meaning(self):
        result = emotion_detector("...")
        self.assertIsInstance(result, dict)

    def test_negative_emotion(self):
        result = emotion_detector("I hate everything")
        self.assertIn("dominant_emotion", result)

if __name__ == "__main__":
    unittest.main()