# gra1-3d-64110w33n - brawon

READ THE FOLLOWING FULLY BEFORE PROCEEDING.

Prerequisites:
1. Clone/download the package into a new folder
2. Install Python 3
3. Install Selenium and Joblib for Python
4. Download ChromeDriver v78 and save in the root of that folder (Google it)
5. Update Chrome to Version 78.xxxx (if you have v79 that's cool, just make sure step 4 and 5 match)
6. Make sure PayPal is already set up with your shipping address and payment information (should already be the case if you've bought on Grailed before)

How to use: 
1. Open [config.py] and leave ONLY the *4* items you want to try for
2. In [config.py], make sure each item/URL has a comma after each closed quotation, EXCEPT for the final item
    1. Example [config.py] with random listings: 
        1. product_urls = [
            "https://www.grailed.com/listings/9520563-Target-Basics---Vineyard-Vines-Vineyard-Vines-x-Target-Waterproof-Deck-of-Cards",
            "https://www.grailed.com/listings/9510375-Hanes-Made-In-Usa-Vintage-90s-Hanes-pat-green-country-music-tour-band-t-shirt",
            "https://www.grailed.com/listings/9494616-Japanese-Brand---Tracey-Vest-LEXUS-TECTICAL-MULTIPOCKET-VEST-JACKET",
            "https://www.grailed.com/listings/9493058-Vintage-Vintage-notre-dame-tshirt-single-stitch"
            ]
3. Run [save_cookies.py] at least 10 minutes before the drop
    1. Login to Grailed in the pop up window (click top-right login), you might need to complete Captchas
    2. In 100 seconds, wait for another pop up window with PayPal to open
    3. Login to PayPal and ENABLE One Touch when prompted (click top-right login)
    4. Wait for the windows to close BY ITSELF, then [save_cookies.py] will terminate
4. Read the notes in [bot.py] and *EDIT* the drop time (line 23) if necessary
5. Run [bot.py] at least 3 minutes before the drop and wait (don't do anything intensive on your computer)
6. Pray to God you get your jawns
7. ??? Profit ???