import time

from requests.exceptions import RequestException


RETRY_DELAY_SECONDS = 5
INTERNET_RETRY_DELAY_SECONDS = 10
MAX_RETRY_COUNT = 5


class get_result_module:

    def get_result(self, love_style):
        from explain_module import InvalidAPIKeyError, LoveStyleExplainer, RateLimitError

        explainer = LoveStyleExplainer()
        rate_retry_count = 0

        while True:
            try:
                print(f"{love_style} 결과를 생성중입니다. 시간이 걸릴 수 있습니다...\n\n\n", flush=True)
                return explainer.explain(love_style)
            except InvalidAPIKeyError:
                print("API키가 유효하지 않습니다.")
                raise SystemExit
            except RateLimitError as error:
                if rate_retry_count == MAX_RETRY_COUNT:
                    raise RuntimeError(
                        "API rate limit kept failing. Please try again later."
                    ) from error

                delay_seconds = error.retry_after or (
                    RETRY_DELAY_SECONDS * (2 ** rate_retry_count)
                )
                rate_retry_count += 1
                print(
                    f"API rate limit reached. Retrying in {delay_seconds} seconds... "
                    f"({rate_retry_count}/{MAX_RETRY_COUNT})",
                    flush=True,
                )
                time.sleep(delay_seconds)
            except RuntimeError as error:
                if not isinstance(error.__cause__, RequestException):
                    raise

                print(
                    f"인터넷 에러가 났습니다. {INTERNET_RETRY_DELAY_SECONDS}초 후에 다시 시도해 주세요.",
                    flush=True,
                )
                time.sleep(INTERNET_RETRY_DELAY_SECONDS)

                while True:
                    choice = input("다시 시도하시겠습니까?(y/n): ").strip().lower()
                    if choice == "y":
                        break
                    if choice == "n":
                        raise SystemExit
                    print("y 또는 n을 입력해 주세요.")
