from pyrogram import Client, filters, types, errors, enums, raw
from pyrogram.types import Message, User, CallbackQuery
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from pyrogram.types.input_media import *
import threading
import jdatetime
import datetime
import zipfile
import shutil
import wget
import os

proxy = {
    "scheme": "http",  # "socks4", "socks5" and "http" are supported
    "hostname": "127.0.0.1",
    "port": 10808,
}
proxy = None
C, M = Client, Message
api_id = 7447592
api_hash = "bf96474b58fd173bca087217d01d16ad"
API_KEY = "7964675545:AAFeyzGVxAp61y-PJYgvnZHTLnJUouNgQWQ"
bot = Client(name="ZzipitBot", api_id=api_id, api_hash=api_hash, bot_token=API_KEY, proxy=proxy)
"""
pip install git+https://github.com/Mayuri-Chan/tgcrypto-pyrofork
pip install git+https://github.com/TelegramPlayGround/pyrogram
"""

start_fmt = "%Y/%m/%d - %H:%M:%S"

history_fmt = "%d_%m_%Y"

jhistory_fmt = "%Y_%m_%d"

fmt = "%H:%M:%S"

IKB = InlineKeyboardButton
IKM = InlineKeyboardMarkup
KEYB = KeyboardButton
IMD = InputMediaDocument
IMP = InputMediaPhoto
IMV = InputMediaVideo
IMAN = InputMediaAnimation
IMAU = InputMediaAudio
PRIVATE = enums.ChatType.PRIVATE
event = threading.Event()
FileSizeLimit = 2 * 1024 * 1024 * 1024

ADDING_FILES_KBR = IKM([[IKB(text="همینا رو زیپ کن 📚", callback_data="done_adding")]])


def remove_directory(directory_path):
    """
    Fully removes the given directory, including all files and subdirectories.

    Args:
        directory_path (str): The path to the directory to remove.

    Returns:
        bool: True if the directory was successfully removed, False otherwise.
    """
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return False

    if not os.path.isdir(directory_path):
        print(f"Path '{directory_path}' is not a directory.")
        return False

    try:
        shutil.rmtree(directory_path)
        print(f"Directory '{directory_path}' has been removed.")
        return True
    except Exception as e:
        print(f"Error removing directory '{directory_path}': {e}")
        return False


def get_file_info(message: M):
    file_info = False
    m = message
    if m.document:
        file_info = m.document
    if m.video_note:
        file_info = m.video_note
    if m.video:
        file_info = m.video
    if m.photo:
        file_info = m.photo
    if m.animation:
        file_info = m.animation
    if message.sticker:
        file_info = m.sticker
    if m.voice:
        file_info = m.voice
    if m.audio:
        file_info = m.audio
    return file_info


def nowtime():
    # Tehran_TZ
    Time = datetime.datetime.now() + datetime.timedelta(hours=3, minutes=30)
    # Time.today()
    return Time


def jnowtime():
    # Tehran_TZ
    Time = jdatetime.datetime.now() + jdatetime.timedelta(hours=3, minutes=30)
    return Time


def osremove(files: list):
    for f in files:
        try:
            os.remove(f)
        except:
            pass
    print(f"Deleted: {' | '.join(files)}")


def zipit(files, zipfilename):
    with zipfile.ZipFile(zipfilename, 'w') as ZiPit:
        for file in files:
            print(file)
            # with open(file, "rb") as cred:
            #    content = cred.read()
            # ZiPit.writestr(os.path.basename(file), content)
            ZiPit.write(file, arcname=os.path.basename(file))
            # ZiPit.write(file)
    print('Done zipingit.')
    return zipfilename


def zip_files(file_list, zip_name):
    """
    Zips the given files using their base names into a single zip file.

    Args:
        file_list (list): List of file paths to be zipped.
        zip_name (str): The name of the output zip file.

    Returns:
        bool: True if the files were successfully zipped, False otherwise.
    """
    try:
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for file_path in file_list:
                if os.path.isfile(file_path):
                    base_name = os.path.basename(file_path)
                    zipf.write(file_path, arcname=base_name)
                else:
                    print(f"Skipping invalid file: {file_path}")
        print(f"Files have been successfully zipped into '{zip_name}'.")
        return zip_name
    except Exception as e:
        print(f"Error zipping files: {e}")
        return False


def system_ping_manager(client, update: M):
    date1 = update.date
    msg1: M = update.reply_text(".")
    date2 = datetime.datetime.now()
    deltad = (date2 - date1).total_seconds()
    time1 = nowtime()
    msg2: M = msg1.edit_text(text="..")
    time2 = nowtime()
    deltat = (time2 - time1).total_seconds()
    msg2.edit_text(text="...")
    filename = None
    try:
        dl1 = nowtime()
        filename = wget.download("http://cachefly.cachefly.net/10mb.test")
        dl2 = nowtime()
        deltadl = round(10 / (dl2 - dl1).total_seconds(), 2)
    except:
        deltadl = None
    text = ("دریافت پیام توسط سرور: {} ثانیه\n"
            "**پاسخ به پیام: {} ثانیه**\n"
            "سرعت دانلود: {}MB/s"
            "\n{}").format(round(deltad, 3), round(deltat, 3), deltadl, jnowtime().strftime("%Y/%m/%d - %H:%M:%S"))

    osremove([filename])
    msg2.edit_text(text=text)


def ETPnumbers(reshte):
    reshte = str(reshte)
    etpn = {"1": "۱", "2": "۲", "3": "۳", "4": "۴", "5": "۵", "6": "۶", "7": "۷", "8": "۸", "9": "۹", "0": "۰"}
    for N in etpn:
        reshte = reshte.replace(N, etpn[N])
    return reshte


def convert_bytes_to_human_readable_size(bytes_input, lang="en", ashar=2):
    if bytes_input < 0:
        return "Input should be a non-negative number of bytes."

    # Define the size units and their respective thresholds
    if lang == "en":
        size_units = ['B', 'KB', 'MB', 'GB']
    if lang == "fa":
        size_units = ['بایت', 'کیلوبایت', 'مِگ', 'گیگ']

    threshold = 1024

    # Determine the appropriate unit and convert the size
    size = bytes_input
    unit_index = 0
    while size >= threshold and unit_index < len(size_units) - 1:
        size /= threshold
        unit_index += 1

    # Format the result with 2 decimal places
    # result = "{:.1f} {}".format(size, size_units[unit_index])
    result = "{} {}".format(round(size, ashar), size_units[unit_index])
    if lang == "fa":
        result = ETPnumbers(result)
    return result


def create_progress_bar(total, completed, bar_length=30, filled_char="█", empty_char="░"):
    """
    Creates a customizable progress bar.

    Parameters:
    - total (int): The total value (A).
    - completed (int): The completed value (B).
    - bar_length (int): The length of the bar in characters (default is 30).
    - filled_char (str): The character for the filled portion of the bar (default is "█").
    - empty_char (str): The character for the empty portion of the bar (default is "-").

    Returns:
    - str: The progress bar as a string.
    """
    if total <= 0:
        return "Total must be greater than 0."

    # Calculate the proportion of completion
    progress = min(max(completed / total, 0), 1)  # Clamp progress between 0 and 1
    filled_length = int(round(bar_length * progress))

    # Create the bar
    bar = filled_char * filled_length + empty_char * (bar_length - filled_length)
    percentage = round(progress * 100, 2)

    return f"[{bar}] {percentage}%"


class UserInfo:
    def __init__(self, user: User):
        self.user = user
        self.user_id = user.id
        self.sui = str(user.id)


cbthrs = convert_bytes_to_human_readable_size


@bot.on_message(filters=filters.command(["ping", "start"]) & filters.incoming, group=0)
def start_manager(client: C, update: M):
    command = update.command[0]
    ud = UserInfo(user=update.from_user)
    if command == "start":
        msg: M = update.reply_text(text="سلام صبح بخیر.\nاسم فایل زیپ رو بدون پسوند بنویس.")
        users_zipping[ud.sui] = {"files": [], "filename": None, "msg": msg, "filesize": 0, "bot_time": 0, "user_time": 0}
        return
    if command == "ping":
        system_ping_manager(client, update)
        return
    pass


@bot.on_message(filters=filters.text & filters.incoming)
def text_manager(client: C, update: M):
    ud = UserInfo(user=update.from_user)
    text = update.text
    if ud.sui in users_zipping:
        if not users_zipping[ud.sui]["filename"]:
            users_zipping[ud.sui]["filename"] = text
            msg = users_zipping[ud.sui]["msg"]
            msg.delete()
            msg: M = msg.reply_text(text="اسم **{}** به عنوان اسم فایل ذخیره شد. فایل ها رو بفرست.".format(text))
            users_zipping[ud.sui]["msg"] = msg


@bot.on_message(filters=filters.media & filters.incoming)
def media_manager(client: C, update: M):
    user = update.from_user
    ud = UserInfo(user=user)
    file_info = get_file_info(update)
    if ud.sui in users_zipping:
        if users_zipping[ud.sui]["filename"]:
            msg = users_zipping[ud.sui]["msg"]
            if file_info:
                msg.delete()
                ufilesize = users_zipping[ud.sui]["filesize"]
                ufile_size = file_info.file_size
                total_file_size = ufilesize + ufile_size
                if total_file_size < FileSizeLimit:
                    users_zipping[ud.sui]["files"].append(file_info.file_id)
                    users_zipping[ud.sui]["filesize"] = total_file_size
                    tedad = len(users_zipping[ud.sui]["files"])
                    FSLfa, TFSfa = cbthrs(FileSizeLimit, "fa"), cbthrs(total_file_size, "fa", 2)
                    cool_thing = create_progress_bar(total=FileSizeLimit, completed=total_file_size, bar_length=12)
                    text = ("به لیست اضافه شد! حواست باشه که محدودیت حجمی فعلی ربات {}ه.\n{} فایل. مجموعا {} از {}\n{}"
                            .format(FSLfa, ETPnumbers(tedad), TFSfa, FSLfa, cool_thing))
                    msg: M = update.reply_text(text=text, reply_markup=ADDING_FILES_KBR)
                    users_zipping[ud.sui]["msg"] = msg
                else:
                    # if len(users_zipping[ud.sui]["files"]) > 0:
                    #     msg: M = update.reply_text(text="نه دیگه حجمش زیاد شد، همینا رو زیپ میکنم.")
                    #     users_zipping[ud.sui]["msg"] = msg
                    #     zip_user_files(client, update, user)
                    # else:
                    msg: M = update.reply_text(text="این خیلی بزرگه جا نمیشه بیخیال، یچیز دیگه بفرست.")
            else:
                msg.delete()
                msg: M = update.reply_text(text="این که نشد! فایل بفرست.\n||فایل، عکس، فیلم حتی گیف و استیکر هم میتونی بفرستی!||")
                users_zipping[ud.sui]["msg"] = msg


def zip_user_files(client: C, update: M, user: User):
    isp = False
    if update:
        if update.chat.type == PRIVATE:
            isp = True
    else:
        isp = True

    ud = UserInfo(user=user)
    users_zipping_data = users_zipping[ud.sui]
    msg: M = users_zipping_data["msg"]
    msg.edit_text(text="در حال دانلود فایل ها...")
    file_ids = users_zipping_data["files"]
    direction = f"/zipped/{ud.sui}"
    remove_directory(direction)
    os.makedirs(name=direction, exist_ok=True)
    filename = "{}.zip".format(users_zipping_data["filename"])
    path = os.path.join(direction, filename)
    files = []
    for file_id in file_ids:
        tmp_fp = bot.download_media(file_id)
        files.append(tmp_fp)
    msg.edit_text(text="در حال زیپ کردن فایل ها...")
    ziped_file = zipit(files, path)
    msg.edit_text(text="در حال آپلود...")
    # caption = os.path.basename(ziped_file)
    # caption = ""
    if isp:
        bot.send_document(chat_id=ud.user_id, document=ziped_file, caption="کپشن")
    else:
        update.reply_to_message.reply_document(document=ziped_file, file_name=caption)
    msg.delete()
    users_zipping.pop(ud.sui)

    pass


@bot.on_callback_query()
def callback_manager(client, update: CallbackQuery):
    call_data = update.data
    # ud = UserInfo(user=update.from_user)
    if call_data == "done_adding":
        zip_user_files(client=client, user=update.from_user, update=update.message.reply_to_message)
        return
    pass


users_zipping = {}

bot.run()
