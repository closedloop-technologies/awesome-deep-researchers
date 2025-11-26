"""Utility functions for benchmark system."""
import re
from pathlib import Path
from typing import List, Dict, Tuple
import json

from .config import SKILLS_DIR, TAXONOMY_FILE, EXCLUDED_SKILLS


def discover_skills() -> List[Dict[str, str]]:
    """
    Dynamically discover all skills in .claude/skills directory.
    
    Returns:
        List of skill dictionaries with name, script_path, and requirements
    """
    skills = []
    
    if not SKILLS_DIR.exists():
        raise FileNotFoundError(f"Skills directory not found: {SKILLS_DIR}")
    
    for skill_dir in SKILLS_DIR.iterdir():
        if not skill_dir.is_dir():
            continue
        
        skill_name = skill_dir.name
        
        # Skip excluded skills and test-related directories
        if skill_name in EXCLUDED_SKILLS or skill_name in ['tests', '__pycache__']:
            continue
        
        # Find the main script
        scripts_dir = skill_dir / "scripts"
        if not scripts_dir.exists():
            continue
        
        # Look for Python scripts
        python_files = list(scripts_dir.glob("*.py"))
        if not python_files:
            continue
        
        # Use the first Python file (or look for specific patterns)
        main_script = python_files[0]
        
        # Check for requirements
        requirements_file = skill_dir / "requirements.txt"
        requirements = []
        if requirements_file.exists():
            requirements = requirements_file.read_text().strip().split('\n')
            requirements = [r.strip() for r in requirements if r.strip() and not r.startswith('#')]
        
        skills.append({
            "name": skill_name,
            "script_path": str(main_script),
            "requirements": requirements,
            "skill_dir": str(skill_dir)
        })
    
    return sorted(skills, key=lambda x: x['name'])


def parse_taxonomy_questions() -> Dict[str, List[str]]:
    """
    Parse the taxonomy document and extract example questions by category.
    
    Returns:
        Dictionary mapping category names to lists of questions
    """
    if not TAXONOMY_FILE.exists():
        raise FileNotFoundError(f"Taxonomy file not found: {TAXONOMY_FILE}")
    
    content = TAXONOMY_FILE.read_text()
    
    categories = {}
    current_category = None
    
    # Pattern to match category headers like "### **3.1 Source Retrieval**"
    category_pattern = re.compile(r'###\s+\*\*\d+\.\d+\s+(.+?)\*\*')
    
    # Pattern to match questions (bullet points starting with *, handles both straight and curly quotes)
    # Matches: * "question" or * "question" (with curly quotes U+201C and U+201D)
    question_pattern = re.compile(r'^\*\s+["\u201C](.+?)["\u201D]', re.MULTILINE)
    
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        # Check if this is a category header
        category_match = category_pattern.match(line.strip())
        if category_match:
            current_category = category_match.group(1).strip()
            categories[current_category] = []
            continue
        
        # Check if this is a question
        if current_category:
            question_match = question_pattern.match(line.strip())
            if question_match:
                question = question_match.group(1).strip()
                categories[current_category].append(question)
    
    # Filter out empty categories
    categories = {k: v for k, v in categories.items() if v}
    
    return categories


def get_skill_command_info(skill_name: str) -> Dict[str, str]:
    """
    Get the command-line interface information for a specific skill.
    
    Returns:
        Dictionary with command template and parameter mappings
    """
    # Define command templates for each skill
    # These map to the actual CLI arguments each skill expects
    
    command_info = {
        "exa-research": {
            "command": "python {script} research {question}",
            "supports_query": True,
        },
        "gpt-researcher": {
            "command": "python {script} --query {question}",
            "supports_query": True,
        },
        "jina-ai": {
            "command": "python {script} search {question}",
            "supports_query": True,
        },
        "langchain-deep-research": {
            "command": "python {script} --query {question}",
            "supports_query": True,
            "requires_server": True,  # Needs LangGraph server running
        },
        "openai-deep-research": {
            "command": "python {script} --prompt {question}",
            "supports_query": True,
        },
        "perplexity-sonar": {
            "command": "python {script} --prompt {question}",
            "supports_query": True,
        },
        "smolagents": {
            "command": "python {script} --task {question}",
            "supports_query": True,
        },
        "stanford-storm": {
            "command": "python {script} --topic {question}",
            "supports_query": True,
        },
        "tavily-search": {
            "command": "python {script} --query {question}",
            "supports_query": True,
        },
        "xai-grok": {
            "command": "python {script} --query {question}",
            "supports_query": True,
        },
    }
    
    return command_info.get(skill_name, {
        "command": "python {script} {question}",
        "supports_query": True,
    })


def sanitize_filename(text: str, max_length: int = 100) -> str:
    """
    Convert text to a safe filename.
    
    Args:
        text: Input text
        max_length: Maximum filename length
        
    Returns:
        Sanitized filename string
    """
    # Remove or replace invalid characters
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '_', text)
    text = text.strip('_')
    
    # Truncate if too long
    if len(text) > max_length:
        text = text[:max_length]
    
    return text.lower()


def format_duration(seconds: float) -> str:
    """
    Format duration in human-readable format.
    
    Args:
        seconds: Duration in seconds
        
    Returns:
        Formatted string (e.g., "2m 30.5s")
    """
    if seconds < 60:
        return f"{seconds:.2f}s"
    
    minutes = int(seconds // 60)
    remaining_seconds = seconds % 60
    
    if minutes < 60:
        return f"{minutes}m {remaining_seconds:.1f}s"
    
    hours = int(minutes // 60)
    remaining_minutes = minutes % 60
    return f"{hours}h {remaining_minutes}m {remaining_seconds:.0f}s"


def estimate_cost(tokens_input: int, tokens_output: int, model: str, provider: str) -> float:
    """
    Estimate cost based on token usage.
    
    Args:
        tokens_input: Number of input tokens
        tokens_output: Number of output tokens
        model: Model name
        provider: Provider name (openai, anthropic, etc.)
        
    Returns:
        Estimated cost in USD
    """
    from .config import COST_PER_1K_TOKENS, DEFAULT_COST_PER_1K
    
    # Get pricing for provider and model
    if provider in COST_PER_1K_TOKENS and model in COST_PER_1K_TOKENS[provider]:
        pricing = COST_PER_1K_TOKENS[provider][model]
    else:
        pricing = DEFAULT_COST_PER_1K
    
    input_cost = (tokens_input / 1000) * pricing["input"]
    output_cost = (tokens_output / 1000) * pricing["output"]
    
    return input_cost + output_cost
