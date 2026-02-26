; Ensure nested function output never < 0
(declare-const x Nat)
(declare-fun f(Nat) Nat)
(assert (< (f (f x)) 0))