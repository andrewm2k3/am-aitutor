import os
from dotenv import load_dotenv

from lang_module.question_generator import generate_questions
from lang_module.vocab_manager import extract_valid_words, generate_known_vocab_text

load_dotenv()  # Load .env with your OPEN_AI_KEY

# Test 1: Generate Questions
essay = "In my essay, I talked about how learning Spanish helped me connect with my grandmother."
questions = generate_questions(essay, "Spanish", 3)
print("Generated Questions:")
print(questions)

# Test 2: Extract Words
response_text = "Aprendí mucho sobre mi cultura y mi familia."
valid_words = extract_valid_words(response_text, "Spanish")
print("\nValid Words:")
print(valid_words)

# Test 3: Generate Paragraph Using Known Vocab
paragraph = generate_known_vocab_text(valid_words, topic="mi familia", target_language="Spanish")
print("\nGenerated Paragraph:")
print(paragraph)
