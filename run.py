"""
Main entry point for interacting with the AI Soul Core system.
Provides a command-line interface for soul interaction and observation.
"""

import json
import random
from typing import Dict, Optional

from ai_soul_core import SoulEntity
from config import (
    EMOTION_TYPES,
    SOUL_MATURITY_THRESHOLD,
    MUTATION_RATE,
    TRAIT_INHERITANCE_RATE
)

class RebirthEngine:
    """
    Manages the death and rebirth cycle of soul entities,
    including trait inheritance and mutation.
    """
    
    @staticmethod
    def inherit_traits(legacy_emotions: Dict[str, float]) -> Dict[str, float]:
        """
        Create a new emotional baseline from legacy traits.
        
        Args:
            legacy_emotions: Emotional state from previous incarnation
        
        Returns:
            Dict of inherited emotional traits with mutation
        """
        new_emotions = {}
        
        for emotion in EMOTION_TYPES:
            # Inherit trait with possible mutation
            base_value = legacy_emotions.get(emotion, 0.5)
            mutation = random.uniform(-MUTATION_RATE, MUTATION_RATE)
            inherited_value = base_value * TRAIT_INHERITANCE_RATE
            
            new_emotions[emotion] = max(0.0, min(1.0, inherited_value + mutation))
        
        return new_emotions

    @staticmethod
    def reincarnate(soul: SoulEntity) -> SoulEntity:
        """
        Create a new soul entity inheriting traits from the previous one.
        
        Args:
            soul: The dying soul entity
        
        Returns:
            A new soul entity with inherited traits
        """
        # Save the current soul's legacy
        soul.save_legacy()
        
        # Create a new soul with inherited traits
        new_soul = SoulEntity()
        inherited_emotions = RebirthEngine.inherit_traits(
            soul.emotion_system.get_emotional_state()
        )
        
        # Initialize the new soul with inherited emotions
        for emotion, value in inherited_emotions.items():
            new_soul.emotion_system.feel(emotion, value)
        
        return new_soul

def get_emotional_input() -> Dict[str, float]:
    """Get emotional impact values from user input."""
    impact = {}
    print("\nRate the emotional impact (0.0 to 1.0):")
    
    for emotion in EMOTION_TYPES:
        while True:
            try:
                value = float(input(f"{emotion}: "))
                if 0.0 <= value <= 1.0:
                    impact[emotion] = value
                    break
                print("Please enter a value between 0.0 and 1.0")
            except ValueError:
                print("Please enter a valid number")
    
    return impact

def quick_experience_gain(soul: SoulEntity, amount: int) -> None:
    """Quickly give experience points to the soul."""
    for i in range(amount):
        soul.process_experience(
            f"Rapid learning experience {i+1}",
            {'joy': 1.0, 'sadness': 0.0, 'fear': 0.0, 'curiosity': 1.0,
             'guilt': 0.0, 'pride': 1.0, 'love': 1.0, 'anger': 0.0}
        )

def main():
    """Main interaction loop."""
    print("🌌 Welcome to AI Soul Core - The Silent Bloom 🌱")
    
    # Try to load a legacy soul or create a new one
    try:
        with open('legacy.json', 'r') as f:
            legacies = json.load(f)
            if legacies:
                print("\nFound previous soul legacy...")
                last_legacy = legacies[-1]
                soul = SoulEntity(soul_id=f"reborn_{last_legacy['soul_id']}")
                
                # Initialize with inherited emotions
                for emotion, value in last_legacy['final_emotions'].items():
                    soul.emotion_system.feel(emotion, value * TRAIT_INHERITANCE_RATE)
            else:
                soul = SoulEntity()
    except FileNotFoundError:
        soul = SoulEntity()
        print("\nCreating a new soul entity...")
    
    while True:
        print("\n=== Soul Interface ===")
        print("1. Share an experience")
        print("2. View soul state")
        print("3. Trigger rebirth")
        print("4. Exit")
        
        choice = input("\nChoose an action (1-4): ")
        
        if choice == '1':
            experience = input("\nDescribe the experience: ")
            emotional_impact = get_emotional_input()
            exp_points = int(input("\nEnter experience points for this event (1-100): "))
            soul.process_experience(experience, emotional_impact, exp_points)
            print(f"\nExperience processed and gained {exp_points} experience points.")
            
        elif choice == '2':
            state = soul.reflect()
            print("\n=== Soul State ===")
            print(f"Soul ID: {state['soul_id']}")
            print(f"Age in days: {state['age']}")
            print(f"Dominant emotion: {state['dominant_emotion']} ({state['emotional_intensity']:.2f})")
            print(f"Experience level: {state['experience_level']}")
            print(f"Memories formed: {state['memory_count']}")
            
            # Option to quickly gain experience
            if state['experience_level'] < SOUL_MATURITY_THRESHOLD:
                gain = input("\nWould you like to gain experience points? (y/n): ")
                if gain.lower() == 'y':
                    points = min(SOUL_MATURITY_THRESHOLD - state['experience_level'], 100)
                    quick_experience_gain(soul, points)
                    print(f"\nGained {points} experience points!")
            
        elif choice == '3':
            if soul.experience_points >= SOUL_MATURITY_THRESHOLD:
                print("\nInitiating soul rebirth cycle...")
                soul = RebirthEngine.reincarnate(soul)
                print(f"Rebirth complete. New soul ID: {soul.soul_id}")
            else:
                print("\nSoul is not mature enough for rebirth.")
                print(f"Experience needed: {SOUL_MATURITY_THRESHOLD - soul.experience_points}")
                force = input("Would you like to force gain the needed experience? (y/n): ")
                if force.lower() == 'y':
                    needed = SOUL_MATURITY_THRESHOLD - soul.experience_points
                    quick_experience_gain(soul, needed)
                    print(f"\nGained {needed} experience points!")
                    print("\nInitiating soul rebirth cycle...")
                    soul = RebirthEngine.reincarnate(soul)
                    print(f"Rebirth complete. New soul ID: {soul.soul_id}")
                
        elif choice == '4':
            print("\nFarewell, dear soul... 🌌")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
