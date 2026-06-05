import time


RETRY_DELAY_SECONDS = 5
MAX_RETRY_COUNT = 5


class get_result_module:

    def get_result(self, love_style):
        from explain_module import LoveStyleExplainer, RateLimitError

        explainer = LoveStyleExplainer()
        for retry_count in range(MAX_RETRY_COUNT + 1):
            try:
                print(f"{love_style} result is being generated...", flush=True)
                return explainer.explain(love_style)
            except RateLimitError as error:
                if retry_count == MAX_RETRY_COUNT:
                    raise RuntimeError(
                        "API rate limit kept failing. Please try again later."
                    ) from error

                delay_seconds = error.retry_after or (
                    RETRY_DELAY_SECONDS * (2 ** retry_count)
                )
                print(
                    f"API rate limit reached. Retrying in {delay_seconds} seconds... "
                    f"({retry_count + 1}/{MAX_RETRY_COUNT})",
                    flush=True,
                )
                time.sleep(delay_seconds)
