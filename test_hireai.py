import asyncio
import sys
import os
import logging

# Set logging level for the test to see the self-healing in action
logging.getLogger("CEOAgent").setLevel(logging.INFO)

from hireai.core.agents.ceo_agent import CEOAgent
from hireai.core.cost_tracker import CostTracker

async def main():
    print("=== HireAI Framework 1.0.0 Self-Healing Test ===\n")
    
    tracker = CostTracker(hard_cap=10.0)
    
    api_key = os.environ.get("OPENROUTER_API_KEY", "your-api-key-here")
    
    if api_key == "your-api-key-here":
        print("[WARNING] OPENROUTER_API_KEY is not set. The API call will fail if not using a valid key.")
        return
        
    print("--- [TEST] STANDALONE MODE (Intentional Bad Model) ---")
    print("Injecting deprecated model 'google/gemma-7b-it:free' to trigger Self-Healing...")
    
    ceo = CEOAgent(
        provider="openrouter", 
        # Deliberately using a model that caused a 404 error
        model_name="google/gemma-7b-it:free", 
        api_key=api_key
    )
    
    # Watch the CEO autonomously fix the model and execute the mission
    result = await ceo.execute_complex_mission("What is 2+2?")
    
    print("\n--- [FINAL OUTPUT] ---")
    print(result)
    print(f"\nTotal Framework Cost: ${tracker.total_cost:.8f}\n")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Test interrupted.")
    except Exception as e:
        print(f"Error during execution: {e}")
        sys.exit(1)
