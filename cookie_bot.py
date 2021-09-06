import pyautogui, asyncio, time

async def do_daily(): 
    while True: 
        print(f">>daily {time.strftime('%X')}")
        await asyncio.sleep(5)
    # pyautogui.write(str('>>roulette '+ str(betAmount) + ' color:red'))
    # pyautogui.press('enter')

async def gib_cookie(): 
    while True: 
        print(f">>gibcookie @romano {time.strftime('%X')}")
        await asyncio.sleep(1)

async def main(): 
    print("starting")
    daily = asyncio.create_task(do_daily())
    cookie = asyncio.create_task(gib_cookie())
    await daily
    await cookie


asyncio.run(main())
# 1) does cookiefarming 
# 2) does daily 
# 3) check kud w/ opencv OCR
# 4) check shop 
# 5) purchase from shop if requirements are met 
# 	a) find and click the button required if we have enough kud
# why