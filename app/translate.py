from googletrans import Translator


async def translate(text, source_language, dest_language):
    tr = Translator()
    res = await tr.translate(text, dest_language, source_language)
    return res
