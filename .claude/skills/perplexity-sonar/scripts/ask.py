import os
import argparse
import sys
from dotenv import load_dotenv

try:
    # Perplexity API is compatible with the OpenAI client structure
    from openai import OpenAI
except ImportError:
    print("Error: openai library not found. Please run 'pip install openai'", file=sys.stderr)
    sys.exit(1)

# Load environment variables
load_dotenv()

def ask_perplexity(prompt, model="sonar-medium-online"):
    """Sends a prompt to the Perplexity Sonar API."""
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        print("Error: PERPLEXITY_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")

    try:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert researcher. Respond to the user's query using the most recent and relevant information available on the web."
                    "Provide a comprehensive, accurate, and neutral response. Cite your sources clearly."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ]

        response = client.chat.completions.create(
            model=model,
            messages=messages,
        )

        # Extract and output the synthesized answer
        answer = response.choices[0].message.content
        print(answer)

    except Exception as e:
        print(f"Error during Perplexity API call: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perplexity Sonar Tool for Claude Skills")
    parser.add_argument("--prompt", required=True, help="The research question or prompt.")
    parser.add_argument("--model", default="sonar-medium-online",
                        choices=["sonar-small-online", "sonar-medium-online", "sonar-large-online"],
                        help="The Perplexity Sonar model to use.")

    args = parser.parse_args()
    ask_perplexity(args.prompt, args.model)
