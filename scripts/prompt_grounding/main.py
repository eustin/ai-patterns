from huggingface_hub import hf_hub_download
from llama_cpp import Llama

# Why this one and not the official Google one?
# Because the Google one says this "You need to agree to share your contact information to access this model"
# No thank you!
HUGGING_FACE_REPO_ID = "unsloth/gemma-3-4b-it-GGUF"
MODEL_FILENAME = "gemma-3-4b-it-Q4_K_M.gguf"

# For reproducability
MODEL_REVISION = "5c28c76ebfeeee5f3676f0518e5fc2ab67beffb4"
TEMPERATURE = 0.0


def main():
    print("Downloading Gemma 3 model...")
    model_fpath = hf_hub_download(
        repo_id=HUGGING_FACE_REPO_ID, filename=MODEL_FILENAME, revision=MODEL_REVISION
    )

    print("Loading model...")
    llm = Llama(model_path=model_fpath, verbose=False)

    # See https://llama-cpp-python.readthedocs.io/en/latest/#chat-completion
    question = "Who won Battle I of Road to Las Vegas 2026?"
    llm_response = llm.create_chat_completion(
        messages=[{"role": "user", "content": question}],
        temperature=TEMPERATURE,
    )
    answer = llm_response["choices"][0]["message"]["content"]
    print(answer)

    # WTF???
    #
    # As of today, November 2, 2023, **Team Liquid** won Battle I of Road to Las Vegas 2026!
    #
    # They defeated Team Solo Quilts in a dominant 3-0 victory.
    #
    # You can find the full results and highlights on the official Road to Las Vegas website: [https://roadtovegas.gg/](https://roadtovegas.gg/)


if __name__ == "__main__":
    main()
