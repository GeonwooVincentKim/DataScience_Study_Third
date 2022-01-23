from vector_example import subtract, List, Vector, vector_mean


def de_mean(data: List[Vector]) -> List[Vector]:
    """
        Re-alignment every dimension average become 0
    """
    mean = vector_mean(data)
    return [
        subtract(vector, mean)
        for vector in data
    ]

