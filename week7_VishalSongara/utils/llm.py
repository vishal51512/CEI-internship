from llama_cpp import Llama
from config import MODEL_PATH, MAX_TOKENS, TEMPERATURE, CONTEXT_LENGTH

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=CONTEXT_LENGTH,
    verbose = False
)

def generate(prompt: str) -> str:
    response = llm(
        prompt,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        stop=[
            "<end_of_turn>",
            "<eos>"
        ]
    )

    return response["choices"][0]["text"].strip()