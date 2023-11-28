
class Imdb_Locator:
    #since expand is button no need of data
    expan_xpath = '//button[@data-testid="adv-search-expand-all"]/span[@class="ipc-btn__text"]'
    name_id = "text-input__7"
    bd_min_id = "text-input__8"
    bd_max_id = "text-input__9"
    bd_day_id = "text-input__10"
    aw_re_path = '//div[@class="ipc-accordion__item__content_inner"]//button[@data-testid="test-chip-id-oscar_best_actress_nominees"]'
    sear_top_xpath = '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[5]/div[2]/div/div/div[2]/div/svg'
    sear_opt_value = 'Place of birth'
    gen_path = '//div[@class="ipc-accordion__item__content_inner"]//button[@data-testid="test-chip-id-FEMALE"]'
    ad_name_ch_id = "include-adult-names"
    search_path = '//button[@data-testid="adv-search-get-results"]//span[@class="ipc-btn__text"]'


