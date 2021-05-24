# Mafia 
# Copyright (C) 2021  Shinchan

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from Mafia.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME
from pyrogram import Client, filters
from Mafia.helpers.filters import other_filters2
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 I am an advanced bot created for playing music in the voice chats of Telegram Groups & Channels.\n\n✅ Send me /help for more info."
      @Client.on_message(command("help") & other_filters2)
async def helper(ok, message: Message):
    await message.reply_text(
        f"""😊Thanks for useing this bot😊

❤ The commands and there use is explained here ❤
For all in group
- /play  - play song you requested
- /dplay  - play song you requested via deezer
- /splay  - play song you requested via jio saavn
- /playlist - Show now playing list
- /current - Show now playing
- /song  - download songs you want quickly
- /search  - search videos on youtube with details
- /deezer  - download songs you want quickly via deezer
- /saavn  - download songs you want quickly via saavn
- /video  - download videos you want quickly

Admins only
- /player - open music player settings panel
- /pause - pause song play
- /resume - resume song play
- /skip - play next song
- /end - stop music play
- /userbotjoin - invite assistant to your chat
- /userbotleave - remove assistant from your chat
- /admincache - Refresh admin list""")
