from pyrogram.types.bots_and_keyboards import *
from pyrogram import Client, types, filters
from urllib.parse import urlparse
from PIL import Image
import subprocess
import traceback
import yt_dlp
import string
import random
import json
import wget
import os
import re



C, M = Client, types.Message
api_id = 7447592
api_hash = "bf96474b58fd173bca087217d01d16ad"
API_KEY = "6192704322:AAHGowhe-DRcUsR20Sd1QfJbrogWNQhsFi0"
bot = Client(name="VideoDL", bot_token=API_KEY, api_id=api_id, api_hash=api_hash, no_updates=False)
Mani_J = 1044031423
bot.start()
bot.send_message(chat_id=Mani_J, text="Started...")
bot.stop()
print("Pedarat Started...")

Kabirak_YouTube_Videos = -1002027758698
IKB = InlineKeyboardButton
IKM = InlineKeyboardMarkup
DOGIG = 2 * 1024 * 1024 * 1023.5


def osremove(files: list):
    for f in files:
        try:
            os.remove(f)
        except:
            pass
    print(f"Deleted: {' | '.join(files)}")


def generate_random_tmp_filename(puffix="", suffix=None, length=8):
    letters_and_digits = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters_and_digits) for _ in range(length))
    if suffix:
        random_string += "." + suffix.replace(".", "")
    return f"{puffix}{random_string}"


def video_downloader(update: M, url):
    msg: M = update.reply_text(text="Loading...")

    idl = yt_dlp.YoutubeDL()
    idict = idl.extract_info(url, download=False)
    dest_fmt = None
    formats = idict["formats"]
    for fmt in formats:
        if fmt["height"] == 480:
            if fmt.get("acodec") and fmt.get("vcodec"):
                dest_fmt = fmt["format_id"]
                break

    # with open(f"yt-dlp_{update.from_user.id}.json", "w") as ytdlp_w:
        # json.dump(idict, ytdlp_w, indent=4, ensure_ascii=False)
    # update.reply_document(ytdlp_w.name)


    options = {
    # "format": "bestvideo[height=?480][fps<=?30]",
    # "format": "bestvideo[height=?480]",
    # "format": "height<=480",
    "format": dest_fmt,
    "outtmpl": "%(title)s.%(ext)s",
        }
    ydl = yt_dlp.YoutubeDL(options)


    try:
        info_dict = ydl.extract_info(url, download=False)
        with open(f"yt-dlp_{update.from_user.id}.json", "w") as ytdlp_w:
            json.dump(info_dict, ytdlp_w, indent=4, ensure_ascii=False)
        tags = " ".join([f"#{x}".replace(" ", "_") for x in info_dict["tags"]])
        categories = " ".join([f"#{x}".replace(" ", "_") for x in info_dict["categories"]])
    except Exception as E:
        print(E)
        msg.edit_text(text="امکان دانلود از لینک داده شده وجود ندارد.")
        return

    msg.edit_text(text="Downloading...")
    ydl.download([url])
    title = info_dict["fulltitle"]
    duration = info_dict["duration"]
    webpage_url = info_dict["webpage_url"]
    width = info_dict["width"]
    height = info_dict["height"]
    output_path = ydl.prepare_filename(info_dict)
    caption = f"**[{title}]({webpage_url})**\ntags:\n||{tags}||\n\ncategories:\n||{categories}||"
    thumb = get_yt_thumbnail(url, (width, height))

    msg.edit_text(text="Uploading..")
    try:
        update.reply_video(video=output_path, caption=caption, duration=duration, width=width, height=height, thumb=thumb, quote=False)
    except:
        update.reply_animation(animation=output_path, caption=caption, duration=duration, width=width, height=height, thumb=thumb, quote=False)
    osremove([output_path, thumb])
    msg.delete()
    update.delete()


def get_yt_thumbnail(video_url, size):
    video_options = {
        # 'format': 'bestvideo',
                     "quiet": True}
    vw, vh = size
    with yt_dlp.YoutubeDL(video_options) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        thumbnails = info_dict.get('thumbnails', [])
        thumbnail = max(thumbnails, key=lambda t: t.get('width', 0) * t.get('height', 0), default=None)

        if thumbnail:
            thumbnail_url = thumbnail.get('url')
            thumbnail_path = wget.download(thumbnail_url)
            thumb = YT_thumbnail(thumbnail_path, [vw, vh])
            thumb = thumbnail_checker(thumb, vw, vh)


            return thumb
        else:
            return None


def thumbnail_checker(image_path, width, height):
    with Image.open(image_path) as img:
        w, h = img.size
        maxt, maxv = max(w, h), max(width, height)
        if w > width:
            zarib = maxv/maxt
            w = int(w*zarib)
            h = int(h*zarib)
            img.thumbnail(size=(w, h))
            img.save(image_path)
    return image_path


def YT_thumbnail(image_path, video_size):
    vw, vh = video_size
    with Image.open(image_path) as img:
        width, height = img.size
        if vw < vh:
            cw = int((height**2 / width) / 2)
            crop_box = [
                width/2 - cw,  # left
                0,  # upper
                width / 2 + cw,  # right
                height  # lower
                        ]
            "left, upper, right, and lower"

            img = img.crop(crop_box)

        width, height = img.size
        max_dim = max(width, height)

        scale = 320 / max_dim

        new_width = round(width * scale)
        new_height = round(height * scale)

        img.thumbnail((new_width, new_height))
        img_path = image_path.split(".")
        img_path[-1] = "jpeg"
        img_path = ".".join(img_path)
        img.save(img_path, "jpeg")
        compress_thumbnail(img_path, img_path)
    return img_path


def compress_thumbnail(input_path, output_path, max_size_kb=200):
    while os.path.getsize(output_path) > max_size_kb * 1024:
        img = Image.open(input_path)
        img.save(output_path, 'JPEG', quality=img.info['quality'] - 5)


def extract_urls(input_string):
    url_pattern = re.compile(r'https?://\S+')

    matches = re.findall(url_pattern, input_string)

    if not matches:
        return False

    cleaned_urls = [urlparse(url).geturl() for url in matches]
    return cleaned_urls


@bot.on_message(filters.regex(r'https?://[^\s]+'))
def Main_VideoCommands(client, update: M):
    # urls = [x.url for x in update.entities if x.url]
    urls = extract_urls(update.text)
    for url in urls:
        video_downloader(update, url)


bot.run()
