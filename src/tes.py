def breach_protocol(matrix, sequences, buffer_size):
    rewards = {tuple(seq): weight for seq, weight in sequences}
    best_path, best_reward = [], 0

    # generate all possible paths
    paths = generate_paths(matrix, buffer_size)

    for path in paths:
        buffer = [matrix[x][y] for x, y in path]
        total_reward = 0
        seq_coords = []  # track the coordinates of the sequences found
        used_coords = set()  # track the coordinates that have been used

        # check if any sequence in the buffer
        for seq, weight in rewards.items():
            for i in range(len(buffer) - len(seq) + 1):
                if tuple(buffer[i:i+len(seq)]) == seq and all(coord not in used_coords for coord in path[i:i+len(seq)]):
                    total_reward += weight
                    seq_coords.extend(path[i:i+len(seq)])
                    used_coords.update(path[i:i+len(seq)])

        if total_reward > best_reward:
            best_path, best_reward = seq_coords, total_reward

    return best_path, best_reward

def generate_paths(matrix, buffer_size):
    paths = []
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            # generate all possible paths starting from (x, y)
            paths.extend(generate_paths_from(matrix, buffer_size, x, y, set([(x, y)])))
    return paths

def generate_paths_from(matrix, buffer_size, x, y, visited):
    if buffer_size == 1:
        return [[(x, y)]]

    paths = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and (nx, ny) not in visited:
            for path in generate_paths_from(matrix, buffer_size - 1, nx, ny, visited | {(nx, ny)}):
                paths.append([(x, y)] + path)
    return paths

# example usage
matrix = [
    ["7A", "55", "E9", "E9", "1C", "55"],
    ["55", "7A", "1C", "7A", "E9", "55"],
    ["55", "1C", "1C", "55", "E9", "BD"],
    ["BD", "1C", "7A", "1C", "55", "BD"],
    ["BD", "55", "BD", "7A", "1C", "1C"],
    ["1C", "55", "55", "7A", "55", "7A"]
]
sequences = [
    (['BD', 'E9', '1C'], 15),
    (['BD', '7A', 'BD'], 20),
    (['BD', '1C', 'BD', '55'], 30)
]
buffer_size = 7

path, total_reward = breach_protocol(matrix, sequences, buffer_size)
print(f"Path: {path}")
print(f"Total reward: {total_reward}")

print("Elements in the path:")
for x, y in path:
    print(matrix[x][y])