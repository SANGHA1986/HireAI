import asyncio
import logging
import sys

# Setup logging to show the SwarmOS and CostTracker clearly
logging.basicConfig(level=logging.INFO, format='%(message)s')
# Override specifically for our test
logging.getLogger("SwarmOS").setLevel(logging.INFO)
logging.getLogger("CostTracker").setLevel(logging.DEBUG)
logging.getLogger("CEOAgent").setLevel(logging.INFO)
logging.getLogger("SubAgent").setLevel(logging.WARNING)

from hireai.core.engine import SwarmOS
from hireai.core.models.router import ModelRouter

# Mock the ModelRouter so we can test the OS without real API keys
async def mock_generate(provider, model_name, api_key, prompt, max_retries=5):
    # Simulate a small delay
    await asyncio.sleep(0.5)
    return f"[Mocked Output for {prompt[:20]}...]", {"prompt_tokens": 1000, "completion_tokens": 1000}

ModelRouter.generate = staticmethod(mock_generate)

async def admin_dashboard(os_engine: SwarmOS):
    """
    Simulates a human-in-the-loop interacting with the dashboard.
    When the OS freezes due to budget constraints, the admin approves more funds.
    """
    while True:
        await asyncio.sleep(2)
        status = os_engine.get_status()
        if status["is_paused"]:
            print("\n[Admin Dashboard] [ALERT] SwarmOS is frozen due to Budget Cap!")
            print(f"[Admin Dashboard] Current Cost: ${status['total_cost']:.2f} / Cap: ${status['hard_cap']:.2f}")
            print("[Admin Dashboard] Approving +$50.00 to resume operations...\n")
            await asyncio.sleep(1) # Simulate think time
            os_engine.resume(50.0)
            break # After one resume, we let it finish

async def main():
    print("=========================================================")
    print("=== HireAI Budget-Native Swarm OS Demonstration       ===")
    print("=========================================================\n")
    
    # 1. Initialize OS with an artificially low budget to force a freeze
    print("--- [STEP 1] Booting SwarmOS with $0.00 Budget Cap ---")
    
    # We use a dummy model name to simulate local/standalone processing 
    # without needing a real API key for this architectural test.
    os_engine = SwarmOS(
        provider="dummy",
        model_name="dummy/model",
        initial_budget=0.0,
        cost_tier="standard"
    )
    
    # Simulate some initial cost to immediately hit the cap upon first generation
    # Actually, if cap is 0.0, it will freeze immediately before the first API call.
    
    # 2. Run the admin dashboard concurrently
    asyncio.create_task(admin_dashboard(os_engine))
    
    # 3. Start a complex mission
    print("\n--- [STEP 2] Submitting Complex Mission to OS ---")
    mission = "Analyze the market trends and write a 10-page report."
    
    # Force pricing so our mocked usage adds actual cost
    os_engine.ceo.pricing_map["dummy/model"] = {"prompt": 1.0, "completion": 1.0}
    
    try:
        # This will freeze because the budget is 0.0
        # The admin_dashboard will see the freeze, and resume it.
        result = await os_engine.execute_mission(mission)
        print("\n--- [STEP 3] Mission Accomplished ---")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error during OS execution: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Test interrupted.")
    except Exception as e:
        sys.exit(1)
