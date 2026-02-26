from pysmt.shortcuts import is_sat, is_unsat
from pysmt.smtlib.parser import get_formula
from io import StringIO

def test_sat():
    smtlib_content = """
    (declare-const x Nat)
    (assert (> x 0))
    """
    formula = get_formula(StringIO(smtlib_content))
    assert is_sat(formula, solver_name="cvc5")