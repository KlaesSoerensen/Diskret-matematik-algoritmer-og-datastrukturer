from sympy.logic.boolalg import Or, And, Not, Implies, Xor
from sympy.abc import p, q

# Function to check equivalence
def check_equivalence(prop1, prop2):
    return prop1.equals(prop2)

# Define the original proposition p => ¬q
original_prop = Implies(p, Not(q))

# Define the given propositions
propositions = {
    "Svar 2.a": Or(p, Not(q)),
    "Svar 2.b": Or(Not(p), Not(q)),
    "Svar 2.c": And(p, Not(q)),
    "Svar 2.d": Not(And(p, q)),
    "Svar 2.e": Or(Not(p), And(p, Not(q))),
    "Svar 2.f": Or(And(p, Not(q)), And(Not(p), q)),
    "Svar 2.g": And(Or(p, q), Or(Not(p), q)),
    "Svar 2.h": Implies(Not(q), p),
    "Svar 2.i": Or(q, Implies(p, q)),
    "Svar 2.j": Or(Implies(p, Not(q)), And(p, Not(p))),
    "Svar 2.k": Or(Xor(p, q), Not(q)),
    "Svar 2.l": And(Not(p), Xor(p, q))
}

def prop_to_str(prop):
    if isinstance(prop, Implies):
        return f"{prop.args[0]}⇒{prop.args[1]}"
    prop_str = str(prop)
    prop_str = prop_str.replace('Or', '∨').replace('And', '∧').replace('Not', '¬').replace('Implies', '⇒')
    prop_str = prop_str.replace('|', '∨').replace('&', '∧').replace('~', '¬').replace('^', '⊕')
    return prop_str

def compare_all_to_original():
    results = {}
    for key, proposition in propositions.items():
        results[key] = check_equivalence(original_prop, proposition)
    return results

# Example usage
results = compare_all_to_original()
for prop, is_equivalent in results.items():
    expression = prop_to_str(propositions[prop])
    original_expression = prop_to_str(original_prop).replace('~', '¬')
    print(f"{prop:<10} {expression:<30} {'is equivalent to' if is_equivalent else 'is not equivalent to':<30} {original_expression}")
