# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""⋆ **مرحبا بك {message.from_user.mention()} !**\n
⋆ [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **يسمح لك بتشغيل الموسيقى والفيديو في مجموعات من خلال محادثات الفيديو الجديدة في التلي**

⋆ **قم بإضافة البوت اللي مجموعتك لكي تبدا الحفله..😺♥️**

⋆ **تم برمجه هذا البوت بواسطه**
⋆ **[Mostafa alazizy](https://t.me/php_7)**
⋆ **[قناة السورس](https://t.me/BANDA1M)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 💞اضف البوت لمجموعتك💞 ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("💞اوامر تشغيل الاغاني💞", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("⋆ الاوامر..💞", callback_data="cbcmds"),
                    InlineKeyboardButton("⋆ مطور البوت..💞", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "⋆ جروب الدعم..💞", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "⋆ قناة السورس..💞", url=f"https://t.me/BANDA1M"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "💞مصطفي العزايري💞", url="https://t.me/php_7"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )



@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ طريقة اضافتي للمجموعة:

1.) اولا قم بإضافة البوت في مجموعتك.
2.) ثانيا قم برفعي مسؤل واعطائي جميع الصلاحيات عدا البقاء متخفيا.
3.) بعد أضافتي ورفعي ادمن قم بكتاابة امر /reload .
3.) قم بإضافة @{ASSISTANT_NAME} الي مجموعتك او استخد امر /userbotjoin للإضافة تلقائيا.
4.) قم بفتح دردشة صوتيه اولا قبل تشغيل فديو/اغنيه.
5.) احيانا امر  /reload يستطيع مساعدتك في حل مشاكل البوت بالمجموعه.

📌 اذا لم ينضم البوت المساعد الي المحادثه الصوتيه قم باستخدام امر /userbotleave ثم اضفه مره اخري 

💡 اذا كان عند أي استفسار قم بالدخول الي جروب الدعم: @{GROUP_SUPPORT}

⚡ قناة السورس @BANDA1M
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("💞العوده💞", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **مرحبا يروحي [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **» قم بالضغط علي الزر الذي تريده لمعرفه الاوامر لكل فئه منهم !**

⋆ قناه السورس @BANDA1M
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⋆ اوامر الادمنيه..💞", callback_data="cbadmin"),
                    InlineKeyboardButton("⋆ اوامر المطور..💞", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("⋆ الاوامر الاساسيه..💞", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("💞العوده💞", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 مرحبا بك في الاوامر الاساسيه:

» /mplay (لتشغيل اغنيه في المحادثه الصوتيه (اسم الاغنيه / الرابط 
» /mplay (لتشغيل فديو في المحادثه الصوتيه (اسم الفديو / الرابط 
» /vstream رابط البث الحي + الجوده 720 360 480
» /playlist - لعرض قائمة التشغيل
» /video (اسم الفديو) - تحميل فيديو من واسطه يوتيوب
» /song (اسم الاغنيه) - تحميل اغنيه من يوتيوب
» /lyric (اغنيه) - جلب كلمات اغنيه
» /search (الفديو/ الاغنيه) - لجلب لينك من علي اليوتيوب
» /ping - لمعرفة سرعة البوت
» /uptime - لعرض مده التشغيل للبوت
» /alive - لمعرفه اذا كا يعمل البوت

⚡ قناة السورس @revorb0t
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("💞العوده💞", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 اوامر الادمنيه:

» /pause -  ايقاف مؤقت
» /resume - استكمال التشغيل
» /skip - لتخطي الاغنيه
» /stop - لايقاف الاغنيه
» /vmute - لكتم البوت في المحادثة الصوتية
» /vunmute - لالغاء كتم البوت في المحادثة الصوتية
» /volume 1-200 - التحكم في صوت البوت (يجب ان يكون البوت الماساعد مشرف)
» /reload - تحديث البوت وتحديث قائمة الادمنية
» /userbotjoin - لدعوة البوت المساعد
» /userbotleave - لخروج البوت الماساعد

⚡ قناة السورس @BANDA1M
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("💞العوده💞", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 مرحبا بك في اوامر المطور:

» /rmw - لحذف جميع الملفات 
» /rmd - لحذف جميع الملفات المحمله
» /sysinfo - لمعرفه معلومات السيرفر
» /update - لتحديث بوتك لاخر نسخه
» /restart - لتحديث البوت
» /leaveall - خروج البوت من جميع المجموعات

⚡ قناة السورس @BANDA1M
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("💞العوده💞", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("أنت مسؤول مجهول! \ n \ n »قم بالعودة إلى حساب المستخدم من حقوق المسؤول.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("⋆ اغلاق القائمه..💞", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("مفيش حاجه شغاله..🙂", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر!", show_alert=True)
    await query.message.delete()
