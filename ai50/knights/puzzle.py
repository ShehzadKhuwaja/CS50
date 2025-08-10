from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # XOR = (A OR B) AND (NOT (A AND B))
    Or(AKnight, AKnave), # A is either Knight or Knave
    Not(And(AKnight, AKnave)), # but not both
    #Implication(AKnight, And(AKnight, AKnave)),
    Biconditional(AKnight, And(AKnight, AKnave)),
    #Or(Not(AKnight), And(AKnight, AKnave)),
    #Implication(AKnave, Not(And(AKnight, AKnave)))
    ##Implication(AKnave, Or(Not(AKnight), Not(AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    #Implication(AKnight, And(AKnave, BKnave)),
    #Or(Not(AKnight), And(AKnave, BKnave)),
    Or(AKnave, And(AKnave, BKnave)),
    #Implication(AKnave, Not(And(AKnave, BKnave)))
    #Or(Not(AKnave), Not(And(AKnave, BKnave)))
    #Or(Not(AKnave), Or(Not(AKnave), Not(BKnave)))
    #Or(Not(AKnave), Or(AKnight, BKnight))
    Or(AKnight, BKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # we are same kinds means we either (A AND B) are Knights OR (A AND B) are Knave.
    #Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # if A is Knave then the above statement is not True. 
    #Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # we are of different kinds <==> B is knight and A is knave or viceversa.  
    #Implication(BKnight, Or(And(BKnight, AKnave), And(BKnave, AKnight))),
    Biconditional(BKnight, Or(And(BKnight, AKnave), And(BKnave, AKnight))),
    # if B is knave then the above statement is not true.
    #Implication(BKnave, Not(Or(And(BKnight, AKnave), And(BKnave, AKnight)))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    Implication(AKnight, Or(AKnight, AKnave)),
    # DeMorgan's law
    Implication(AKnave, And(Not(AKnight), Not(AKnave))),
    # if B is knight then if A is Knight then Aknave or if A is knave then not a Aknave
    #Implication(And(BKnight, AKnight), AKnave),
    Biconditional(And(BKnight, AKnight), AKnave),
    #Implication(BKnight, CKnave),
    #Implication(BKnave, Not(CKnave)),
    Biconditional(BKnight, CKnave),
    #Implication(CKnight, AKnight),
    #Implication(CKnave, Not(AKnight))
    Biconditional(CKnight, AKnight),

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
