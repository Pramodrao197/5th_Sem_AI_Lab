
# Forward Chaining in First Order Logic
# Problem: Prove that Robert is a Criminal

# Initial Facts
facts = {
    ("American", "Robert"),
    ("Enemy", "CountryA", "America"),
    ("Missile", "M1"),
    ("Owns", "CountryA", "M1")
}

# Rules
rules = [
    # All missiles are weapons
    ([("Missile", "?x")],
     ("Weapon", "?x")),

    # Robert sold all missiles to Country A
    ([("Missile", "?x"),
      ("Owns", "CountryA", "?x")],
     ("Sells", "Robert", "?x", "CountryA")),

    # An American selling weapons to an enemy
    # country is a criminal
    ([("American", "?x"),
      ("Weapon", "?y"),
      ("Sells", "?x", "?y", "?z"),
      ("Enemy", "?z", "America")],
     ("Criminal", "?x"))
]


# Match facts with rules
def match(pattern, fact, substitution):

    if pattern[0] != fact[0]:
        return None

    for p, f in zip(pattern[1:], fact[1:]):

        if p.startswith("?"):
            if p in substitution:
                if substitution[p] != f:
                    return None
            else:
                substitution[p] = f

        elif p != f:
            return None

    return substitution


# Find possible substitutions
def find_substitutions(premises, facts, substitution=None):

    if substitution is None:
        substitution = {}

    if not premises:
        return [substitution]

    results = []

    first = premises[0]
    remaining = premises[1:]

    for fact in facts:
        new_sub = match(first, fact, substitution.copy())

        if new_sub is not None:
            results.extend(
                find_substitutions(remaining, facts, new_sub)
            )

    return results


# Forward Chaining Algorithm
def forward_chaining(facts, rules, goal):

    while True:
        new_fact_added = False

        for premises, conclusion in rules:

            substitutions = find_substitutions(
                premises, facts
            )

            for sub in substitutions:

                new_fact = tuple(
                    sub.get(item, item)
                    for item in conclusion
                )

                if new_fact not in facts:
                    facts.add(new_fact)

                    print("Derived:", new_fact)

                    new_fact_added = True

                    if new_fact == goal:
                        return True

        if not new_fact_added:
            break

    return goal in facts


# Goal to prove
goal = ("Criminal", "Robert")

# Execute the program
print("Initial Facts:")
for fact in sorted(facts):
    print(fact)

print("\nForward Chaining:")

if forward_chaining(facts, rules, goal):
    print("\nGoal Proved: Robert is a Criminal")
else:
    print("\nGoal Not Proved")
