import time

def generate_all_paths(matrix, buffer_size, start=(0,0), is_horizontal=True):
    i, j = start
    if buffer_size == 1:
        if is_horizontal:
            return [[(i, new_j)] for new_j in range(len(matrix[0])) if new_j != j]
        else:
            return [[(new_i, j)] for new_i in range(len(matrix)) if new_i != i]
    else:
        paths = []
        if is_horizontal:
            for new_j in range(len(matrix[0])):
                if new_j != j:
                    smaller_paths = generate_all_paths(matrix, buffer_size - 1, start=(i, new_j), is_horizontal=False)
                    for path in smaller_paths:
                        paths.append([(i, new_j)] + path)
        else:
            for new_i in range(len(matrix)):
                if new_i != i:
                    smaller_paths = generate_all_paths(matrix, buffer_size - 1, start=(new_i, j), is_horizontal=True)
                    for path in smaller_paths:
                        paths.append([(new_i, j)] + path)
        return paths


def breach_protocol(matrix, sequences, buffer_size):
    start_time = time.time()
    max_reward = 0
    best_buffer = []
    best_coordinates = []

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

paths = generate_all_paths(matrix, buffer_size)
paths = [path for path in paths if path[0] == (0, 0)]

max_reward, best_buffer, best_coordinates, execution_time = breach_protocol(matrix, sequences, buffer_size)

print("Bobot hadiah maksimal:", max_reward)
print("Isi dari buffer:", ' '.join(best_buffer))
print("Koordinat dari setiap token secara terurut:", best_coordinates)
print("Waktu eksekusi program dalam ms:", execution_time)