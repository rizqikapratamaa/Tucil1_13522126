nama_file = input("Masukkan nama file (tanpa format): ")

try:
    with open("../test/" + nama_file + ".txt", 'r') as file:
        lines = file.readlines()

        try:
            buffer_size = int(lines[0])
        except ValueError:
            raise ValueError("Nilai buffer harus berupa bilangan bulat.")

        try:
            matrix_width, matrix_height = map(int, lines[1].split())
        except (ValueError, IndexError):
            raise ValueError("Format pengisian panjang dan lebar matriks tidak sesuai.")

        if matrix_height != len(lines[2:2+matrix_height]) or any(len(line.strip().split()) != matrix_width for line in lines[2:2+matrix_height]):
            raise ValueError("Dimensi matriks tidak sesuai dengan width dan height yang diharapkan.")

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
            raise ValueError("Number of sequences harus berupa bilangan bulat.")

        if num_sequences * 2 != len(lines) - (3 + matrix_height):
            raise ValueError("Jumlah sequence dan reward tidak sesuai dengan number of sequences yang diharapkan.")

        sequences_rewards = []

        for i in range(3+matrix_height, len(lines), 2):
            sequence = lines[i].strip().split()
            try:
                reward = int(lines[i+1])
            except ValueError:
                raise ValueError("Reward harus berupa bilangan bulat.")
            if reward <= 0:
                raise ValueError("Reward harus merupakan bilangan bulat positif.")
            sequences_rewards.append((sequence, reward))

    print("Buffer size:", buffer_size)
    print("Matrix width:", matrix_width)
    print("Matrix height:", matrix_height)
    print("Matrix:")
    for row in matrix:
        print(row)
    print("Number of Sequences:", num_sequences)
    print("Sequences and Rewards:", sequences_rewards)

    reward = 0
    my_sequences = []

except FileNotFoundError:
    print("File tidak ditemukan.")
except ValueError as e:
    print("Error:", e)
