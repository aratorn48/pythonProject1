data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data):
    def jarvis(structure):
        sum = 0
        if isinstance(structure, (list, set, tuple)):
            for i in structure:
                sum += jarvis(i)
        elif isinstance(structure, (dict)):
            for key, value in structure.items():
                sum += jarvis(key)
                sum += jarvis(value)
        elif isinstance(structure, (int, float)):
            sum += structure
        elif isinstance(structure, str):
            sum += len(structure)
        return sum
    return jarvis(data)

result = calculate_structure_sum(data_structure)
print(result)