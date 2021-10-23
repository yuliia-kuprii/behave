class Locators():

    # homepage
    create_poll_homepage_by_class = "btn.btn-light.btn-lg.my-2"
    create_poll_navbar_by_xpath = "//*[@class='nav-item'][3]"
    save_button_home_xpath = "/html/body/app-root/app-landing/app-hero/app-poll-autocreate-modal/div/div/div/div[3]/button"

    #pop-ups inputs
    poll_title_pop_up_by_xpath = "/html/body/app-root/app-landing/app-hero/app-poll-autocreate-modal/div/div/div/div[2]/input"
    poll_name_pop_up_by_xpath = "*//app-update-user-modal/div/div/div/div[3]/input"
    poll_save_button_pop_up_by_xpath = "*//app-update-user-modal/div/div/div/div[4]/button"

    #  polls form
    title_field_by_id = "title"
    description_field_by_id = "description"
    save_button_by_xpath = "/html/body/app-root/app-poll-create/div/form/div[3]/button"
    edit_poll_save_button_xpath = "/html/body/app-root/app-poll-create/div/form/div[2]/button"

    # my polls
    actual_title_by_class = "text-secondary.prevent-line-increase.mb-0"
    my_polls_by_xpath = "//*[@class='nav-item'][2]"
    polls_list_by_class = "row"
    delete_button_by_css = "button.btn.btn-outline-secondary"
    edit_button_by_css = "button.btn.btn-outline-primary.mr-2"
    vote_tab_by_xpath = "/html/body/app-root/app-poll/div/div[2]/ul/li[2]/a"
    time_save_button_by_xpath = "/html/body/app-root/app-poll/div/app-poll-vote/div/app-poll-vote-date-modal/div/div/div/div[4]/button[1]"
    details_tab_by_xpath = "/html/body/app-root/app-poll/div/div[2]/ul/li[1]/a"
    all_charts_by_class = "row"
    near_day_by_xpath = "/html/body/app-root/app-poll/div/app-poll-vote/div/ul/li[1]/a/app-poll-vote-date/div"

