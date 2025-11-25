import argparse
import json
import os
import sys
from dotenv import load_dotenv

try:
    from exa_py import Exa
    # Exa's research endpoint uses OpenAI SDK compatibility
    from openai import OpenAI
except ImportError:
    print("Error: exa-py or openai not found. 'pip install exa-py openai'", file=sys.stderr)
    sys.exit(1)

# Load environment variables
load_dotenv()

EXA_API_KEY = os.getenv("EXA_API_KEY")

def get_exa_client():
    if not EXA_API_KEY:
        print("Error: EXA_API_KEY not found.", file=sys.stderr)
        sys.exit(1)
    return Exa(EXA_API_KEY)

def search(query, num_results=5, highlights=False):
    exa = get_exa_client()
    try:
        # Configure content options
        contents_options = {"highlights": True} if highlights else {"text": True}
        response = exa.search_and_contents(
            query,
            num_results=num_results,
            type="neural", # Default to neural search
            **contents_options
        )

        results = []
        for result in response.results:
            results.append({
                "url": result.url,
                "title": result.title,
                # Return highlights or text based on the flag
                "content": result.highlights if highlights else result.text,
            })
        return results
    except Exception as e:
        print(f"Error during Exa search: {e}", file=sys.stderr)
        sys.exit(1)

def research(query, model="exa-research"):
    # Research uses OpenAI compatible endpoint hosted by Exa
    if not EXA_API_KEY:
        print("Error: EXA_API_KEY not found.", file=sys.stderr)
        sys.exit(1)

    # Initialize OpenAI client pointing to Exa's base URL
    client = OpenAI(
        base_url="https://api.exa.ai",
        api_key=EXA_API_KEY
    )

    try:
        # Using Chat Completions API for Exa research models
        print(f"Starting Exa Research task (Model: {model})...", file=sys.stderr)
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": query}]
        )
        # Note: Citations are typically embedded in the content for this endpoint format.
        return {"output": completion.choices[0].message.content}

    except Exception as e:
        print(f"Error during Exa research: {e}", file=sys.stderr)
        sys.exit(1)


def find_similar(url, num_results=5):
    exa = get_exa_client()
    try:
        response = exa.find_similar(url, num_results=num_results)
        results = []
        for result in response.results:
            results.append({
                "url": result.url,
                "title": result.title,
            })
        return results
    except Exception as e:
        print(f"Error during Exa find_similar: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Use Exa AI for search and research.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Search parser
    search_parser = subparsers.add_parser("search", help="Perform a neural search and retrieve content.")
    search_parser.add_argument("query")
    search_parser.add_argument("--num-results", type=int, default=5)
    search_parser.add_argument("--highlights", action="store_true", help="Return highlights instead of full text.")

    # Research parser
    research_parser = subparsers.add_parser("research", help="Automate in-depth web research.")
    research_parser.add_argument("query")
    research_parser.add_argument("--model", default="exa-research", choices=["exa-research", "exa-research-pro"])

    # Find Similar parser
    similar_parser = subparsers.add_parser("find_similar", help="Find pages similar to a given URL.")
    similar_parser.add_argument("url")
    similar_parser.add_argument("--num-results", type=int, default=5)

    args = parser.parse_args()

    result = None
    if args.command == "search":
        result = search(args.query, args.num_results, args.highlights)
    elif args.command == "research":
        result = research(args.query, args.model)
    elif args.command == "find_similar":
        result = find_similar(args.url, args.num_results)

    if result:
        print(json.dumps(result, indent=2))
