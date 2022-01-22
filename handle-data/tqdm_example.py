import tqdm
import random


for i in tqdm.tqdm(range(100)):
    _ = [random.random() for _ in range(1000000)]
    