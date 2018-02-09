from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

pos = mc.player.getTilePos()

heights = [pos.y, pos.y]
count = 0

while count < 50:
    pos = mc.player.getTilePos()

    if pos.y < heights[0]:
        heights[0] = pos.y
    elif pos.y > heights[1]:
        heights[1] = pos.y
    print (heights)

    count += 1
    time.sleep(1)

mc.postToChat("Lowest: "+ str(heights[0]))
mc.postToChat("Highest: "+ str(heights[1]))
