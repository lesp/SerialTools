import mcpi.minecraft as minecraft
import SerialTools.py as st
import time
mc = minecraft.Minecraft.create()
try:
    st.find_board()
except:
    print("BOARD NOT FOUND")
while True:
    time.sleep(0.2)
    data = print_serial()
    if data == "FIRE":
        x,y,z = mc.player.getPos()
        tnt = 46
        mc.setBlocks(x+1, y+1, z+1, x+5, y+5, z+5, tnt, 1)
        mc.postToChat("Hit the blocks and RUN!!!")
    
