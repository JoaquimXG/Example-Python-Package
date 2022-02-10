# from .required_by_both import required_by_both
from sample_package.two import two
from sample_package.module_and_function_name_match import test, module_and_function_name_match

def one():
    print("This is one")
    module_and_function_name_match("one")
    test("one")
    two()