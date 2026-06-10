import time
import sys
from explain_module import validate_openrouter_api_key
from get_result_module import get_result_module


def typewriter(text, delay=0.07):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

def typewriter2(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

# 딕셔너리
user_mbti = {'H': 0, 'O': 0, 'K': 0, 'M': 0, 'A': 0, 'D': 0, 'J': 0, 'B': 0}

def get_choice():
    #사용자의 입력을 받는 함수
    while True:
        try:
            choice = 0
            choice = int(input("(1 또는 2를 입력하세요): "))
            if choice in [1, 2]:
                return choice
            else:
                print("1 또는 2를 입력해주세요.")
                time.sleep(0.6)
                sys.stdout.write("\033[F\033[K" * 2)
                time.sleep(0.2)

        except ValueError:
            print("숫자로 입력해주세요.")
            time.sleep(0.6)
            sys.stdout.write("\033[F\033[K" * 2)
            time.sleep(0.2)

            
def print_transition():
    print(".")
    time.sleep(0.7)
    print("..")
    time.sleep(0.7)
    print("...")
    time.sleep(0.7)
    sys.stdout.write("\033[F\033[K" * 15)
    time.sleep(1)


# 출력문 디자인 및 설계 
def play_intro(set_idx):
    if set_idx == 0:
        time.sleep(1.2)
        print("\033[H\033[J", end="")
        print(".", end="", flush=True)
        time.sleep(1)
        print(".", end="", flush=True)
        time.sleep(1)
        print(".", flush=True)
        time.sleep(1)
        typewriter2('본 프로그램은 미연시를 플레이하며 당신의 연애 스타일을 분석하는 가상 연애 시뮬레이터입니다.\n실제 연애 상황이라 생각하고 답변하여, 몰랐던 당신의 연애 유형을 발견해보세요!\n\n터미널 창의 크기를 키우고(최대화), 글자크기를 줄이면 더 몰입감 있는 플레이가 가능합니다!')
        time.sleep(1.1)
        print("\033[H\033[J", end="")
        time.sleep(1)
        print(".", end="", flush=True)
        time.sleep(0.75)
        print(".", end="", flush=True)
        time.sleep(0.75)
        print(".", flush=True)
        time.sleep(0.85)
        print("""╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                💘  가상 연애 시뮬레이션  💘                  ║
║                  당신의 연애 유형을 찾아서                   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝""")
        
        time.sleep(1)

        typewriter2(f"\n\n안녕하세요! 지금부터 당신의 연애 이야기를 시작합니다. 💕\n")
        time.sleep(1)
        print("\033[H\033[J", end="")

        time.sleep(1.3)

        print(".", end="", flush=True)
        time.sleep(0.8)
        print(".", end="", flush=True)
        time.sleep(0.8)
        print(".", flush=True)
        time.sleep(1)
        print("\033[H\033[J", end="")
        time.sleep(0.6)

        print(r"""
                *         ,,,`''`''`',,,,             .         .
             .          .'               `'',,,            .        .
                     .,'                 --.;:.:        *
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
          |8o/  :   :. |/ | \   /,       .  :: .\o88888888888oo|    """)
         
        
        time.sleep(1.7)   # 시작 
    else:
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...\n")
        time.sleep(1.5)

# 질문
HO_questions = [
    "그녀가 내 번호를 물어보고, 번호를 교환하게 되었다.\n그녀는 영어교육과 26학번이라고 자신을 소개했다.\n그날 저녁, 그녀에게서 카톡이 왔다. “내일 시간되면 같이 밥 먹을래?”",
    "디엠을 주고받으며 벌써 밤이 되는데, 계속 그녀 생각이 난다.\n어느새 그녀를 너무너무 좋아하게 된 것 같다.",
    "그녀와 부쩍 가까워지고, 어느날 교양수업이 끝난 후 그녀가 주말에 만나서 놀자고 한다.\n“뭐 하고 싶어?” 그녀가 묻는다."
]

KM_questions = [
    "수업이 끝나고 강의실을 나가려고 할 때, 그녀가 내 앞에 필통을 떨어뜨렸다.\n나는 반사적으로 그녀의 필통을 주워 건네주었다.",
    "그녀에게서 연락이 왔다.\n“사실 어제 같이 있던 남자 친오빠인데 혹시 너 오해할까봐 말해주려고.. ”",
    "집에 가는 길에, 꽃집과 옷가게가 눈앞에 보인다.\n아무래도 그녀와의 데이트를 위해 무언가 준비해야겠다는 생각이 든다."
]

AD_questions = [
    "오늘은 교양 수업 첫날이다. 310관에 들어가서 강의실을 찾아갔다.\n적당한 자리를 찾으려 고개를 돌린 순간, 내 시선이 한곳에 멈췄다.\n‘와… 진짜 예쁘다.’",
    "그녀에게서 연락이 왔다.\n잠깐 할 말이 있으니 나오라고 한다.",
    "드디어 데이트 날이다.\n그녀와 나란히 걷다 우연히 손이 스쳐 분위기가 어색해졌다."
]

JB_questions = [
    "같이 맛있게 밥을 먹고, 한강에서 단둘이 산책도 하였다.\n데이트가 끝나고 집에 와서, 아쉬운 마음에 그녀에게 연락한다.",
    "다음날, 수업이 끝나고 집에 가려는데,\n카우버거 창 너머에서 그녀가 어떤 남자와 단둘이 밥 먹는 걸 보게 됐다.",
    "오늘 데이트는 성공적이었다. 데이트가 끝나고 그녀의 집 앞에서 사귀자고 말을 꺼냈다.\n그녀가 아무말을 안 한다.. 고민 중인듯 하다."
]

# 대답 
H_responses = [
    '같이 309관 학식을 먹자고 제안한다.',
    '시간이 늦었으니 그냥 전화하자고 한다.',
    '만화카페나 카페같은 조용한 곳에 가서 놀자고 한다.'
]

O_responses = [
    "정문쪽에 있는 식당에 가자고 제안한다.",    
    "잠깐이라도 보러 나가자. 나갈 준비를 한다.",
    "시내를 돌아다니며 놀자고 한다."
]

K_responses = [
    "“괜찮아? 여기.” 다정하게 말을 걸면서 건네준다.",
    "“오해 안 했으니까 걱정 안 해도 돼.”",
    "주말에 그녀 만나기 전에 꽃 한 송이를 사가서 주자."
]

M_responses = [
    "말없이 슥 집어서 건네준다.",
    "“그랬구나. 알겠어”",
    "그때 입을 깔끔한 옷을 사자."
]

A_responses = [
    "그냥 빈 자리에 적당히 앉고 멀리서 바라본다.",
    "예감이 좋지 않으니 지금은 바쁘다고 말한다.",
    "재밌는 이야기를 꺼내서 어색한 분위기를 푼다."
]

D_responses = [
    "용기를 내서 바로 옆자리에 앉는다.",
    "궁금하니까 할 말이 뭔지 디엠으로 당장 알려달라고 한다.",
    "기회를 보다 그녀의 손을 잡는다."
]

J_responses = [
    "“다음에는 뭐 할까? 너 가보고 싶다고 했던 곳 같이 갈래?” 바로 다음 약속을 잡는다.",
    "그날 저녁에 디엠으로 옆에 있던 남자와 어떤 사이인지 물어본다.",
    "“사귀면 정말 잘해줄게” 라고 말해본다.."
]

B_responses = [
    "“오늘 재밌었어. 가능하면 다음에 또 만나자.” 담백하게 문자를 보낸다.",
    "사귀는 사이도 아니니 그냥 넘어간다.",
    "가만히 그녀의 대답을 기다려본다."
]

# 반응
H_reactions = [
    '“좋아! 309관 학식 맛있지~”',
    '우리는 한참동안 전화를 하다가 잠에 들었다.',
    '“그래! 날도 더우니까 카페 가자~”'
]

O_reactions = [
    "“그럼 기꾸스시 가자! 거기 초밥 맛있어~”",    
    "그녀에게 연락을 하고, 집 앞에서 같이 산책을 했다.\n잠깐이라도 얼굴을 보니 너무 좋았다...",
    "“그래! 재밌겠다ㅎㅎ”"
]

K_reactions = [
    "“앗 감사합니다! 저기, 혹시...”",
    "“다행이다..”",
    "‘꽃 좋아하려나..? 마음에 들었으면 좋겠다.’"
]

M_reactions = [
    "“아, 감사합니다.”\n나는 고개를 끄덕인 후, 그녀를 지나쳐 가려는데.. “저기, 혹시...”",
    "“응...”",
    "‘흠...이건 좀 부담스러운가? 그럼 이거?’\n한참을 고민하다가 결국 처음 골랐던 옷을 샀다."
]

A_reactions = [
    "...눈이 마주친 것 같은데, 기분 탓이겠지?",
    "‘그녀가 하려던 말이 뭐였을까...’생각에 잠겼다.",
    "그녀는 내가 꺼낸 이야기에 웃어주었다!\n우리는 즐겁게 이야기를 나누며 걸었다."
]

D_reactions = [
    "수업에 집중하는 그녀의 옆모습이 너무 예뻤다...",
    "‘대체 무슨 말을 하려고 하는걸까?’ 불안하지만...꼭 들어야겠다.",
    "그녀는 조금 놀란듯 했지만, 내 손을 꼭 잡아주었다."
]

J_reactions = [
    "“그래! 같이 가자ㅎㅎ 오늘 재밌었어!”",
    "...아직 사귀는 사이도 아닌데 부담스러우려나...\n결국 그녀에게 연락하지 못했다.",
    "나는 그녀를 바라보았다."
]

B_reactions = [
    "“나도 오늘 너무 재밌었어ㅎㅎ 다음에 봐!”",
    "그래...아직 사귀는 사이도 아니니까 부담스럽겠지.",
    "나는 그녀를 바라보았다."
]

# --- 각 질문 모듈 ---
def ask_HO(set_idx):
    typewriter(f"\n\n{HO_questions[set_idx]}\n\n")
    time.sleep(1.7)
    print(f"1: {H_responses[set_idx]}")
    print(f"2: {O_responses[set_idx]}")
    if get_choice() == 1:
        user_mbti['H'] += 1
        typewriter(f"\n{H_reactions[set_idx]}\n")
    else: 
        user_mbti['O'] += 1
        typewriter(f"\n{O_reactions[set_idx]}\n")
    print_transition()

def ask_KM(set_idx):
    typewriter(f"\n\n{KM_questions[set_idx]}\n\n")
    time.sleep(1.7)
    print(f"1: {K_responses[set_idx]}")
    print(f"2: {M_responses[set_idx]}")
    if get_choice() == 1: 
        user_mbti['K'] += 1
        typewriter(f"\n{K_reactions[set_idx]}\n")
    else: 
        user_mbti['M'] += 1
        typewriter(f"\n{M_reactions[set_idx]}\n")
    print_transition()

def ask_AD(set_idx):
    typewriter(f"\n\n{AD_questions[set_idx]}\n\n")
    time.sleep(1.7)
    print(f"1: {A_responses[set_idx]}")
    print(f"2: {D_responses[set_idx]}")
    if get_choice() == 1: 
        user_mbti['A'] += 1
        typewriter(f"\n{A_reactions[set_idx]}\n")
    else:
        user_mbti['D'] += 1
        typewriter(f"\n{D_reactions[set_idx]}\n")
    print_transition()

def ask_JB(set_idx):
    typewriter(f"\n\n{JB_questions[set_idx]}\n\n")
    time.sleep(1.7)
    print(f"1: {J_responses[set_idx]}")
    print(f"2: {B_responses[set_idx]}")
    if get_choice() == 1: 
        user_mbti['J'] += 1
        typewriter(f"\n{J_reactions[set_idx]}\n")
    else: 
        user_mbti['B'] += 1
        typewriter(f"\n{B_reactions[set_idx]}\n")
    print_transition()

def final_dialogue():
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    typewriter("\n그녀는 미소를 지으며 고개를 끄덕였다.\n그날 밤, 그녀와의 첫 데이트, 그리고 그녀에게 고백한 그 순간,\n\n그 모든 것이 우리에게는 소중한 추억이 되었다.")
    time.sleep(1)
    print("\n.")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...\n")
    time.sleep(2)

# 마무리 및 성격유형 계산
def determine_mbti():
    mbti_result = ""
    mbti_result += 'H' if user_mbti['H'] > user_mbti['O'] else 'O'
    mbti_result += 'K' if user_mbti['K'] > user_mbti['M'] else 'M'
    mbti_result += 'A' if user_mbti['A'] > user_mbti['D'] else 'D'
    mbti_result += 'J' if user_mbti['J'] > user_mbti['B'] else 'B'
    
    return mbti_result


if __name__ == "__main__":
    if not validate_openrouter_api_key():
        try:
            input(
                "openrouter api 키가 유효하지 않습니다. "
                "환경변수를 다시 확인해주시기 바랍니다. (엔터를 눌러 종료)"
            )
        except EOFError:
            pass
        raise SystemExit

    # 첫 번째 사이클 (인덱스: 0)
    # 순서: A/D -> K/M -> H/O -> J/B
    play_intro(0)
    ask_AD(0)
    ask_KM(0)
    ask_HO(0)
    ask_JB(0)

    # 두 번째 사이클 (인덱스: 1)
    # 순서: J/B -> A/D -> K/M -> H/O
    ask_JB(1)
    ask_AD(1)
    ask_KM(1)
    ask_HO(1)

    # 세 번째 사이클 (인덱스: 2)
    # 순서: H/O -> K/M -> A/D -> J/B
    ask_HO(2)
    ask_KM(2)
    ask_AD(2)
    ask_JB(2)

    final_dialogue()
    mbti_result = determine_mbti()

    print("\033[H\033[J", end="")
    time.sleep(1.2)
    print(f"당신의 연애 스타일 코드는 {mbti_result}입니다.")
    
    time.sleep(1.2)
    print("\n집돌이(H) vs 야외형(O)\n\n다정형(K) vs 무심형(M)\n\n회피형(A) vs 돌진형(D)\n\n집착형(J) vs 방치형(B)\n\n")
    time.sleep(1.5)
    print(".")
    time.sleep(1.7)
    print(".")
    time.sleep(1.8)
    print(".")
    time.sleep(1)

    explainer = get_result_module()
    explain_result = explainer.get_result(mbti_result)
    print(explain_result)
