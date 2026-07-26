# Copyright (c) 2026 SANGHA1986. All rights reserved. Licensed under BUSL-1.1.
import asyncio
import logging

logger = logging.getLogger("BudgetGuard")

class BudgetGuard:
    """
    BudgetGuard checks real-time token pricing and freezes execution
    if the budget limit (hard_cap) is reached.
    """
    def __init__(self, hard_cap: float = 100.0):
        self.hard_cap = hard_cap
        self.total_cost = 0.0
        self.budget_event = asyncio.Event()
        self.budget_event.set()  # Allowed to run initially

    def set_hard_cap(self, new_limit: float):
        """Dynamically increase/decrease the budget cap and resume if valid."""
        self.hard_cap = new_limit
        logger.warning(f"[BudgetGuard] 💸 Budget Cap adjusted to: ${self.hard_cap:.2f}")
        if self.total_cost <= self.hard_cap:
            logger.info("[BudgetGuard] 🟢 Resuming execution...")
            self.budget_event.set()

    async def wait_if_capped(self):
        """Await before calling LLMs to ensure budget is under hard_cap."""
        if self.total_cost > self.hard_cap and self.budget_event.is_set():
            logger.critical(f"[BudgetGuard] 🚨 BUDGET EXCEEDED (${self.total_cost:.5f} > ${self.hard_cap:.2f}). Freezing Swarm.")
            self.budget_event.clear()
            
        if not self.budget_event.is_set():
            logger.warning("[BudgetGuard] ⏸️ Swarm frozen, awaiting budget approval...")
            
        await self.budget_event.wait()

    def add_usage(self, cost: float):
        """Register cost and freeze if cap exceeded."""
        self.total_cost += cost
        logger.debug(f"[BudgetGuard] Added cost: ${cost:.6f}. Total: ${self.total_cost:.5f} / Limit: ${self.hard_cap:.2f}")
        if self.total_cost > self.hard_cap:
            self.budget_event.clear()

    def calculate_cost(self, prompt_tokens: int, completion_tokens: int, model: str = "default") -> float:
        """Calculate real-time token cost based on simple pricing map."""
        # Simple standard pricing model
        prompt_rate = 0.0015 / 1000
        completion_rate = 0.002 / 1000
        cost = (prompt_tokens * prompt_rate) + (completion_tokens * completion_rate)
        return cost
