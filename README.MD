# HireAI

HireAI prevents AI agents from burning your API budget.  
Most AI agent frameworks optimize for autonomy. HireAI optimizes for survival.  
Your agents can think freely. They cannot spend freely.

**Positioning:** The Financial Operating System for AI Agents  
(**Budget-Native AI Agent Operating System**)

---

## 🇺🇸 English

### Problem
You wake up and your agent has spent your monthly API budget overnight.
Traditional orchestration frameworks help agents do more work, but they do not
treat cost control as a first-class safety boundary.

### Solution
HireAI freezes spending before damage spreads.

- At your hard cap (for example, $50), API execution pauses automatically.
- The system waits for admin approval.
- Work resumes from where it stopped after approval.

### 3-Second Flow

```text
[ AI Agent Task Running ]
          |
          v
[ API Cost Reaches $50 ] --(over cap)--> [ Dynamic Pause: Auto Freeze ]
                                                     |
                                                     v
[ Task Completed ] <--------(resume)-------- [ Admin Approval: Resume Engine ]
```

### Core Components
1. **CostTracker**: real-time cost accounting per run
2. **Dynamic Pause**: automatic hard-cap freeze
3. **Resume Engine**: controlled restart from paused state

### Installation
```bash
git clone https://github.com/SANGHA1986/HireAI.git
cd HireAI
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e .
```

### Quick Start
```bash
python test_budget_harness.py
```

### Evidence (Demo)
This is a reproducible local demo result (not a customer case study).

```text
$ python test_budget_harness.py
PASS: harness result -> Mock result for: Summarize sales data
PASS: total cost -> 0.001075
PASS: hired agents -> ['sub_agent_1']

$ BudgetGuard hard_cap=1.0
cost 0.5 running True
cost 1.1 frozen True
resumed True
```

### License
This project is licensed under **BUSL 1.1**.
See `LICENSE.md` for commercial usage terms.

---

## 🇰🇷 한국어

### 문제
자고 일어났더니 에이전트가 API 비용을 한꺼번에 소진하는 상황이 자주 발생합니다.
기존 에이전트 프레임워크는 "더 많은 작업"에는 강하지만, "비용 생존성"은 약합니다.

### 해결
HireAI는 비용 폭탄이 발생하기 전에 자동으로 동결합니다.

- 설정한 하드캡(예: $50)에 도달하면 즉시 자동 일시정지
- 관리자 승인 전까지 추가 비용 발생 차단
- 승인 후 멈춘 지점부터 작업 재개

### 3초 이해 흐름도

```text
[ AI 에이전트 작업 실행 ]
          |
          v
[ API 비용 $50 도달 ] --(비용 초과)--> [ Dynamic Pause: 자동 일시정지 ]
                                                     |
                                                     v
[ 작업 완료 ] <--------(작업 재개)-------- [ 관리자 승인: Resume Engine ]
```

### 핵심 구성 요소
1. **CostTracker**: 실행 단위 실시간 비용 집계
2. **Dynamic Pause**: 하드캡 초과 시 자동 동결
3. **Resume Engine**: 승인 후 안전 재개

### 설치 방법
```bash
git clone https://github.com/SANGHA1986/HireAI.git
cd HireAI
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e .
```

### 빠른 시작
```bash
python test_budget_harness.py
```

### Evidence (데모)
아래는 실제 고객 사례가 아니라, 로컬에서 재현 가능한 데모 결과입니다.

```text
$ python test_budget_harness.py
PASS: harness result -> Mock result for: Summarize sales data
PASS: total cost -> 0.001075
PASS: hired agents -> ['sub_agent_1']

$ BudgetGuard hard_cap=1.0
cost 0.5 running True
cost 1.1 frozen True
resumed True
```

### 라이선스 안내
본 프로젝트는 **BUSL 1.1** 라이선스를 따릅니다.
상업적 이용 조건은 `LICENSE.md`를 확인하세요.