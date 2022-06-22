const GoogleLocalResultScrapper = require('./google_local_result_scrapper');

/**
 * This example searches for companies in Lekki, Lagos Nigeria.
 */

(async ()=>{
    const bot = new GoogleLocalResultScrapper();

    try {
        await bot.initPuppeteer(false);

        const query = 'spa in noida';

        const records = await bot.visitGoogle(query, 1);
       
        const res=await bot.filterRes({records})
        await bot.saveAsCSV({res, file_name: query});

        GoogleLocalResultScrapper.logDataStats(records);

    }catch (e) {
        console.error(e)
    }
    await bot.closeBrowser();

})();
