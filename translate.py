import asyncio
from googletrans import Translator


async def translate_text():
    async with Translator() as translator:
        result = await translator.translate('Hola', dest="ru", src="es")
        # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
        print(result.text)


async def my_tr():
    tr = Translator()
    res = await tr.translate("Hola", dest="ru")
    return res

asyncio.run(translate_text())
print(asyncio.run(my_tr()).text)
