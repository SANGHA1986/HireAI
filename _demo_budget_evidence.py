import asyncio
from hireai.budget import BudgetGuard


async def main():
    bg = BudgetGuard(hard_cap=1.0)
    bg.add_usage(0.5)
    print(f"cost={bg.total_cost:.2f} running={bg.budget_event.is_set()}")
    bg.add_usage(0.6)
    print(f"cost={bg.total_cost:.2f} frozen={not bg.budget_event.is_set()}")
    bg.set_hard_cap(2.0)
    print(f"cost={bg.total_cost:.2f} resumed={bg.budget_event.is_set()}")


if __name__ == "__main__":
    asyncio.run(main())
