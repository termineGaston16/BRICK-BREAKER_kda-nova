import random
from objects.objects import blocks
from objects.block.block import Block

colors = [
    (255, 155, 0),
    (255, 0, 0 ),
    (35, 255, 0),
    (0, 255, 228),
    (4, 0, 255),
]

def block_array(rows, colums, block_width, block_height, spacing, xMove, yMove):
    for row in range(rows):
        for column in range(colums):
            x = column * (block_width + spacing) 
            y = row * (block_height + spacing) + 50 

            blocks.add(Block(block_width, block_height, (x + xMove), (y + yMove), colors[random.randint(0,4)]))
            


            


