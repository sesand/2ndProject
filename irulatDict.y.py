import json

# Dictionary of English words and their meanings
english_dictionary = {
    "good": ["fine", "virtuous", "moral", "ethical", "upright", "quality", "superior"],
    "bad": ["poor", "inferior", "evil", "harmful", "negative", "unpleasant"],
    "happy": ["joyful", "content", "pleased", "satisfied", "delighted", "cheerful"],
    "sad": ["unhappy", "mournful", "gloomy", "dejected", "downhearted", "melancholy"],
    "bright": ["shining", "vibrant", "intelligent", "clever", "luminous", "radiant"],
    "dark": ["dim", "gloomy", "obscure", "sinister", "mysterious", "shadowy"],
    "strong": ["powerful", "robust", "vigorous", "sturdy", "resilient", "potent"],
    "weak": ["frail", "feeble", "fragile", "powerless", "vulnerable", "inadequate"],
    "fast": ["quick", "speedy", "rapid", "swift", "brisk", "hasty"],
    "slow": ["sluggish", "leisurely", "gradual", "unhurried", "languid", "delayed"],
    "big": ["large", "huge", "enormous", "immense", "gigantic", "massive"],
    "small": ["tiny", "little", "miniature", "petite", "minuscule", "compact"],
    "hot": ["warm", "boiling", "heated", "scorching", "sizzling", "blazing"],
    "cold": ["chilly", "frigid", "frosty", "icy", "freezing", "polar"],
    "old": ["ancient", "vintage", "antique", "elderly", "mature", "senior"],
    "new": ["fresh", "modern", "recent", "novel", "contemporary", "innovative"],
    "beautiful": ["attractive", "lovely", "gorgeous", "stunning", "charming", "pretty"],
    "ugly": ["unattractive", "unsightly", "repulsive", "hideous", "repugnant", "grotesque"],
    "smart": ["intelligent", "clever", "bright", "wise", "sharp", "knowledgeable"],
    "dumb": ["stupid", "foolish", "dense", "unintelligent", "ignorant", "witless"],
    "rich": ["wealthy", "affluent", "prosperous", "well-off", "loaded", "opulent"],
    "poor": ["impoverished", "needy", "destitute", "broke", "indigent", "penurious"],
    "thick": ["dense", "coarse", "chunky", "stout", "bulky", "heavy"],
    "thin": ["slim", "slender", "lean", "narrow", "skinny", "scrawny"]
}

# Specify the file path where you want to save the JSON file
json_file_path = 'english_dictionary.json'

# Save the dictionary to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(english_dictionary, json_file, indent=4)

print(f'The English dictionary has been saved to {json_file_path}.')

