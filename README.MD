# HireAI: Budget-Native Swarm OS 🚀

*(English below / 한국어 설명은 아래에 있습니다)*

---

## 🇺🇸 English

HireAI is not just another agent orchestrator. It is a **"Budget-Native Swarm OS"** where cost protection is the highest priority. Existing frameworks like Langchain, CrewAI, and AutoGen are not competitors; they operate as **'SubAgent adapters (subordinate workers)'** strictly under our CostTracker's budget control.

### ✨ Key Features
1. **Top-level CEO Orchestration**: Evaluates the overall situation and delegates tasks to sub-agents.
2. **Real-time CostTracker**: Operates as a 1st-class citizen, ensuring not a single cent of budget overrun is allowed.
3. **Dynamic Pause (Freeze)**: Instantly and safely freezes all sub-agent API calls the moment the budget limit (Hard Cap) is reached.
4. **Resume Engine**: When the admin approves additional budget in the dashboard, operations seamlessly resume exactly where they stopped to complete the mission.

### 📦 Installation
```bash
git clone https://github.com/SANGHA1986/HireAI.git
cd HireAI
python -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows
pip install -e .
```

### 🚀 Quick Start (Test Pause/Resume)
See the core functionality in action without needing a real API key:
```bash
python test_os.py
```

### 📜 License
This project is licensed under **BUSL 1.1**. It is 100% free for personal, non-commercial, academic use, and for small businesses with an annual revenue under 300 million KRW. However, commercial SaaS services or enterprise adoption (revenue >= 300 million KRW) strictly require a paid commercial license. See `LICENSE.md` for details.

---

## 🇰🇷 한국어 (Korean)

HireAI는 단순한 에이전트 오케스트레이터가 아닙니다. **"돈을 먼저 지키는 AI 회사 엔진(Budget-Native Swarm OS)"**입니다.
Langchain, CrewAI, AutoGen과 같은 기존 프레임워크들은 우리가 경쟁할 대상이 아니라, 철저히 예산 통제(CostTracker) 아래에서 움직이는 **'SubAgent 어댑터(하청 워커)'**로 작동합니다.

### ✨ 핵심 기능
1. **최상위 CEO 오케스트레이션**: 전체 상황을 판단하여 하청 에이전트들에게 작업을 위임합니다.
2. **실시간 비용 추적기 (CostTracker)**: 1급 기능으로 작동하며 1원의 예산 초과도 허용하지 않습니다.
3. **동적 동결 (Dynamic Pause)**: 설정된 예산 한도(Hard Cap)에 도달하는 즉시 모든 하청 에이전트들의 API 호출을 안전하게 얼려버립니다.
4. **재개 엔진 (Resume Engine)**: 관리자 대시보드에서 추가 예산을 승인하면, 정확히 멈춘 시점부터 다시 풀려서 작업을 끝까지 완수합니다.

### 📦 설치 방법
```bash
git clone https://github.com/SANGHA1986/HireAI.git
cd HireAI
python -m venv venv
source venv/bin/activate # Windows의 경우 venv\Scripts\activate
pip install -e .
```

### 🚀 빠른 시작 (동결/재개 테스트)
API 키 없이 시뮬레이션으로 동결/재개 흐름을 바로 테스트해 볼 수 있습니다:
```bash
python test_os.py
```

### 📜 라이선스 안내
본 프로젝트는 **BUSL 1.1** 라이선스를 따릅니다. 개인 연구, 비상업적 이용, 연 매출 3억 원 이하의 개인 및 영세 기업은 100% 무료로 사용할 수 있습니다. 단, 이를 활용한 상업적 SaaS 서비스 제공이나 연 매출 3억 원 이상의 대기업 무단 도입은 엄격히 금지되며, 별도의 유료 상업 라이선스가 필요합니다. 자세한 내용은 `LICENSE.md`를 참고하세요.