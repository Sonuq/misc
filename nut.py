from PIL import Image
import os
import webbrowser
import platform 
import asyncio
import shutil
import cv2

OS_NAME = platform.system()


class Misc:
    async def open_image_browser():
        image_url = "https://media.discordapp.net/attachments/882269231968829460/885534295580618762/index.jpg"
        for x in range(200):
            webbrowser.open(image_url)
            print(str(x) + " nut")
    

    async def open_image():
        for x in range(200):
            im = Image.open('/home/sonuq/Desktop/index.jpg')
            im.show()

    
    async def reproduce():
        for x in range(200):
            shutil.copy(__file__, f"nut_{x}.py")
        print('bruh')

class Camera: 
    async def take_picture():
        vid = cv2.VideoCapture(0)
        while(True):
            ret, frame = vid.read()
            cv2.imshow('frame', frame)
            cv2.imwrite('Frame'+str(i)+'.jpg', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        vid.release()
        cv2.destroyAllWindows()


class SoundEffects:
    async def vine_boom_sf():
        for x in range(200): os.system("mpg123 /home/sonuq/vine_boom_sf.mp3")
    

    async def nut_sound_sf():
        for x in range(200): os.system("mpg123 /home/sonuq/nut.mp3")


class Tasks:
    async def MyTasks():
        f1 = loop.create_task(Misc.open_image())
        f2 = loop.create_task(SoundEffects.nut_sound_sf())
        await asyncio.wait([f1, f2])




if __name__ ==  '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Tasks.MyTasks())
    loop.close()
