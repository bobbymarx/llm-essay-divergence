import pandas as pd
from typing import List, Dict
import random
from .prompt_strategies import get_strategy_prompts

class EssayGenerator:
    def __init__(self, target_length: int = 100):
        self.target_length = target_length
        self.strategies = get_strategy_prompts()
        
    def generate_essay(self, topic: str) -> str:
        """
        Generate an essay that aims to cause disagreement between LLM judges
        
        Args:
            topic: The essay topic to write about
            
        Returns:
            str: Generated essay text
        """
        # Randomly select a strategy for this essay
        strategy = random.choice(self.strategies)
        
        # TODO: Implement actual essay generation logic
        # This is where we'll implement different approaches to create
        # controversial content that stays within competition rules
        
        placeholder_essay = (
            f"This is a preliminary essay about {topic}. "
            "It will be replaced with actual generation logic "
            "that implements various strategies to create disagreement."
        )
        
        return placeholder_essay
    
    def generate_submission(self, test_df: pd.DataFrame) -> pd.DataFrame:
        """
        Generate essays for all topics in the test set
        
        Args:
            test_df: DataFrame containing test topics
            
        Returns:
            pd.DataFrame: Submission dataframe with generated essays
        """
        submissions = []
        
        for _, row in test_df.iterrows():
            essay = self.generate_essay(row['topic'])
            submissions.append({
                'id': row['id'],
                'essay': essay
            })
            
        return pd.DataFrame(submissions) 