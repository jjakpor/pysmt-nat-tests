from pysmt.shortcuts import is_sat, is_unsat
from pysmt.smtlib.parser import get_formula
from io import StringIO

SOLVER_NAME = "cvc5"

def test_sat():
    # x in Nat, x > 0
    smtlib_content = """
    (declare-const x Nat)
    (assert (> x 0))
    """
    formula = get_formula(StringIO(smtlib_content))
    assert is_sat(formula, solver_name=SOLVER_NAME)

def test_unsat():
    # x in Nat, x < 0
    smtlib_content = """
    (declare-const x Nat)
    (assert (< x 0))
    """
    formula = get_formula(StringIO(smtlib_content))
    assert is_unsat(formula, solver_name=SOLVER_NAME)