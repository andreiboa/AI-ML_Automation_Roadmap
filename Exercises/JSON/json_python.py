
#for practicing JSON in Python
import json

json_data = '''
{
    "name": "Andrei Boa",
    "age": 22,
    "learning_ai_ml": true,
    "skills": [
        "Python",
        "Git",
        "SQL"
    ]
}
'''

json_data = json.loads(json_data)
print(f"JSON Data: {json_data}\n"
      f"Type: {type(json_data)}\n"
      f"Name: {json_data['name']}\n"
      f"First Skill: {json_data['skills'][0]}",
      )

myself = {
    "name": "Andrei Boa",
    "age": 22,
    "skills": [
        "Python",
        "Java",
        "C#"
    ],
    "learning_ai_ml": True,
    "tools": {
        "engine": "Unity",
        "ide": [
            "Visual Studio",
            "Netbeans"
        ]
    }
}

myself_json = json.dumps(myself, indent=4)
print(f"myself: {myself_json}\n"
      f"Type: {type(myself_json)}\n"
      )
    