import cfscrape

import hearthstone.hearthpwn as hearthpwn

site_url = "http://www.hearthpwn.com/cards?display=1&filter-set=106&filter-unreleased=1"
content = '<a class="rarity-1 set-107 manual-data-link" href="/cards/49676-smugglers-run" data-id="50245" data-type-id="295636317" >Smuggler&#x27;s Run</a> </td><td class="col-type">Ability</td><td class="col-class"><span class="class-paladin"></span>&nbsp;Paladin</td><td class="col-cost">1<span class="icon-mana"></span></td><td class="col-attack">0<span class="icon-attack"></span></td><td class="col-health">0<span class="icon-health"></span></td></tr><tr class="even"><td class="col-name"> <a class="rarity-1 set-107 manual-data-link" href="/cards/49745-alleycat" data-id="50254" data-type-id="295636317" >Alleycat</a> </td><td class="col-type">Minion</td><td class="col-class"><span class="class-hunter"></span>&nbsp;Hunter</td><td class="col-cost">1<span class="icon-mana"></span></td><td class="col-attack">1<span class="icon-attack"></span></td><td class="col-health">1<span class="icon-health"></span></td></tr><tr class="odd"><td class="col-name"> <a class="rarity-1 set-107 manual-data-link" href="/cards/49685-grimscale-chum" data-id="50364" data-type-id="295636317" >Grimscale Chum</a> </td><td class="col-type">Minion</td><td class="col-class"><span class="class-paladin"></span>&nbsp;Paladin</td><td class="col-cost">1<span class="icon-mana"></span></td><td class="col-attack">2<span class="icon-attack"></span></td><td class="col-health">1<span class="icon-health"></span></td></tr><tr class="even"><td class="col-name"> <a class="rarity-1 set-107 manual-data-link" href="/cards/49692-kabal-lackey" data-id="50239" data-type-id="295636317" >Kabal Lackey</a> </td><td class="col-type">Minion</td><td class="col-class"><span class="class-mage"></span>&nbsp;Mage</td><td class="col-cost">1<span class="icon-mana"></span></td><td class="col-attack">2<span class="icon-attack"></span></td><td class="col-health">1<span class="icon-health"></span></td></tr><tr class="odd"><td class="col-name"> <a class="rarity-4 set-107 manual-data-link" href="/cards/49641-meanstreet-marshal" data-id="50453" data-type-id="295636317" >Meanstreet Marshal</a> </td><td class="col-type">Minion</td><td class="col-class"><span class="class-paladin"></span>&nbsp;Paladin</td><td class="col-cost">1<span class="icon-mana"></span></td><td class="col-attack">1<span class="icon-attack"></span></td><td class="col-health">2<span class="icon-health"></span></td></tr><tr class="even"><td class="col-name"> <a class="rarity-1 set-107 manual-data-link" href="/cards/49646-mistress-of-mixtures" data-id="50243" data-type-id="295636317" >Mistress of Mixtures</a> </td><td class="col-type">Minion</td><td class="col-class"></td><td class="col-cost">1<span class="icon-mana"></span></td><td class="col-attack">2<span class="icon-attack"></span></td><td class="col-health">2<span class="icon-health"></span></td></tr><tr class="odd"><td class="col-name"> <a class="rarity-5 set-107 manual-data-link" href="/cards/49624-patches-the-pirate" data-id="50353" data-type-id="295636317" >Patches the Pirate</a> </td><td class="col-type">Minion</td><td class="col-class"></td><td class="col-cost">1<span class="icon-mana"></span></td><td class="col-attack">1<span class="icon-attack"></span></td><td class="col-health">1<span class="icon-health"></span></td></tr><tr class="even"><td class="col-name"> <a class="rarity-3 set-107 manual-data-link" href="/cards/49759-small-time-buccaneer" data-id="50261" data-type-id="295636317" >Small-Time Buccaneer</a> </td><td class="col-type">Minion</td><td class="col-class"></td><td class="col-cost">1<span class="icon-mana"></span></td><td class="col-attack">1<span class="icon-attack"></span></td><td class="col-health">2<span class="icon-health"></span></td></tr><tr class="odd"><td class="col-name"> <a class="rarity-4 set-107 manual-data-link" href="/cards/49758-weasel-tunneler" data-id="50242" data-type-id="295636317" >Weasel Tunneler</a> </td><td class="col-type">Minion</td><td class="col-class"></td><td class="col-cost">1<span class="icon-mana"></span></td><td class="col-attack">1<span class="icon-attack"></span></td><td class="col-health">1<span class="icon-health"></span></td></tr><tr class="even"><td class="col-name"> <a class="rarity-3 set-107 manual-data-link" href="/cards/49643-counterfeit-coin" data-id="50348" data-type-id="295636317" >Counterfeit Coin</a> </td><td class="col-type">Ability</td><td class="col-class"><span class="class-rogue"></span>&nbsp;Rogue</td><td class="col-cost">0<span class="icon-mana"></span></td><td class="col-attack">0<span class="icon-attack"></span></td><td class="col-health">0<span class="icon-health"></span></td></tr><tr class="odd"><td class="col-name"> <a class="rarity-1 set-107 manual-data-link" href="/cards/49734-freezing-potion" data-id="50225" data-type-id="295636317" >Freezing Potion</a> </td><td class="col-type">Ability</td><td class="col-class"><span class="class-mage"></span>&nbsp;Mage</td><td class="col-cost">0<span class="icon-mana"></span></td><td class="col-attack">0<span class="icon-attack"></span></td><td class="col-health">0<span class="icon-health"></span></td></tr> </tbody> </table> </div> <div class="listing-footer"> '


def get_input(text):
    try:
        return int(input(text))
    except TypeError:
        print("Not a number")
        exit()


def get_site_content(url):
    scraper = cfscrape.create_scraper(js_engine="Node")
    return scraper.get(url).text


hearthpwn.directory.check_output_directories()

# page_index_end = get_input("Enter end index: ")
page_index_end = 2

for page_index in range(1, page_index_end):
    site_url = hearthpwn.page.modify_display_type(site_url)
    site_url = hearthpwn.page.modify_page(site_url, page_index, page_index_end)

    print("Loading " + site_url)

    # content = get_site_content(site_url)
    hearthpwn.downloader.start_download(content, page_index)

hearthpwn.logger.print_log()
