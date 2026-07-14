import gdown 

url = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
gdown.download(url, 'P1_data.txt', quiet=False)

file_path = './P1_data.txt'

def count_word(file_path):
    word_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    return word_count

print(count_word(file_path))