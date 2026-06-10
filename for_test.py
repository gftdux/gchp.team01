from get_result_module import get_result_module


explainer = get_result_module()
explain_result = explainer.get_result("HKDJ")
print(explain_result)