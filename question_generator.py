from lang_module.openai_client import get_openai_client

def generate_questions(essay_text, target_language, num_questions):
    client = get_openai_client()
    
    system_prompt = f"""
    You are an exam administrator evaluating whether a student has authentically engaged with their written work by generating insightful, personalized questions based on the essay. Focus on the Human Dimension of Fink's model. Use key quotes and make the user reflect. Only use one question mark per question.
    Generate {num_questions} questions.
    Format:
    Question 1: <text>
    ...
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": essay_text}
        ],
        temperature=0.7,
        max_tokens=1000
    )

    questions_text = response.choices[0].message.content
    questions = []

    for line in questions_text.strip().split("\n"):
        if line.strip().startswith("Question"):
            parts = line.split(":", 1)
            if len(parts) > 1:
                questions.append(parts[1].strip())

    return questions
