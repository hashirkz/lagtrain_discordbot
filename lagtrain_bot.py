import ascii_renderer
import os
import pathlib
import cv2
import pafy
import numpy as np
from PIL import Image
import youtube_dl
from discord.ext import commands


# video processor / discord bot to make ascii videos (frame by frame)
TOKEN = os.eviron.get('TOKEN')

# checks if youtube link is a real link / exists
def is_supported(url):
    extractors = youtube_dl.extractor.gen_extractors()
    for e in extractors:
        if e.suitable(url) and e.IE_NAME != 'generic':
            return True

    return False

def url_to_webm(url):

    video = pafy.new(url)

    formats = ('mp4', 'webm')
    for f in formats:
        best = video.getbest(preftype=f)
        if best != None:
            break

    return best.url


def makedir(path_name):
    try:
        if not os.path.exists(path_name):
            os.makedirs(path_name)
    except OSError:
        print('path_name directory already exists')


def get_ascii_frames(vid_path, w=50, h=22):
    name = pathlib.Path(vid_path).stem + '_frames'
    makedir(name)


    # capturing each frame as an image in the directory name
    # note the dimensions w=100 and h=44 are inverted and based on the aspect ratio h:w = 2.25 in discord
    i = 0
    vid = cv2.VideoCapture(vid_path)

    fps = 0
    while True:
        if not fps % 100 == 0:
            fps += 1
            continue



        ret, cur_frame = vid.read()
        cur_frame = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)

        cur_frame = cv2.resize(cur_frame, (w, h))
        cur_ascii_frame = ascii_renderer.ascii_str(path=None, img=cur_frame, w=w, h=h)


        frame_name = name[:-7] + '_' +str(i) + '.txt'
        with open(name + '\\' + frame_name, 'w') as cur_ascii_txtfile:
            cur_ascii_txtfile.write(cur_ascii_frame)

        if ret == False:
            break

        i += 1
        fps += 1


    vid.release()
    cv2.destroyAllWindows()



# discord bot stuff not advisable to change stuff unless u know what ur doing
client = commands.Bot(command_prefix='&')

@client.event
async def on_ready():
    print('running as {0.user}'.format(client))

@client.event
async def on_message(message):
    await client.process_commands(message)

    username = str(message.author).split('#')[0]
    msg = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {msg}: ({channel})')

    if message.author == client.user:
        return




# ascii video rendering script
@client.command(aliases=['frames'])
async def send_ascii_frames(ctx, url, w=70, h=27, fps=24):

    # fetches url and checks if it exists / is valid yt link
    if not is_supported(url):
        await ctx.send('unable to find yt link')
        return


    #discord function to send ascii frames
    #note the dimensions w=70 and h=27 are inverted and based on the aspect ratio h:w = 2.25 in discord
    url = url_to_webm(url)
    #await ctx.send(url)

    i = 0
    vid = cv2.VideoCapture(url)

    fps_in = vid.get(cv2.CAP_PROP_FPS)
    fps_out = fps

    index_in = -1
    index_out = -1

    try:
        while True:

            usefulframe = vid.grab()
            if not usefulframe:
                continue
            index_in += 1

            out_due = int(index_in / fps_in * fps_out)
            if out_due > index_out:

                ret, cur_frame = vid.retrieve()

                # if cur_frame == []:
                #     await ctx.send('cur_frame is null')

                cur_frame = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)

                cur_frame = cv2.resize(cur_frame, (w, h))
                cur_ascii_frame = ascii_renderer.ascii_str(path=None, img=cur_frame, w=w, h=h)

                await ctx.send('```' + cur_ascii_frame + '```')

                if ret == False:
                    break

                i += 1
    except:
        vid.release()
        cv2.destroyAllWindows()

    return

@client.command(aliases=['stop', 'end'])
async def end_frames(ctx):
    exit()

client.run(TOKEN)

