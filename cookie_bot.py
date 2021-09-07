import pyautogui, asyncio, time, random, logging


async def do_daily(): #22 hour cooldown 3600 seconds in 1 hour 
    while True: 
        # print(f">>daily {time.strftime('%X')}")
        pyautogui.write(str('>>daily'))
        pyautogui.press('enter')
        sleep_time = random.randint(22,24)
        logging.info(f"daily {sleep_time}")
        print(f"daily sleep {sleep_time} hours")
        await asyncio.sleep(3600*sleep_time)

async def gib_cookie(): #58 minute cooldown 60 seconds to minute
    while True: 
        current_time = int(time.strftime('%H'))
        if current_time > 9 and  current_time <23:
            #     print(f">>gibcookie @romano {time.strftime('%X')}")   
            pyautogui.write(str('>>gibcookie @Romano&Juliet#9642'))
            pyautogui.press('enter')
            sleep_time = random.randint(60, 75)
            logging.info(f"cookie {sleep_time}")
        print(f"cookie sleep {sleep_time}minutes")
        await asyncio.sleep(60*sleep_time)

async def main(): 
    await asyncio.sleep(10)
    print("starting")
    log = "log.log"
    logging.basicConfig(filename=log,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    logging.info('begin logging')
    daily = asyncio.create_task(do_daily())
    cookie = asyncio.create_task(gib_cookie())
    await daily
    await cookie


asyncio.run(main())
# 1) does cookiefarming 
    #done 
# 2) does daily 
#   done 
#   2b) needs to check the result of each with python ocr 
# 3) check kud w/ opencv OCR
# 4) check shop 
# 5) purchase from shop if requirements are met 
# 	a) find and click the button required if we have enough kud
# 6) log data in a sqlite database 