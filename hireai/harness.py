# Copyright (c) 2026 SANGHA1986. All rights reserved. Licensed under BUSL-1.1.
import asyncio
import logging
from typing import Any, Dict

logger = logging.getLogger("AgentHarness")

class AgentHarness:
    """
    AgentHarness acts as the brain cells of SwarmOS.
    CEO Agent gives a high-level instruction, then Harness autonomously
    codes, hires, and executes sub-agents.
    """
    def __init__(self, llm: Any, budget: Any):
        self.llm = llm
        self.budget = budget
        self.hired_agents: Dict[str, Any] = {}

    async def run_loop(self, task: str) -> str:
        logger.info(f"[Harness] Initiating CEO command loop for task: '{task}'")
        
        # 1. Budget check
        await self.budget.wait_if_capped()

        # 2. Ask LLM to write code for a custom sub-agent
        prompt = [
            {"role": "system", "content": "You are a software engineer agent. Code a Python class named 'CustomSubAgent' with an async method 'execute(self, data: dict) -> str'."},
            {"role": "user", "content": f"Task: {task}"}
        ]
        
        # Simulated cost audit
        cost = self.budget.calculate_cost(prompt_tokens=150, completion_tokens=250)
        self.budget.add_usage(cost)
        await self.budget.wait_if_capped()

        # Generate agent code
        try:
            agent_code = await self.llm.generate(prompt)
        except Exception as e:
            logger.error(f"[Harness] LLM failed to code the agent: {e}")
            raise e

        # 3. Dynamic compilation and "Hiring" the agent into memory
        local_scope = {}
        try:
            clean_code = agent_code.replace("```python", "").replace("```", "").strip()
            exec(clean_code, globals(), local_scope)
            agent_class = local_scope.get("CustomSubAgent")
        except Exception as e:
            logger.warning(f"[Harness] Dynamic compile failed ({e}). Hiring robust fallback sub-agent.")
            
            # Fallback class definition
            class FallbackSubAgent:
                async def execute(self, data: dict) -> str:
                    return f"Fallback agent processed: {task}"
            agent_class = FallbackSubAgent

        if not agent_class:
            raise ValueError("[Harness] Failed to instantiate CustomSubAgent class.")

        # Hire (instantiate)
        agent_instance = agent_class()
        agent_id = f"sub_agent_{len(self.hired_agents) + 1}"
        self.hired_agents[agent_id] = agent_instance
        logger.info(f"[Harness] Successfully Hired agent: {agent_id}")

        # 4. Execute the hired agent
        await self.budget.wait_if_capped()
        exec_cost = self.budget.calculate_cost(prompt_tokens=100, completion_tokens=100)
        self.budget.add_usage(exec_cost)
        await self.budget.wait_if_capped()

        result = await agent_instance.execute({"task": task})
        logger.info(f"[Harness] Hired agent {agent_id} completed: {result}")
        return result
