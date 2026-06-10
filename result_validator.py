import re


VALID_TYPES = {
    "HKAJ",
    "HKAB",
    "HKDJ",
    "HKDB",
    "HMAJ",
    "HMAB",
    "HMDJ",
    "HMDB",
    "OKAJ",
    "OKAB",
    "OKDJ",
    "OKDB",
    "OMAJ",
    "OMAB",
    "OMDJ",
    "OMDB",
}

REQUIRED_SECTIONS = ("1.", "2.", "3.", "4.", "5.")
STYLE_CODE_PATTERN = re.compile(r"\b[HO][KM][AD][JB]\b")
BAD_RESPONSE_KEYWORDS = (
    "api error",
    "error",
    "cannot",
    "can't",
    "sorry",
    "오류",
    "죄송",
    "제공할 수",
)


def find_style_codes(text):
    return STYLE_CODE_PATTERN.findall(text.upper())


def get_validation_errors(result, love_style):
    errors = []

    if not isinstance(result, str) or not result.strip():
        return ["empty result"]

    normalized_result = result.strip()
    normalized_code = love_style.strip().upper()

    if len(normalized_result) < 80:
        errors.append("result is too short")

    missing_sections = [
        section for section in REQUIRED_SECTIONS if section not in normalized_result
    ]
    if missing_sections:
        errors.append(f"missing sections: {', '.join(missing_sections)}")

    lowered_result = normalized_result.lower()
    if any(keyword in lowered_result for keyword in BAD_RESPONSE_KEYWORDS):
        errors.append("result looks like an error or refusal message")

    style_codes = find_style_codes(normalized_result)
    valid_codes = [code for code in style_codes if code in VALID_TYPES]
    recommended_codes = [code for code in valid_codes if code != normalized_code]

    if not valid_codes:
        errors.append("no valid love style code found")
    elif not recommended_codes:
        errors.append("no recommended code different from user code found")

    return errors


def validate_result(result, love_style):
    return len(get_validation_errors(result, love_style)) == 0
