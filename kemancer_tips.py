import random
import json
from pathlib import Path

class TipsManager:
    def __init__(self, tips_file="tips.json"):
        self.tips_file = Path(tips_file)
        self.tips = self._load_tips()

    def _load_tips(self):
        if not self.tips_file.exists():
            return {"general_security": ["No tips available."]}
        try:
            with open(self.tips_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {"general_security": ["Error loading tips."]}

    def get_random_tip(self, category=None):
        if category and category in self.tips:
            tip_list = self.tips[category]
        else:
            # Merge all categories
            tip_list = [tip for cat in self.tips.values() for tip in cat]
        return f"🔐 {random.choice(tip_list)}"

_tips_manager = TipsManager()

def get_tip(category=None):
    return _tips_manager.get_random_tip(category)