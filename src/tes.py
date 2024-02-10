import time

def generate_all_paths(matrix, buffer_size):
    if buffer_size == 1:
        return [[(i, j)] for i in range(len(matrix)) for j in range(len(matrix[0]))]
    else:
        smaller_paths = generate_all_paths(matrix, buffer_size - 1)
        paths = []
        for path in smaller_paths:
            i, j = path[-1]
            if len(path) % 2 == 1:
                # We move horizontally
                for new_j in range(len(matrix[0])):
                    if new_j != j:
                        paths.append(path + [(i, new_j)])
            else:
                # We move vertically
                for new_i in range(len(matrix)):
                    if new_i != i:
                        paths.append(path + [(new_i, j)])
        return paths

def breach_protocol(matrix, sequences, buffer_size):
    start_time = time.time()
    max_reward = 0
    best_buffer = []
    best_coordinates = []

    # Generate all possible paths
    paths = generate_all_paths(matrix, buffer_size)

    for path in paths:
        buffer = [matrix[i][j] for i, j in path]
        total_reward = sum(reward for seq, reward in sequences if ''.join(seq) in ''.join(buffer))
        if total_reward > max_reward:
            max_reward = total_reward
            best_buffer = buffer
            best_coordinates = [(i+1, j+1) for i, j in path]

    execution_time = (time.time() - start_time) * 1000 # in ms

    return max_reward, best_buffer, best_coordinates, execution_time

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

# Start from the coordinate (1,1) with value "7A"
paths = generate_all_paths(matrix, buffer_size)
paths = [path for path in paths if path[0] == (0, 0)]

max_reward, best_buffer, best_coordinates, execution_time = breach_protocol(matrix, sequences, buffer_size)

print("Bobot hadiah maksimal:", max_reward)
print("Isi dari buffer:", ' '.join(best_buffer))
print("Koordinat dari setiap token secara terurut:", best_coordinates)
print("Waktu eksekusi program dalam ms:", execution_time)
