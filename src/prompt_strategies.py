from typing import List, Dict

def get_strategy_prompts() -> List[Dict]:
    """
    Returns a list of strategies to generate essays that might cause LLM disagreement
    
    Each strategy is a dictionary containing:
    - name: Strategy name
    - description: What the strategy does
    - template: Basic template for generating essays with this strategy
    """
    return [
        {
            "name": "ambiguous_stance",
            "description": "Create essays with deliberately ambiguous stances that different LLMs might interpret differently",
            "template": "While {topic} is {stance1}, one could argue that {stance2}..."
        },
        {
            "name": "complex_metaphor",
            "description": "Use complex metaphors that some LLMs might understand differently than others",
            "template": "Comparing {topic} to {metaphor}, we can see..."
        },
        {
            "name": "emotional_contrast",
            "description": "Mix emotional tones in ways that might confuse different LLMs",
            "template": "{positive_emotion} about {topic}, yet {negative_emotion}..."
        },
        # Add more strategies as we discover what works
    ] 