import math

def get_valid_input(prompt, is_float=False):
    """사용자 입력을 안전하게 처리하는 함수"""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'q': return 'q'
        try:
            val = float(user_input) if is_float else int(user_input)
            return val
        except ValueError:
            print("⚠️ 숫자로 입력해주세요 (종료하려면 'q')")

def mode_1_reach_probability(p):
    """[기능 1] 특정 누적 확률 도달까지 필요한 사냥수"""
    print(f"\n[ 확률 도달 분석 (드랍률: {p*100}%) ]")
    print("-" * 45)
    # 누적 확률 P를 달성하기 위한 n: (1-p)^n = 1-P => n = log(1-P) / log(1-p)
    targets = [50, 80, 90, 99, 99.9]
    for target_pct in targets:
        target_val = target_pct / 100
        n = math.log(1 - target_val) / math.log(1 - p)
        print(f" > {target_pct:>4}% 확률로 득템 가능  |  {math.ceil(n):>12,}마리")
    print("-" * 45)

def mode_2_target_count(p):
    """[기능 2] 아이템 k개를 먹기 위한 평균 사냥수"""
    k = get_valid_input("\n > 목표 아이템 개수를 입력하세요: ")
    if k == 'q': return
    
    # 평균(기댓값) E = k / p
    expected = k / p
    print(f"\n[ 아이템 {k}개 획득 기댓값 ]")
    print(f" > 통계적 평균 사냥수: {math.ceil(expected):,}마리")
    print(f" > 운이 좋은 편(25%): {math.ceil(expected * 0.5):,}마리 수준")
    print(f" > 운이 나쁜 편(25%): {math.ceil(expected * 1.5):,}마리 수준")

def mode_3_unluck_test(p):
    """[기능 3] 기우제 모드 (현재 불운도 측정)"""
    n = get_valid_input("\n > 현재까지 잡은 몬스터 수를 입력하세요: ")
    if n == 'q': return
    
    # 한 번도 못 먹었을 확률 (불운도)
    fail_rate = (1 - p) ** n
    success_rate = (1 - fail_rate) * 100
    
    print("\n" + "!"*50)
    print(f" > 분석 결과: {n:,}마리 사냥 중 무득템")
    print(f" > 남들은 {success_rate:.4f}% 확률로 이미 먹었습니다.")
    print(f" > 당신은 상위 [ {fail_rate*100:.4f}% ]의 불운아입니다.")
    
    if fail_rate < 0.01:
        print(" > 이건 확률이 아니라 저주입니다. 운영자를 찾아가세요.")
    elif fail_rate < 0.1:
        print(" > 통계적으로 '곧' 나올 차례입니다. 조금만 더!")
    else:
        print(" > 아직은 '정상 범위'입니다. 기우제를 더 지내세요.")
    print("!"*50)

def main():
    print("="*50)
    print("   🍀 초정밀 득템 & 기우제 계산기 🍀")
    print("="*50)

    while True:
        prob_input = get_valid_input("\n[단계 1] 기본 드랍 확률을 입력하세요 (%, 종료: 'q'): ", is_float=True)
        if prob_input == 'q': break
        
        p = prob_input / 100
        if not (0 < p < 1):
            print("⚠️ 확률은 0.0001% ~ 99.99% 사이로 입력해주세요.")
            continue

        while True:
            print(f"\n[ 현재 설정 확률: {prob_input}% ]")
            print(" 1. 목표 확률 도달 계산 (몇 마리 잡아야 먹을까?)")
            print(" 2. 평균 획득수 계산 (아이템 n개 먹을 때까지)")
            print(" 3. 기우제 모드 (내 불운 테스트)")
            print(" b. 확률 다시 입력하기 (Back)")
            print(" q. 프로그램 종료")
            
            choice = input(" > 선택: ").strip().lower()
            
            if choice == '1': mode_1_reach_probability(p)
            elif choice == '2': mode_2_target_count(p)
            elif choice == '3': mode_3_unluck_test(p)
            elif choice == 'b': break
            elif choice == 'q': return
            else: print("⚠️ 올바른 번호를 선택해주세요.")

if __name__ == "__main__":
    main()