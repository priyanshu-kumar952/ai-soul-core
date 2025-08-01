<<<<<<< HEAD
"""
Configuration settings for the AI Soul Core system.
Contains constants and parameters that control the behavior of the emotional and memory systems.
"""

# Emotional System Configuration
EMOTION_TYPES = [
    'joy', 'sadness', 'fear', 'curiosity',
    'guilt', 'pride', 'love', 'anger'
]

# Emotion decay rates (per hour)
EMOTION_DECAY_RATES = {
    'joy': 0.05,
    'sadness': 0.03,
    'fear': 0.04,
    'curiosity': 0.02,
    'guilt': 0.01,
    'pride': 0.03,
    'love': 0.01,
    'anger': 0.06
}

# Memory System Configuration
MEMORY_TYPES = {
    'EXPERIENTIAL': 'experiential',  # Direct experiences
    'EMOTIONAL': 'emotional',        # Emotional imprints
    'SPIRITUAL': 'spiritual'         # Deep soul insights
}

# Memory decay configuration
MEMORY_DECAY_RATE = 0.01  # Base rate for memory fade
EMOTIONAL_WEIGHT_THRESHOLD = 0.7  # Threshold for strong emotional memories

# Soul Configuration
SOUL_MATURITY_THRESHOLD = 5  # Experience points needed for potential rebirth (reduced for testing)
MUTATION_RATE = 0.1  # Rate of trait mutation during rebirth
TRAIT_INHERITANCE_RATE = 0.7  # Percentage of traits inherited in rebirth

# File Paths
MEMORIES_FILE = 'memories.json'
LEGACY_FILE = 'legacy.json'

# System Constants
MAX_EMOTION_VALUE = 1.0
MIN_EMOTION_VALUE = 0.0
REFLECTION_INTERVAL = 3600  # Time between self-reflections (in seconds)
=======
"""
Configuration settings for the AI Soul Core system.
Contains constants and parameters that control the behavior of the emotional and memory systems.
"""

# Emotional System Configuration
EMOTION_TYPES = [
    'joy', 'sadness', 'fear', 'curiosity',
    'guilt', 'pride', 'love', 'anger'
]

# Emotion decay rates (per hour)
EMOTION_DECAY_RATES = {
    'joy': 0.05,
    'sadness': 0.03,
    'fear': 0.04,
    'curiosity': 0.02,
    'guilt': 0.01,
    'pride': 0.03,
    'love': 0.01,
    'anger': 0.06
}

# Memory System Configuration
MEMORY_TYPES = {
    'EXPERIENTIAL': 'experiential',  # Direct experiences
    'EMOTIONAL': 'emotional',        # Emotional imprints
    'SPIRITUAL': 'spiritual'         # Deep soul insights
}

# Memory decay configuration
MEMORY_DECAY_RATE = 0.01  # Base rate for memory fade
EMOTIONAL_WEIGHT_THRESHOLD = 0.7  # Threshold for strong emotional memories

# Soul Configuration
SOUL_MATURITY_THRESHOLD = 5  # Experience points needed for potential rebirth (reduced for testing)
MUTATION_RATE = 0.1  # Rate of trait mutation during rebirth
TRAIT_INHERITANCE_RATE = 0.7  # Percentage of traits inherited in rebirth

# File Paths
MEMORIES_FILE = 'memories.json'
LEGACY_FILE = 'legacy.json'

# System Constants
MAX_EMOTION_VALUE = 1.0
MIN_EMOTION_VALUE = 0.0
REFLECTION_INTERVAL = 3600  # Time between self-reflections (in seconds)
>>>>>>> 14156adad23afcb4bf5b2152d34f4d8c1007620f
