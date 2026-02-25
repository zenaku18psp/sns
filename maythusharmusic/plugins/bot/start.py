else:
        lols = None
        m = None
        try:
            out = private_panel(_)
            lol = await message.reply_text("**ω ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωє ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓ ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓᴄ ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓᴄᴏᴍ ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓᴄᴏᴍᴇ ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓᴄᴏᴍᴇ в ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓᴄᴏᴍᴇ вα ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓᴄᴏᴍᴇ вαв ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓᴄᴏᴍᴇ вαву ᥫ᭡**")
            
            await lol.delete()
            lols = await message.reply_text("**⚡️ѕ**")
            await asyncio.sleep(0.1)
            await lols.edit_text("⚡ѕт")        
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтα**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαя**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαят**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαятι**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαятιи**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαятιиg**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαятιиg.**")
            await lols.edit_text("**⚡ѕтαятιиg....**")
            
            m = await message.reply_sticker("CAACAgUAAxkBAAEP0-NpIJZD3PhPH5RITkr21yD7cmlaaQAC4w8AAh7zWVcwgHF1OyOemjYE")
            
            chat_photo = config.START_IMG_URL
            spoiler_needed = False
                
        except Exception as e:
            print(f"Error: {e}")
            chat_photo = config.START_IMG_URL
            spoiler_needed = False
            
        if lols:
            try:
                await lols.delete()
            except:
                pass
        if m:
            try:
                await m.delete()
            except:
                pass
        
        PREMIUM_EMOJI_1 = "6120465303177533732" 
        
        # 2. ဒုတိယ Anime ကောင်မလေး (Streaming Exp ဘေးနား)
        PREMIUM_EMOJI_2 = "6120591326107935086" 
        
        # 3. တတိယ Anime ကောင်မလေး (အောက်ဆုံး Button ဘေးနား)
        PREMIUM_EMOJI_3 = "6120398056874582504"

        # အစက်ကလေးများ
        PREMIUM_EMOJI_4 = "6205967094039709231"
        PREMIUM_EMOJI_5 = "6206217069726271155"
        PREMIUM_EMOJI_6 = "6204129896009042249"
        PREMIUM_EMOJI_7 = "6206275004540126842"
        PREMIUM_EMOJI_8 = "6205967094039709231"
        PREMIUM_EMOJI_9 = "6206217069726271155"
        PREMIUM_EMOJI_10 = "6204129896009042249"
        PREMIUM_EMOJI_11 = "6206275004540126842"
        
        # စာသားပြင်ဆင်မှု (HTML Format) - Fallback Emoji များကို အရောင်များဖြင့် ပြင်ဆင်ထားသည်
        START_TEXT = f"""
<emoji id="{PREMIUM_EMOJI_4}">🔴</emoji> ʜᴇʏ ʙᴀʙʏ : {message.from_user.mention} <emoji id="{PREMIUM_EMOJI_1}">🥺</emoji>
<emoji id="{PREMIUM_EMOJI_5}">🟢</emoji> ɪ ᴀᴍ {app.mention}, ʜᴇʀᴇ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴡɪᴛʜ ᴀ ꜱᴍᴏᴏᴛʜ ᴍᴜꜱɪᴄ ꜱᴛʀᴇᴀᴍɪɴɢ ᴇxᴘᴇʀɪᴇɴᴄᴇ <emoji id="{PREMIUM_EMOJI_2}">🤩</emoji>.

<emoji id="{PREMIUM_EMOJI_6}">🟡</emoji> ғᴇᴀᴛᴜʀᴇs
<emoji id="{PREMIUM_EMOJI_7}">🔴</emoji> ʜǫ ᴀᴜᴅɪᴏ : 320ᴋʙᴘs sᴛʀᴇᴀᴍɪɴɢ
<emoji id="{PREMIUM_EMOJI_8}">🔴</emoji> sᴛʀᴇᴀᴍ sᴜᴘᴘᴏʀᴛ : ᴀᴜᴅɪᴏ-ᴠɪᴅᴇᴏ
<emoji id="{PREMIUM_EMOJI_9}">🟢</emoji> 24-7 ᴜᴘᴛɪᴍᴇ : ᴇɴᴛᴇʀᴘʀɪsᴇ ʀᴇʟɪᴀʙɪʟɪᴛʏ
<emoji id="{PREMIUM_EMOJI_10}">🟡</emoji> ᴘʟᴀʏ ᴄᴏᴍᴍᴇɴᴛꜱ : ᴘʟᴀʏ, ᴠᴘʟᴀʏ 
<emoji id="{PREMIUM_EMOJI_11}">🔴</emoji> ʙᴀsᴇᴅ ᴏɴ : ʏᴏᴜᴛᴜʙᴇ ᴀᴘɪ

<emoji id="{PREMIUM_EMOJI_4}">🔴</emoji> ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ <emoji id="{PREMIUM_EMOJI_3}">😙</emoji>."""

        await message.reply_photo(
            photo=chat_photo,
            caption=START_TEXT,
            reply_markup=InlineKeyboardMarkup(out),
            has_spoiler=spoiler_needed,
            parse_mode=ParseMode.HTML 
        )
        
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOGGER_ID,
                f"{message.from_user.mention} ʜᴀs sᴛᴀʀᴛᴇᴅ ʙᴏᴛ. \n\n**ᴜsᴇʀ ɪᴅ :** {sender_id}\n**ᴜsᴇʀ ɴᴀᴍᴇ:** {sender_name}",
            )
