import os

import requests

MODEL = "openrouter/free"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_API_KEY_PREFIX = "sk-or-v1-"

TYPE_AXES = {
    0: {
        "H": ("집돌이", "집이나 익숙한 공간에서 안정감을 느끼는 편"),
        "O": ("야외형", "밖에서 새로운 경험을 하며 에너지를 얻는 편"),
    },
    1: {
        "K": ("다정형", "말과 행동으로 애정을 자주 표현하는 편"),
        "M": ("무심형", "담백하고 부담 없는 방식으로 마음을 보여주는 편"),
    },
    2: {
        "A": ("회피형", "갈등이나 부담스러운 감정에서 잠시 거리를 두는 편"),
        "D": ("돌진형", "마음이 생기면 솔직하고 빠르게 다가가는 편"),
    },
    3: {
        "J": ("집착형", "관계의 확신과 잦은 연결을 중요하게 느끼는 편"),
        "B": ("방치형", "서로의 자유와 개인 시간을 중요하게 느끼는 편"),
    },
}
TYPES = [
    "HKAJ",  # 집돌이 · 다정형 · 회피형 · 집착형
    "HKAB",  # 집돌이 · 다정형 · 회피형 · 방치형
    "HKDJ",  # 집돌이 · 다정형 · 돌진형 · 집착형
    "HKDB",  # 집돌이 · 다정형 · 돌진형 · 방치형

    "HMAJ",  # 집돌이 · 무심형 · 회피형 · 집착형
    "HMAB",  # 집돌이 · 무심형 · 회피형 · 방치형
    "HMDJ",  # 집돌이 · 무심형 · 돌진형 · 집착형
    "HMDB",  # 집돌이 · 무심형 · 돌진형 · 방치형

    "OKAJ",  # 야외형 · 다정형 · 회피형 · 집착형
    "OKAB",  # 야외형 · 다정형 · 회피형 · 방치형
    "OKDJ",  # 야외형 · 다정형 · 돌진형 · 집착형
    "OKDB",  # 야외형 · 다정형 · 돌진형 · 방치형

    "OMAJ",  # 야외형 · 무심형 · 회피형 · 집착형
    "OMAB",  # 야외형 · 무심형 · 회피형 · 방치형
    "OMDJ",  # 야외형 · 무심형 · 돌진형 · 집착형
    "OMDB",  # 야외형 · 무심형 · 돌진형 · 방치형
]


def validate_code(code):
    code = code.strip().upper()

    if len(code) != 4:
        raise ValueError("결과는 예시처럼 HKDJ 형태의 4글자여야 합니다.")

    for index, letter in enumerate(code):
        if letter not in TYPE_AXES[index]:
            allowed = ", ".join(TYPE_AXES[index].keys())
            raise ValueError(f"{index + 1}번째 글자는 {allowed} 중 하나여야 합니다.")

    return code


def describe_code(code):
    lines = []
    for index, letter in enumerate(code):
        name, description = TYPE_AXES[index][letter]
        lines.append(f"- {letter}: {name} ({description})")
    return "\n".join(lines)


def build_prompt(code):
    return f"""
너는 연애 성향을 담백하고 직관적으로 설명하는 한국어 상담형 도우미야.

사용자의 연애 스타일 코드는 {code}야.
코드는 각 axis마다 2가지 글자 중 하나로 구성되어 있어.
각 글자의 의미는 다음과 같아.
{describe_code(code)}
따라서 연애 스타일 코드는 다음 16가지 중 하나로 나타내어져.
{TYPES}

다음 형식으로 답해줘.
1. 한 줄 요약
2. 전체 연애 스타일 설명
3. 연애할 때 장점 3가지
4. 조심하면 좋은 점 3가지
5. 잘 맞는 상대의 (연애 스타일 코드)와 이유

반드시 지켜야 할 조건:
- 영어를 쓰지 말고 한국어로만 답해.
- 이모티콘과 이모지는 절대 쓰지 마.
- 오글거리거나 과장된 표현은 피하고 담백하게 써.
- 비유는 과하게 쓰지 말고, 필요한 내용은 직관적으로 설명해.
- 사람을 단정하거나 상처 주는 표현은 피하고, 성향의 장단점을 균형 있게 설명해.
- 잘 맞는 상대의 연애 스타일 코드를 제시할 때에는 {TYPES}중 하나를 제시해. 그러나 자신의 연애 스타일 코드와 모든 글자가 같아서는 안 돼.
""".strip()


def request_love_style(code, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-Title": "Love Style Explainer",
    }
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "너는 한국어로 연애 성향을 설명하는 친절한 도우미야.",
            },
            {"role": "user", "content": build_prompt(code)},
        ],
        "temperature": 0.8,
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    if response.status_code == 429:
        retry_after = response.headers.get("Retry-After")
        try:
            retry_after = int(retry_after) if retry_after else None
        except ValueError:
            retry_after = None

        raise RateLimitError(
            "API rate limit reached. Please try again later.",
            retry_after=retry_after,
        )

    if response.status_code in (401, 403):
        raise InvalidAPIKeyError("API키가 유효하지 않습니다.")

    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"].strip()


class RateLimitError(RuntimeError):
    def __init__(self, message, retry_after=None):
        super().__init__(message)
        self.retry_after = retry_after


class InvalidAPIKeyError(ValueError):
    pass


def validate_openrouter_api_key(api_key=OPENROUTER_API_KEY):
    token = api_key.removeprefix(OPENROUTER_API_KEY_PREFIX)
    return (
        api_key.startswith(OPENROUTER_API_KEY_PREFIX)
        and bool(token)
        and not any(char.isspace() for char in api_key)
    )


class LoveStyleExplainer:
    def __init__(self, api_key=OPENROUTER_API_KEY):
        self.api_key = api_key

    def explain(self, code):
        if (
            not self.api_key
            or self.api_key.startswith("여기에_")
            or self.api_key.startswith("?")
        ):
            raise InvalidAPIKeyError("API키가 유효하지 않습니다.")

        try:
            code = validate_code(code)
        except ValueError as error:
            raise ValueError(f"입력 오류: {error}") from error

        if not self.api_key or self.api_key == "여기에_OPENROUTER_API_KEY_입력":
            raise ValueError("OPENROUTER_API_KEY에 OpenRouter API 키를 입력한 뒤 다시 실행하세요.")

        try:
            return request_love_style(code, self.api_key)
        except requests.exceptions.HTTPError as error:
            if error.response is not None and error.response.status_code == 429:
                raise RuntimeError(
                    "API 요청 실패: 무료 모델 사용량이 많거나 요청 제한에 걸렸습니다. "
                    "잠시 뒤 다시 실행해 보세요. 현재 모델은 덜 몰리는 무료 라우터(openrouter/free)입니다."
                ) from error
            raise RuntimeError(f"API 요청 실패: {error}") from error
        except requests.exceptions.RequestException as error:
            raise RuntimeError(f"API 요청 실패: {error}") from error
        except (KeyError, IndexError, TypeError) as error:
            raise RuntimeError(f"API 응답을 해석하지 못했습니다: {error}") from error
