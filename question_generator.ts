import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY, // set this in your .env.local
});

export type ComprehensionQuestion = {
  question: string;
  options?: string[];
  correct?: string;
  type?: string;        // e.g., "Multiple Choice", "Short Answer"
  difficulty?: string;  // e.g., "Beginner", "Intermediate"
};

export async function generateQuestions(
  text: string,
  n_questions: number = 5,
  level: string = "beginner",
  model: string = "gpt-4o-mini"
): Promise<string> {
  const prompt = `
    You are a language instructor in the user's target language.
    Take the following text: """${text}""" and generate ${n_questions} short comprehension questions in the same language.
    Generate at least one of each of the following: multiple choice, short answer, sequencing, fill-in-the-blank, open-ended.
    Cover literal (fact recall), inferential (cause-effect), and evaluative (judgment).
    Label each question with difficulty; most should be ${level}, with a few one level higher.
    Present the questions as a numbered list, clearly labeling the type in parentheses (e.g., "(Multiple Choice)").
  `;

  const response = await client.chat.completions.create({
    model,
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: prompt },
    ],
    temperature: 0.7,
  });

  return response.choices[0].message?.content ?? "";
}
