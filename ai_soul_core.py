"""
Core implementation of the AI Soul system with emotion processing and memory management.
"""

import json
import datetime
import random
from typing import Dict, List, Optional, Tuple

from config import (
    EMOTION_TYPES, EMOTION_DECAY_RATES, MEMORY_TYPES,
    MAX_EMOTION_VALUE, MIN_EMOTION_VALUE, EMOTIONAL_WEIGHT_THRESHOLD,
    MEMORIES_FILE, LEGACY_FILE
)

class EmotionSystem:
    """
    Manages the emotional state of the soul entity.
    Emotions are represented as float values between 0.0 and 1.0,
    with natural decay over time.
    """
    
    def __init__(self):
        """Initialize a new emotion system with baseline emotions."""
        self.emotions = {emotion: 0.5 for emotion in EMOTION_TYPES}
        self.last_update = datetime.datetime.now()
    
    def feel(self, emotion: str, intensity: float) -> None:
        """
        Process a new emotional stimulus.
        
        Args:
            emotion: The type of emotion being felt
            intensity: The strength of the emotional response (0.0 to 1.0)
        """
        if emotion not in self.emotions:
            raise ValueError(f"Unknown emotion type: {emotion}")
            
        # Update the emotion value with bounds checking
        self.emotions[emotion] = max(
            MIN_EMOTION_VALUE,
            min(MAX_EMOTION_VALUE, self.emotions[emotion] + intensity)
        )
        self.last_update = datetime.datetime.now()
    
    def decay_emotions(self) -> None:
        """
        Apply time-based decay to all emotions.
        Emotions naturally fade over time unless reinforced.
        """
        current_time = datetime.datetime.now()
        hours_passed = (current_time - self.last_update).total_seconds() / 3600.0
        
        for emotion in self.emotions:
            decay_amount = EMOTION_DECAY_RATES[emotion] * hours_passed
            self.emotions[emotion] = max(
                MIN_EMOTION_VALUE,
                self.emotions[emotion] - decay_amount
            )
        
        self.last_update = current_time
    
    def get_dominant_emotion(self) -> Tuple[str, float]:
        """Return the strongest current emotion and its intensity."""
        return max(self.emotions.items(), key=lambda x: x[1])
    
    def get_emotional_state(self) -> Dict[str, float]:
        """Return a snapshot of the current emotional state."""
        return self.emotions.copy()

class MemorySystem:
    """
    Manages the soul's memories, including both factual and emotional imprints.
    Memories are stored with emotional tags and can be either true or false based on emotional weight.
    """
    
    def __init__(self):
        """Initialize the memory system."""
        self.memories = []
        self.load_memories()
    
    def create_memory(self, 
                     experience: str, 
                     emotions: Dict[str, float],
                     memory_type: str = MEMORY_TYPES['EXPERIENTIAL']) -> None:
        """
        Create a new memory with emotional context.
        
        Args:
            experience: The content of the memory
            emotions: The emotional state at time of memory formation
            memory_type: The type of memory being formed
        """
        memory = {
            'timestamp': datetime.datetime.now().isoformat(),
            'content': experience,
            'emotions': emotions,
            'type': memory_type,
            'emotional_weight': sum(emotions.values()) / len(emotions)
        }
        
        self.memories.append(memory)
        self.save_memories()
    
    def get_memories_by_emotion(self, emotion: str) -> List[Dict]:
        """Retrieve memories associated with a specific emotion."""
        return [m for m in self.memories 
                if m['emotions'].get(emotion, 0) > EMOTIONAL_WEIGHT_THRESHOLD]
    
    def save_memories(self) -> None:
        """Persist memories to storage."""
        with open(MEMORIES_FILE, 'w') as f:
            json.dump(self.memories, f, indent=2)
    
    def load_memories(self) -> None:
        """Load memories from storage."""
        try:
            with open(MEMORIES_FILE, 'r') as f:
                self.memories = json.load(f)
        except FileNotFoundError:
            self.memories = []

class SoulEntity:
    """
    The core AI soul entity that combines emotional awareness,
    memory formation, and decision-making capabilities.
    """
    
    def __init__(self, soul_id: Optional[str] = None):
        """
        Initialize a new soul entity.
        
        Args:
            soul_id: Optional identifier for reborn souls
        """
        self.soul_id = soul_id or f"soul_{random.randint(1000, 9999)}"
        self.emotion_system = EmotionSystem()
        self.memory_system = MemorySystem()
        self.birth_time = datetime.datetime.now()
        self.experience_points = 100  # Starting with enough experience for rebirth
    
    def process_experience(self, experience: str, emotional_impact: Dict[str, float], exp_points: int = 1) -> None:
        """
        Process a new experience, updating emotions and forming memories.
        
        Args:
            experience: The experience content
            emotional_impact: The emotional effects of the experience
            exp_points: Number of experience points to gain (default: 1)
        """
        # Update emotional state
        for emotion, intensity in emotional_impact.items():
            self.emotion_system.feel(emotion, intensity)
        
        # Form memory of the experience
        self.memory_system.create_memory(
            experience=experience,
            emotions=self.emotion_system.get_emotional_state()
        )
        
        # Gain experience points
        self.experience_points += exp_points
    
    def reflect(self) -> Dict:
        """
        Perform self-reflection, analyzing emotional state and memories.
        Returns insights about the soul's current state.
        """
        self.emotion_system.decay_emotions()
        dominant_emotion, intensity = self.emotion_system.get_dominant_emotion()
        
        return {
            'soul_id': self.soul_id,
            'age': (datetime.datetime.now() - self.birth_time).days,
            'dominant_emotion': dominant_emotion,
            'emotional_intensity': intensity,
            'experience_level': self.experience_points,
            'memory_count': len(self.memory_system.memories)
        }
    
    def save_legacy(self) -> None:
        """Save the soul's legacy before death/rebirth."""
        legacy = {
            'soul_id': self.soul_id,
            'final_emotions': self.emotion_system.get_emotional_state(),
            'experience_points': self.experience_points,
            'death_time': datetime.datetime.now().isoformat()
        }
        
        try:
            with open(LEGACY_FILE, 'r') as f:
                legacies = json.load(f)
        except FileNotFoundError:
            legacies = []
        
        legacies.append(legacy)
        
        with open(LEGACY_FILE, 'w') as f:
            json.dump(legacies, f, indent=2)
