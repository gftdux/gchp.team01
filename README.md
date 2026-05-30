# gchp.team01

[미연시로 연애스타일 (알파벳 4자리수)-CC 컨셉]

질문 12개
: 하나에 한 요소x4 세 cycle 돌리기 (집돌이 2, 야외형 1 답변시 집돌이 판단)

마지막에 “당신의 연애스타일은 __ 입니다.

Finding Your Love Style(Relationship?)

<연애 스타일> HO/KM/AD/JB
집돌이(H) vs 야외형(O)
다정형(K) vs 무심형(M)
회피형(A) vs 돌진형(D)
집착형(J) vs 방치형(B)

LLM한테 나온 유형의 특징 설명 시키기 - 유형의 이름, 특징, 장점, 조심할점, 잘맞는 상대와 이유

성별 정해 말아
일단 미소녀로 만들어 놓고 미소년은 나중에 추가


### explain_module.py 사용 예시
```
explainer = LoveStyleExplainer()
result = explainer.explain("HKDJ")
print(result)
```
유효성 검사를 다른 모듈로 빼긴 할 건데 호출을 설명 모듈 안에서 할지 아니면 메인 프로그램 루프에 포함시킬지는 미정.