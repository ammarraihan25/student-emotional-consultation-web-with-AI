import json
from predefined_responses import PREDEFINED_RESPONSES

with open('predefined_responses.json', 'w', encoding='utf-8') as f:
    json.dump(PREDEFINED_RESPONSES, f, ensure_ascii=False, indent=2)
print("Successfully exported predefined responses to predefined_responses.json")
