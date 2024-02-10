import random

import random

while True:
    token_sum = int(input("Masukkan jumlah token: "))
    unique_token = list(map(str, input("Masukkan kode unik dipisahkan dengan spasi: ").split()))

    if len(unique_token) == token_sum:
        break
    else:
        print("Jumlah token unik tidak sesuai dengan jumlah yang diminta. Silakan coba lagi.")

print("Unique token:", unique_token)

buffer = int(input("Masukkan jumlah buffer: "))
width, height = map(int, input("Masukkan panjang dan lebar matriks dipisahkan dengan spasi: ").split())

matrix = [[random.choice(unique_token) for i in range(width)] for j in range(height)]

jumlah_sekuens = int(input("Masukkan jumlah sekuens: "))
ukuran_max_sekuens = int(input("Masukkan ukuran maksimal sekuens: "))

for row in matrix:
    print(row)

# Membuat sekuens dan bobotnya secara acak dari unique_token
sekuens_list = []
bobot_list = []
for _ in range(jumlah_sekuens):
    ukuran_sekuens = random.randint(1, ukuran_max_sekuens)  # Ukuran sekuens dihasilkan secara acak antara 1 dan ukuran_max_sekuens
    sekuens = random.choices(unique_token, k=ukuran_sekuens)
    bobot = random.randint(1, 10)  # Bobot dihasilkan secara acak antara 1 dan 10
    sekuens_list.append(sekuens)
    bobot_list.append(bobot)

# def brute_force(matriks, sekuens, buffer):
#     # Mengubah matriks menjadi list
#     matriks_list = [item for sublist in matriks for item in sublist]
    
#     # Mencari semua kombinasi dari matriks_list dengan panjang maksimal buffer
#     kombinasi = []
#     for i in range(len(matriks_list)):
#         for j in range(i+1, min(i+buffer+1, len(matriks_list))):
#             kombinasi.append(matriks_list[i:j])
    
#     # Mencari sekuens dalam kombinasi
#     for k in kombinasi:
#         if k == sekuens:
#             return True
#     return False

# Mencetak hasil
print("Sekuens:", sekuens_list)
print("Bobot:", bobot_list)



def cli():
    while True:
        token_sum = int(input("Masukkan jumlah token: "))
        unique_token = list(map(str, input("Masukkan kode unik dipisahkan dengan spasi: ").split()))

        if len(unique_token) == token_sum:
            break
        else:
            print("Jumlah token unik tidak sesuai dengan jumlah yang diminta. Silakan coba lagi.")

    print("Unique token:", unique_token)

    buffer = int(input("Masukkan jumlah buffer: "))
    width, height = map(int, input("Masukkan panjang dan lebar matriks dipisahkan dengan spasi: ").split())



    matrix = [[random.choice(unique_token) for i in range(width)] for j in range(height)]

    for row in matrix:
        print(row)

def using_file():
    sequences = []
    rewards = []

    no_sequence = int(input("Masukkan jumlah sequence yang diinginkan: "))
    for i in range(no_sequence):
        sequence_input = input(f"Masukkan elemen sequence ke-{i+1} dipisahkan dengan spasi: ")
        reward = int(input(f"Masukkan reward untuk sequence ke-{i+1}"))
        sequence = [x for x in sequence_input.split()]
        sequences.append(sequence)
        rewards.append(reward)

    print("sequences:", sequences)
    print("rewards:", rewards)