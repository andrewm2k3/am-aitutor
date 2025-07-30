from lambda.question_generator import generate_questions
from lambda.vocab_manager import load_vocab, update_vocab

def lambda_handler(event, context):
    # e.g., event = {"user_id": 123, "level": "beginner"} - depends on API/front-end
    
    user_id = event.get("user_id", "default_user")
    level = event.get("level", "beginner")

    questions = generate_questions(user_id, level)

    return {
        "statusCode": 200,
        "body": questions
    }
