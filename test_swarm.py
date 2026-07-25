import asyncio
import sys
import os
import logging

logging.getLogger("CEOAgent").setLevel(logging.INFO)
logging.getLogger("CostTracker").setLevel(logging.DEBUG)
logging.getLogger("ModelRouter").setLevel(logging.WARNING)

from hireai.core.agents.ceo_agent import CEOAgent
from hireai.core.cost_tracker import CostTracker

async def approve_budget_webhook(tracker: CostTracker):
    """Simulates an external webhook (e.g. Arkcoder Web UI) unpausing the Swarm."""
    await asyncio.sleep(5)
    print("\n[WEBHOOK] User clicked 'Approve' on the UI!")
    tracker.set_hard_cap(100.0) # Increase cap to resume work

async def swarm_worker(ceo: CEOAgent, worker_id: int):
    """Spawns an agent and immediately executes a task, participating in the 50-agent swarm."""
    agent_id = await ceo.spawn_agent(role=f"SwarmWorker-{worker_id}")
    result = await ceo.delegate_task(agent_id, f"Report status for worker {worker_id}", {"id": worker_id})
    print(f"Worker {worker_id} Finished.")
    return result

async def main():
    print("=========================================================")
    print("=== HireAI Limitless Swarm & Auto-Retry Test (50 Agents) ===")
    print("=========================================================\n")
    
    # 1. Initialize Tracker with very low cap to force a Human-in-the-loop pause immediately
    tracker = CostTracker(hard_cap=0.0)
    
    api_key = os.environ.get("OPENROUTER_API_KEY", "your-api-key-here")
    if api_key == "your-api-key-here":
        print("[WARNING] OPENROUTER_API_KEY is not set. Execution will fail without real API.")
        # Proceed anyway to demonstrate architecture
        
    print("--- [STEP 1] CEO Initializing with ECONOMY Cost Tier ---")
    # Using 'economy' means CEO will dynamically fetch openrouter models, parse prices, 
    # and automatically pick a 0-cost model (like google/gemma-7b-it:free) for the entire swarm.
    ceo = CEOAgent(
        provider="openrouter", 
        model_name="invalid-model-name-to-force-fallback", 
        api_key=api_key,
        cost_tier="economy"
    )
    
    # 2. Start the Webhook listener in the background to rescue the swarm when it freezes
    asyncio.create_task(approve_budget_webhook(tracker))
    
    # 3. Launch 50 Agents Concurrently!
    print("\n--- [STEP 2] Launching 50 Agents in Parallel! (Expect 429 Auto-Retry) ---")
    tasks = [swarm_worker(ceo, i) for i in range(50)]
    
    # This will freeze instantly because hard_cap is 0.0. 
    # After 5 seconds, the webhook fires, cap increases, and all 50 fire at OpenRouter simultaneously.
    # OpenRouter will likely return 429 Too Many Requests, which the Router will catch and Exponential Backoff.
    await asyncio.gather(*tasks)
    
    print("\n--- [FINAL OUTPUT] ---")
    print("All 50 Swarm Agents completed their missions successfully despite Rate Limits!")
    print(f"Total Swarm Cost: ${tracker.total_cost:.8f}\n")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Test interrupted.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
