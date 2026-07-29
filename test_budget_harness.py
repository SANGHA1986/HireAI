import asyncio
import sys
sys.path.insert(0, '.')

from hireai.harness import AgentHarness
from hireai.budget import BudgetGuard


class MockLLM:
    async def generate(self, messages):
        return (
            "class CustomSubAgent:\n"
            "    async def execute(self, data: dict) -> str:\n"
            "        return f\"Mock result for: {data.get('task')}\"\n"
        )


async def test_harness():
    bg = BudgetGuard(hard_cap=10.0)
    harness = AgentHarness(llm=MockLLM(), budget=bg)
    result = await harness.run_loop("Summarize sales data")
    assert "Mock result" in result, f"Unexpected result: {result}"
    print(f"PASS: harness result -> {result}")
    print(f"PASS: total cost -> {bg.total_cost:.6f}")
    print(f"PASS: hired agents -> {list(harness.hired_agents.keys())}")


if __name__ == "__main__":
    asyncio.run(test_harness())
    print("ALL HARNESS TESTS PASSED")
