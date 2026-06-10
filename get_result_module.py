import time

from result_validator import get_validation_errors


INTERNET_RETRY_DELAY_SECONDS = 10
MAX_RESULT_VALIDATION_ATTEMPTS = 3


class get_result_module:

    def ask_retry(self):
        while True:
            choice = input("다시 시도하시겠습니까?(y/n): ").strip().lower()
            if choice == "y":
                return True
            if choice == "n":
                return False
            print("y 또는 n을 입력해 주세요.")

    def is_internet_error(self, error):
        cause = error.__cause__
        if cause is None:
            return False

        error_module = cause.__class__.__module__
        return error_module.startswith("requests.")

    def get_error_message(self, error):
        if self.is_internet_error(error):
            return "인터넷 에러가 났습니다."
        return f"{type(error).__name__}: {error}"

    def get_result(self, love_style):
        while True:
            try:
                from explain_module import LoveStyleExplainer

                explainer = LoveStyleExplainer()
                for attempt in range(1, MAX_RESULT_VALIDATION_ATTEMPTS + 1):
                    print(
                        f"{love_style} 결과를 생성중입니다. 시간이 걸릴 수 있습니다...\n\n\n",
                        flush=True,
                    )
                    result = explainer.explain(love_style)
                    validation_errors = get_validation_errors(result, love_style)

                    if not validation_errors:
                        return result

                    print(
                        "생성된 결과가 검증을 통과하지 못해 자동으로 다시 생성합니다. "
                        f"({attempt}/{MAX_RESULT_VALIDATION_ATTEMPTS})",
                        flush=True,
                    )
                    print(f"검증 실패 사유: {', '.join(validation_errors)}", flush=True)

                raise RuntimeError(
                    f"AI 결과가 {MAX_RESULT_VALIDATION_ATTEMPTS}회 연속 검증에 실패했습니다."
                )
            except Exception as error:
                print(f"에러가 났습니다. {self.get_error_message(error)}", flush=True)

                if self.is_internet_error(error):
                    print(
                        f"{INTERNET_RETRY_DELAY_SECONDS}초 후에 다시 시도해 주세요.",
                        flush=True,
                    )
                    time.sleep(INTERNET_RETRY_DELAY_SECONDS)

                if not self.ask_retry():
                    raise SystemExit
