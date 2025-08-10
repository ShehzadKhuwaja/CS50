import sys
import random

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for v in self.domains:
            new_set = self.domains[v].copy()
            for value in self.domains[v]:
                if len(value) != v.length:
                    new_set.remove(value)
            self.domains[v] = new_set
    
        # raise NotImplementedError

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revise = False
        updated_words = self.domains[x].copy()
        if self.crossword.overlaps[x, y] is not None:
            i, j = self.crossword.overlaps[x, y]
            for word_x in self.domains[x]:
                match_found = False
                for word_y in self.domains[y]:
                    if word_x[i] == word_y[j]:
                        match_found = True
                        break
                if not match_found:
                    updated_words.remove(word_x)
                    revise = True
        self.domains[x] = updated_words
        return revise
        # raise NotImplementedError

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs is None:
            arcs = []
            for overlap in self.crossword.overlaps:
                if self.crossword.overlaps[overlap] is not None:
                    arcs.append(overlap)

        while len(arcs) != 0:
            constrainst = arcs.pop(0)
            if self.revise(*constrainst):
                if len(self.domains[constrainst[0]]) == 0:
                    return False
                for z in self.crossword.neighbors(constrainst[0]) - {constrainst[1]}:
                    arcs.append((z, constrainst[0]))
        return True


        raise NotImplementedError

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        if len(assignment) == len(self.crossword.variables):
            return True
        return False
        raise NotImplementedError

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        for variable in assignment:
            if len(assignment[variable]) != variable.length:
                return False
            
        for var_one in assignment:
            for var_two in assignment:
                if assignment[var_one] == assignment[var_two] and var_one != var_two:
                    return False
                
        for overlap in self.crossword.overlaps:
            if self.crossword.overlaps[overlap] is not None:
                i, j = self.crossword.overlaps[overlap]
                if overlap[0] in assignment and overlap[1] in assignment and assignment[overlap[0]][i] != assignment[overlap[1]][j]:
                    return False
        
        return True
             
        raise NotImplementedError

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # least constraining value (lcv)
        lcv = {}
        for value in self.domains[var]:
            lcv[value] = 0
            count = 0
            for y in self.crossword.neighbors(var):
                if y not in assignment:
                    if self.crossword.overlaps[var, y] is not None:
                        i, j = self.crossword.overlaps[var, y]
                        for word_y in self.domains[y]:
                            if value[i] != word_y[j]:
                                count += 1
                        lcv[value] = count

        return sorted(lcv, key=lambda item: lcv[item])
        raise NotImplementedError

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        unassigned_variables = self.crossword.variables.copy()
        for variable in assignment:
            unassigned_variables.remove(variable)
        
        smallest_domain_variables = []
        smallest_variable = None
        for variable in unassigned_variables:
            if smallest_variable is None or len(self.domains[variable]) < smallest_variable:
                smallest_domain_variables = [variable]
                smallest_variable = len(self.domains[variable])
            elif len(self.domains[variable]) == smallest_variable:
                smallest_domain_variables.append(variable)
        
        highest_degree_variables = []
        highest_degree_variable = None
        for variable in smallest_domain_variables:
            if highest_degree_variable is None or len(self.crossword.neighbors(variable)) > highest_degree_variable:
                highest_degree_variables = [variable]
                highest_degree_variable = len(self.crossword.neighbors(variable))
            elif len(self.crossword.neighbors(variable)) == highest_degree_variable:
                highest_degree_variables.append(variable)

        return random.choice(highest_degree_variables)
    
        raise NotImplementedError

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            assignment[var] = value
            if self.consistent(assignment):
                inferences = self.inference(var, assignment)
                if inferences != False:
                    for new_assignment in inferences:
                        assignment[new_assignment[0]] = new_assignment[1]
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                del assignment[var]
                for sentence in inferences:
                    del assignment[sentence[0]]
        return None
        raise NotImplementedError

    def inference(self, var, assignment):
        possible_arcs = []
        original_copy = {var: self.domains[var].copy()}
        for variable in self.crossword.neighbors(var):
            if variable not in assignment:
                original_copy[variable] = self.domains[variable].copy()
                possible_arcs.append((variable, var))
        self.domains[var] = {assignment[var]} 
        if not self.ac3(possible_arcs):
            for variable in original_copy:
                self.domains[variable] = original_copy[variable]
            return False
        new_knowledge = []
        for variable in self.crossword.neighbors(var):
            if len(self.domains[variable]) == 1:
                new_knowledge.append((variable, *self.domains[variable]))
        for variable in original_copy:
            self.domains[variable] = original_copy[variable]
        return new_knowledge
        

def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
