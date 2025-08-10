import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    joint_probability = 1
    for family_member in people:
        gene_copy = 0
        trait = False
        if family_member in one_gene:
            gene_copy = 1
        elif family_member in two_genes:
            gene_copy = 2

        if family_member in have_trait:
            trait = True
        if people[family_member]["mother"] is None and people[family_member]["father"] is None:
            joint_probability *= PROBS["gene"][gene_copy] * PROBS["trait"][gene_copy][trait]
        else:
            if people[family_member]["mother"] in two_genes:
                mother_probability = 1 - PROBS["mutation"]
            elif people[family_member]["mother"] in one_gene:
                mother_probability = 0.5
            else:
                mother_probability = PROBS["mutation"]

            if people[family_member]["father"] in two_genes:
                father_probability = 1 - PROBS["mutation"]
            elif people[family_member]["father"] in one_gene:
                father_probability = 0.5
            else:
                father_probability = PROBS["mutation"]

            if gene_copy == 1:
                gene_probability = (mother_probability * (1 - father_probability)) + (father_probability * (1 - mother_probability))
            elif gene_copy == 2:
                gene_probability = mother_probability * father_probability
            else:
                gene_probability = (1 - mother_probability) * (1 - father_probability)

            joint_probability *= gene_probability * PROBS["trait"][gene_copy][trait]

    return joint_probability
                


    # raise NotImplementedError


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    # get genetrait_details
    for person in probabilities:
        gene_copy = 0
        trait = False
        if person in one_gene:
            gene_copy = 1
        elif person in two_genes:
            gene_copy = 2

        if person in have_trait:
            trait = True

        probabilities[person]["gene"][gene_copy] += p
        probabilities[person]["trait"][trait] += p     
       
    # raise NotImplementedError


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    # alpha = a
    # a(p1, p2, p3) = 1 divide both sides of equation by p1 + p2 + p3
    # a = 1 / p1 + p2 + p3
    for person in probabilities:
        gene_prob_sum = probabilities[person]["gene"][0] + probabilities[person]["gene"][1] + probabilities[person]["gene"][2]
        trait_prob_sum = probabilities[person]["trait"][True] + probabilities[person]["trait"][False]
        alpha_gene = 1 / gene_prob_sum
        alpha_trait = 1 / trait_prob_sum

        for i in range(3): probabilities[person]["gene"][i] *= alpha_gene

        probabilities[person]["trait"][True] *= alpha_trait
        probabilities[person]["trait"][False] *= alpha_trait  

    # raise NotImplementedError


if __name__ == "__main__":
    main()
