import os
import time
import random

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

    execution_time = (time.time() - start_time) * 1000

    return max_reward, best_buffer, best_coordinates, execution_time


def generate_matrix_and_sequence(num_unique_tokens, tokens, buffer_size, matrix_width, matrix_height, num_sequences, max_sequence_length):
    matrix = [[random.choice(tokens) for i in range(matrix_width)] for j in range(matrix_height)]
    sequences_reward = [(random.choices(tokens, k=random.randint(1, max_sequence_length)), random.randint(1, 30)) for z in range(num_sequences)]
    return matrix, sequences_reward



def save_solution(buffer_size, num_sequences, max_reward, best_buffer, best_coordinates, execution_time, matrix, sequences):
    folder_path = "../test"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = input("Input file name to save the solution: ")
    file_path = os.path.join(folder_path, f"{filename}.txt")
    
    with open(file_path, 'w') as file:
        file.write(f"Buffer size: {buffer_size}\n")
        file.write("Matrix:\n")
        for row in matrix:
            file.write(' '.join(row) + '\n')
        file.write(f"Number of Sequences: {num_sequences}\n")
        file.write("Sequences and Rewards:\n")
        for sequence, reward in sequences:
            file.write(f"Sequence: {' '.join(sequence)}, Reward: {reward}\n")
        file.write("\n")
        if max_reward == 0:
            file.write("Maximum reward weight: 0\n")
            file.write("Tidak ada jalur yang optimal atau tidak ada urutan yang bisa dibentuk.\n")
        else:
            file.write(f"Maximum reward weight: {max_reward}\n")
            file.write(f"Contents of the buffer: {' '.join(best_buffer)}\n")
            file.write("Coordinates of each token in order:\n")
            for coordinate in best_coordinates:
                file.write(f"{coordinate}\n")
        file.write(f"Program execution time in ms: {execution_time} ms\n")

    print(f"The solution has been saved into {filename}.txt")