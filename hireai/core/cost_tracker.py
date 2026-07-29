# Copyright (c) 2026 SANGHA1986. All rights reserved. Licensed under BUSL-1.1.
import logging

logger = logging.getLogger("CostTracker")


class CostTracker:
    """
    경량 비용 추적기. AgentHarness 외부에서 별도 집계가 필요할 때 사용.
    BudgetGuard와 독립적으로 동작하며, 분석/리포트 목적으로 쓴다.
    """
    def __init__(self, hard_cap: float = 100.0):
        self.hard_cap = hard_cap
        self.total_cost: float = 0.0

    def add(self, amount: float):
        self.total_cost += amount
        logger.debug(f"[CostTracker] +{amount:.6f} -> total {self.total_cost:.6f}")
        if self.total_cost > self.hard_cap:
            logger.warning(f"[CostTracker] Hard cap exceeded: {self.total_cost:.4f} > {self.hard_cap}")

    def reset(self):
        self.total_cost = 0.0

    def remaining(self) -> float:
        return max(0.0, self.hard_cap - self.total_cost)

