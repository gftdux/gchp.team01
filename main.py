import time
from get_result_module import get_result_module

# 질문
HO_questions = [
    "그녀가 내 번호를 물어보고, 번호를 교환하게 되었다./n 그녀는 영어교육과 26학번이라고 자신을 소개했다./n 그녀에게서 카톡이 왔다. “내일 시간되면 같이 밥 먹을래?”",
    "HO 2",
    "HO 3"
]

KM_questions = [
    "KM 1",
    "KM 2",
    "KM 3"
]

AD_questions = [
    "AD 1",
    "AD 2",
    "AD 3"
]

JB_questions = [
    "JB 1",
    "JB 2",
    "JB 3"
]

# 대답 
H_responses = [
    'H1',
    'H2',
    'H3'
]

O_responses = [
    "O1",    
    "O2",
    "O3"
]

K_responses = [
    "K1",
    "K2",
    "K3"
]

M_responses = [
    "M1",
    "M2",
    "M3"
]

A_responses = [
    "A1",
    "A2",
    "A3"
]

D_responses = [
    "D1",
    "D2",
    "D3"
]

J_responses = [
    "J1",
    "J2",
    "J3"
]

B_responses = [
    "B1",
    "B2",
    "B3"
]

# 딕셔너리
user_mbti = {'H': 0, 'O': 0, 'K': 0, 'M': 0, 'A': 0, 'D': 0, 'J': 0, 'B': 0}

def get_choice():
    #사용자의 입력을 받는 함수
    while True:
        try:
            choice = int(input("(1 또는 2를 입력하세요): "))
            if choice in [1, 2]:
                return choice
            else:
                print("1 또는 2를 입력해주세요.")
        except ValueError:
            print("숫자로 입력해주세요.")


    # 출력문 디자인 및 설계 
def dialogue(set_idx):
    if set_idx == 0:
        time.sleep(1.2)
        print("\033[H\033[J", end="")
        print(".", end="", flush=True)
        time.sleep(1)
        print(".", end="", flush=True)
        time.sleep(1)
        print(".", flush=True)
        time.sleep(1)
        print("그녀와의 대화\n")
        time.sleep(1.4)
        print("시작!\n\n")
        time.sleep(1.35)

        print(r"""
                                      .     .
                       .          .                    .  /\   .
        .                                       *         `'
                  *         ,,, ,,,                       .           .
                          ,'   '   `'',,,             .         .
             .          .'               `'',,,
                     .,'                 --.;:.:
       .-,        .-;       ,/.   /\         ::.\         .---.
       `-'       ;::'          .  \/    .   ::::.`-.    .'     \      *
      .        ,:':;,...;_ _'.''-.___    \.::;::|8:.|,e/    .   b
              .;' '  :::|,'./|    ---\,,::\:|8|e|88:\8' _
    .         |      ,;/.//|:|     |`\\ \;;-|8888888|'.8e'--.         .
         .   ,|  ,,;;///./':(||    ` `||||:\88888888||8'     \
             |:.::;//.|'//|||`|    |  `\\||\::`8888888'_      \
    /\       |:::///.|;|..---';.  `----.\|).|.|..`888|8e=--.   |     ,-,
    \/       ||:|/.|:,'|',===;.-   ====-.:\.||.\\.'888'     \  U     `-'
        .    |||/.:||(.-=';.| \\|   `..`"|\;..|....\88ee     \      .
              \<|..'.|.\ ___'       ._'_,\\|'\|.|.|\88b'\     b
              .'|:|;.|||`  '           ' |'|.\'.|..|.qp  |
    .         | |.(:.|.`        \         ';':.)|.|.| .._ U
              ` |.`.,`|.\               /|:.|.|.,(..\..:;-      .      .
        *       /\.||..|.`      _      '||:.:.`.|...|...-.
   .           ' |.`..).,|\    `-`    /|:(|:.):||..|.|. .:`_
                 |..).|.|..`..      .':|:||:.|.')`.\.\ .\--.      *
                 /..'|'.| |||  ._.'.||;|:;|:.|/||:` \`,..\._           .
      .   .     '('|:|`..'_;|    .:.|=---.;/|| |||  \-oo.|__
                .' / |`|.'-='-------`"'::.| '|  |`. \8oooooo\
              .'.   .'|'|_   __,--'...;:--'  |  `.  .8bod888o|  .   /\
         *   .'. '  | :::|`-' __.---' _++-'  '    ' \88e8888o|      `'
 .           ;-'   ,,:::|---'     ___+++-       :   \8888888o`.
            ,8'  ,:::::'|_o-o----'_++++-   :    :. \.8888888oo|    .
       .   ,8/  ,:::' .|`88 _.--.++++-    ::: . ::\o88888888oo|
    .     ,88/     . . |.`8'__.-',-'      :::  .::\o88888888bo`.
          |8o/  :.  . .| `|\    /,          ::. :\o8888888888oo|     *
          |8o/  :   :. |/ | \   /,       .  :: .\o88888888888oo|        .
         ,888o/    :. .|  |     /, __   . . :: |o888888888888bo`.  .
         |8888o/: :  .|...|    .--' -'     . :|o88888888888888oo|
    .   ,88888o/ :  . |...|/..|::=---,  : .  |o888888888888888oo|
        |88888o/   . .|...|.. |:',__   :   .|o8888888888888888bo`.    .
        |888888o/   . |...|. |:::__ '  :: .|o888888X88888888888oo|
       ,88888888o|   .|b..|. |::,--'  .:::|88888888X88888888888oo|
  .    |8888X888o/   .d8b----'::|    . .::|88888888188888888888bo`. """)
        
        
        time.sleep(2)   # 시작 
        print("\n\n반짝이는 눈동자, 귀여운 목소리, 그리고 항상 밝은 웃음을 띄고 있는 그녀,\n그녀를 보기만 해도 마음이 설레고, 가슴이 쿵쾅거리는 것을 느꼈다.\n\n")
        time.sleep(2)
    else:
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...\n")
        time.sleep(2)
     

    # H vs O
    print(f"{HO_questions[set_idx]}\n")
    time.sleep(2)
    print(f"1: {H_responses[set_idx]}")
    print(f"2: {O_responses[set_idx]}")
    
    choice = get_choice()
    if choice == 1:
        user_mbti['H'] += 1
    else:
        user_mbti['O'] += 1

    print(".")
    time.sleep(0.7)
    print("..")
    time.sleep(0.7)
    print("...\n")
    time.sleep(1.5)

    # K vs M
    print(f"{KM_questions[set_idx]}\n")
    time.sleep(2)
    print(f"1: {K_responses[set_idx]}")
    print(f"2: {M_responses[set_idx]}")
    
    choice = get_choice()
    if choice == 1:
        user_mbti['K'] += 1
    else:
        user_mbti['M'] += 1

    print(".")
    time.sleep(0.7)
    print("..")
    time.sleep(0.7)
    print("...\n")
    time.sleep(1.5)

    # A vs D
    print(f"{AD_questions[set_idx]}\n")
    time.sleep(2)
    print(f"1: {A_responses[set_idx]}")
    print(f"2: {D_responses[set_idx]}")
    
    choice = get_choice()
    if choice == 1:
        user_mbti['A'] += 1
    else:
        user_mbti['D'] += 1

    print(".")
    time.sleep(0.7)
    print("..")
    time.sleep(0.7)
    print("...\n")
    time.sleep(1.5)

    # J vs B
    print(f"{JB_questions[set_idx]}\n")
    time.sleep(2)
    print(f"1: {J_responses[set_idx]}")
    print(f"2: {B_responses[set_idx]}")
    
    choice = get_choice()
    if choice == 1:
        user_mbti['J'] += 1
    else:
        user_mbti['B'] += 1

# 마무리 멘트
def final_dialogue():
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    print("그녀는 나의 말에 미소를 지으며 고개를 끄덕였다. 그날 밤, 그녀와의 첫 데이트, 그리고 그녀에게 고백한 그 순간, 그 모든 것이 나에게는 소중한 추억이었다.")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...\n")
    time.sleep(2)

# 성격유형 판단
def determine_mbti():
    mbti_result = ""
    mbti_result += 'H' if user_mbti['H'] > user_mbti['O'] else 'O'
    mbti_result += 'K' if user_mbti['K'] > user_mbti['M'] else 'M'
    mbti_result += 'A' if user_mbti['A'] > user_mbti['D'] else 'D'
    mbti_result += 'J' if user_mbti['J'] > user_mbti['B'] else 'B'
    
    return mbti_result


# 메인 실행부
if __name__ == "__main__":
    for i in range(3):
        dialogue(i)
    final_dialogue()
    mbti_result = determine_mbti()
    print(f"당신의 연애 스타일 코드는 {mbti_result}입니다.")
    explainer = get_result_module()
    explain_result = explainer.get_result(mbti_result)
    print(explain_result)
