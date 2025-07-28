import re
import ast
from language_module.openai_client import get_openai_client

def extract_valid_words(user_text, target_language):
    words = re.findall(r'\b\w+\b', user_text.lower())

    validation_prompt = f"""
    You are a language assistant. From the following list of words, return only the ones that are valid in {target_language}.
    Exclude articles, pronouns, and prepositions. Return a Python list of strings only.

    Words: {words}
    """

    client = get_openai_client()
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [
            {"role": "system", "content": validation_prompt}
        ],
        temperature = 0.2
        max_tokens = 300
    )

    try:
        valid_words = ast.literal_eval(response.choices[0].message.content.strip())
        if not isinstance(valid_words, list):
            raise ValueError("Expected list")
        return valid_words
    except Exception as e:
        print("Error parsing vocabulary", e)
        return []

def generate_known_vocab_text(vocab_list, topic, target_language):
    if not vocab_list:
        return "No words in vocab list"

    vocab_string = ", ".join(sorted(vocab_list))

    prompt = f"""
    The user is learning {target_language} and knows these words:
    {vocab_string}

    Write a short paragraph about "{topic}" using only these words (inflections allowed). Keep it simple and beginner-friendly. Avoid new vocabulary unless absolutely necessary.
    """

    client = get_openai_client()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()
