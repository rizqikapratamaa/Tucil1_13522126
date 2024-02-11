import functions
import os

def file_mode():
    nama_file = input("Masukkan nama file (tanpa format): ")

    try:
        with open("input_file/" + nama_file + ".txt", 'r') as file:
            lines = file.readlines()

            try:
                buffer_size = int(lines[0])
            except ValueError:
                raise ValueError("Buffer value should be integer.")

            try:
                matrix_width, matrix_height = map(int, lines[1].split())
            except (ValueError, IndexError):
                raise ValueError("The format for filling in the length and width of the matrix does not match.")

            if matrix_height != len(lines[2:2+matrix_height]) or any(len(line.strip().split()) != matrix_width for line in lines[2:2+matrix_height]):
                raise ValueError("The matrix dimensions do not match the expected width and height.")

            matrix = []
            for line in lines[2:2+matrix_height]:
                row = []
                i = 0
                while i < len(line.strip()):
                    if line[i] != ' ':
                        row.append(line[i:i+2])
                        i += 2
                    else:
                        i += 1
                matrix.append(row)

            try:
                num_sequences = int(lines[2+matrix_height])
            except ValueError:
                raise ValueError("Number of sequences should be integer.")

            if num_sequences * 2 != len(lines) - (3 + matrix_height):
                raise ValueError("The number of sequences and rewards does not match the expected number of sequences.")

            sequences_rewards = []

            for i in range(3+matrix_height, len(lines), 2):
                sequence = lines[i].strip().split()
                try:
                    reward = int(lines[i+1])
                except ValueError:
                    raise ValueError("Reward should be.")
                if reward <= 0:
                    raise ValueError("Reward harus merupakan bilangan bulat positif.")
                sequences_rewards.append((sequence, reward))

        print("Buffer size:", buffer_size)
        print("Matrix width:", matrix_width)
        print("Matrix height:", matrix_height)
        print("Matrix:")
        for row in matrix:
            print(' '.join(row))
        print("Number of Sequences:", num_sequences)
        print("Sequences and Rewards:")
        for sequence, reward in sequences_rewards:
            print(f"Sequence: {' '.join(sequence)}, Reward: {reward}")


        max_reward, best_buffer, best_coordinates, execution_time = functions.breach_protocol(matrix, sequences_rewards, buffer_size)
        print()
        print("Maximum reward weight: ", max_reward)
        print("Contents of the buffer: ", ' '.join(best_buffer))
        print("Coordinates of each token in order: ")
        for i in range(len(best_coordinates)):
            print(best_coordinates[i])
        print("Program execution time in ms: ", execution_time)
        print()

        save = input("Do you want to save the solution? (y/n): ")

        if save == 'y' or save == 'Y':
            functions.save_solution(max_reward, best_buffer, best_coordinates, execution_time, matrix, sequences_rewards)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except ValueError as e:
        print("Error:", e)

def manual_mode():
    try:
        while True:
            try:
                num_unique_tokens = int(input("Enter the number of unique tokens: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        while True:
            try:
                tokens = input("Enter the tokens (separated by space): ").split()
                if len(tokens) != num_unique_tokens:
                    print("Number of tokens does not match the specified number of unique tokens. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter tokens separated by spaces.")

        while True:
            try:
                buffer_size = int(input("Enter the buffer size: "))
                if buffer_size <= 0:
                    print("Buffer size must be a positive integer. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer for buffer size.")

        while True:
            try:
                matrix_width, matrix_height = map(int, input("Enter the matrix size (width and height, separated by space): ").split())
                if matrix_width <= 0 or matrix_height <= 0:
                    print("Matrix dimensions must be positive integers. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter two integers separated by space.")

        while True:
            try:
                num_sequences = int(input("Enter the number of sequences: "))
                if num_sequences <= 0:
                    print("Number of sequences must be a positive integer. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer for the number of sequences.")

        while True:
            try:
                max_sequence_length = int(input("Enter the maximum sequence length: "))
                if max_sequence_length <= 0:
                    print("Maximum sequence length must be a positive integer. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer for maximum sequence length.")


        matrix, sequences_rewards = functions.generate_matrix_and_sequence(num_unique_tokens, tokens, buffer_size, matrix_width, matrix_height, num_sequences, max_sequence_length)

        print("Matrix: ")
        for row in matrix:
            print(' '.join(row))
        print("Sequences and Rewards:")
        for sequence, reward in sequences_rewards:
            print(f"Sequence: {' '.join(sequence)}, Reward: {reward}")

        max_reward, best_buffer, best_coordinates, execution_time = functions.breach_protocol(matrix, sequences_rewards, buffer_size)
        print()
        print("Maximum reward weight: ", max_reward)
        print("Contents of the buffer: ", ' '.join(best_buffer))
        print("Coordinates of each token in order: ")
        for i in range(len(best_coordinates)):
            print(best_coordinates[i])
        print("Program execution time in ms: ", execution_time)
        print()

        save = input("Do you want to save the solution? (y/n): ")

        if save == 'y' or save == 'Y':
            functions.save_solution(max_reward, best_buffer, best_coordinates, execution_time, matrix, sequences_rewards)
    
    except ValueError as e:
        print("Error:", e)

while True:
    os.system("cls")
    print("1. File Input")
    print("2. Manual Input")
    choice = int(input("Choose option: "))
    if choice == 1:
        file_mode()
        break
    elif choice == 2:
        manual_mode()
        break
    else:
        print("There is no such option.")