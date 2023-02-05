from pelicanconf import * #get all my config variables
my_config = globals()
import pelican
import glob
import imgkit
import time
from pyppeteer import launch
import asyncio

pelican_obj, settings = pelican.get_instance(pelican.parse_arguments()) #get the default settings

#overwrite the defaults with my custom values from my config file
for key in settings.keys():
    if key in my_config.keys():
        print('Overriding key', key)
        settings[key] = my_config[key]
del my_config

#and now loop over the themes and make and run a new instance for each theme
theme_list = glob.glob('pelican-themes/*')
#theme = next(iter(theme_list))
for i, theme in enumerate(theme_list):
    print('Theme %s, %d of %d'%(theme, i, len(theme_list)))
    settings['THEME'] = theme
    #instantiate the instance
    # pelican_obj = pelican.Pelican(settings)
    # pelican_obj.run()
    try:
        pelican.Pelican(settings).run()
        time.sleep(1)
    except:
        continue

    #imgkit.from_file('output/index.html','theme_'+theme.split('\\')[1]+'.jpg')
    # options = {'width': 1920, 'height': 1080}
    # imgkit.from_url('http://127.0.0.1:8000/', 'theme_'+theme.split('\\')[1]+'.jpg',options=options)
    async def main():
        browser = await launch()
        page = await browser.newPage()
        await page.goto('http://127.0.0.1:8000/')
        await page.screenshot({'path': 'theme_'+theme.split('\\')[1]+'.png'})
        await browser.close()
    asyncio.get_event_loop().run_until_complete(main())