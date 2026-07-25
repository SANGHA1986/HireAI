# HireAI: Budget-Native Swarm OS 🚀

HireAI는 단순한 에이전트 오케스트레이터가 아닙니다. **"돈을 먼저 지키는 AI 회사 엔진(Budget-Native Swarm OS)"**입니다.
Langchain, CrewAI, AutoGen과 같은 기존 프레임워크들은 우리가 경쟁할 대상이 아니라, 철저히 예산 통제(CostTracker) 아래에서 움직이는 **'SubAgent 어댑터(하청 워커)'**로 작동합니다.

## ✨ 핵심 기능

1. **최상위 CEO 오케스트레이션**: 전체 상황을 판단하여 하청 에이전트들에게 작업을 위임합니다.
2. **실시간 비용 추적기 (CostTracker)**: 1급 기능으로 작동하며 1원의 예산 초과도 허용하지 않습니다.
3. **동적 동결 (Dynamic Pause)**: 설정된 예산 한도(Hard Cap)에 도달하는 즉시 모든 하청 에이전트들의 API 호출을 안전하게 얼려버립니다.
4. **재개 엔진 (Resume Engine)**: 관리자 대시보드에서 추가 예산을 승인하면, 정확히 멈춘 시점부터 다시 풀려서 작업을 끝까지 완수합니다.

## 📦 설치 방법

```bash
# 1. 저장소 클론
git clone https://github.com/your-username/HireAI.git
cd HireAI

# 2. 가상환경 생성 및 활성화 (권장)
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. 설치
pip install -e .
```

## 🚀 빠른 시작 (동결/재개 테스트)

HireAI의 가장 강력한 기능인 **"예산 한도 도달 시 동결(Pause) 및 승인 후 재개(Resume)"** 흐름을 직접 눈으로 확인해 보세요. API 키 없이도 동작을 시뮬레이션할 수 있습니다.

```bash
# 데모 테스트 스크립트 실행
python test_os.py
```

**[실행 결과 시나리오]**
1. 예산 `$0.00`으로 OS가 부팅됩니다.
2. 미션이 주어지고 첫 번째 프롬프트 토큰이 소비되자마자 즉각 모든 시스템이 동결(`Pause`)됩니다.
3. 대시보드에서 예산(+$50.00)을 추가로 승인하는 시뮬레이션 이벤트가 발생합니다.
4. 예산이 넉넉해진 OS가 중단된 작업부터 다시 재개(`Resume`)하여 미션을 성공적으로 완수합니다.

## 🧱 구조 (Architecture)

- `hireai/core/engine.py`: SwarmOS 메인 엔진 (CEO 및 CostTracker 묶음 관리)
- `hireai/core/cost_tracker.py`: 자금 모니터링 및 실시간 동결/재개 제어 담당
- `hireai/core/agents/ceo_agent.py`: 전체 미션을 쪼개고 하위 에이전트에게 작업을 안전하게 위임
- `hireai/core/agents/sub_agent.py`: Langchain, CrewAI 등 외부 도구를 래핑하여 명령만 수행하는 순수 하청 워커