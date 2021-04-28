class FundsElement:
    deposit_button = "btn-primary"  # by Class Name
    deposit_page_title = "#page-content-wrapper > div.content.p-2.pt-5.pt-md-5.px-md-4 > div > div:nth-child(1) > div > div > span"  # by CSS
    enter_amount_dropdown = "/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[3]/div"  # by Class Name
    deposit_amount_field = "amountField"  # by ID
    payment_overview_dropdown = "/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[5]/div"  # by XPath
    will_be_charged_amount = "#deposit-3 > div > div.row.mb-3 > div.text-black.text-right.col"  # by CSS
    deposit_confirm_button = "/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[6]/div/div[5]/div/button"  # by XPath
    bank_details_confirm_button = "#modal-bank-details___BV_modal_footer_ > div > button"  # CSS
    deposit_form= "bg-white"  # by Class Name
    deposit_see_all_transaction = "float-right"  # by Class Name
    deposit_transaction_page_title = "#page-content-wrapper > div.content.p-2.pt-5.pt-md-5.px-md-4 > div > div:nth-child(1) > div > div > span"  # by CSS Selector
    withdraw_button = "btn-outline-primary"  # by Class Name
    withdraw_page_title = "#page-content-wrapper > div.content.p-2.pt-5.pt-md-5.px-md-4 > div > div:nth-child(1) > div > div > span"  # by CSS
    withdraw_amount_field = "amountField"  # by ID
    withdraw_submit_button = "btn-primary"  # by Class
    withdraw_see_all_transaction = "float-right"  # by Class Name
    withdraw_transaction_page_title = "#page-content-wrapper > div.content.p-2.pt-5.pt-md-5.px-md-4 > div > div:nth-child(1) > div > div > span"  # by CSS
    transfer_button = "float-right"  # by Class Name
    transfer_page_title = "/html/body/div/div/div/div[2]/div[2]/div/div[1]/div/div/span"  # by XPath
    transfer_from_field = "/html/body/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[1]/select"  # by XPath
    transfer_to_field = "/html/body/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/select"  # by Xpath
    transfer_amount_field = "amountField"  # by ID
    submit_button = "col-md-3"  # by Class Name
    main_wallet_amount = "#page-content-wrapper > div.content.p-2.pt-5.pt-md-5.px-md-4 > div > div.row > div.col-md-10.col-lg-6 > div > div > div.list-group.mt-2.d-inline > div:nth-child(1) > span:nth-child(2)"  # by CSS
    evo_amount = "#page-content-wrapper > div.content.p-2.pt-5.pt-md-5.px-md-4 > div > div.row > div.col-md-10.col-lg-6 > div > div > div.list-group.mt-2.d-inline > div:nth-child(2) > span:nth-child(2)"  # by CSS
    transaction_page_navigator = "justify-content-center"  # by Class Name
    deposit_payment_type_field = "__BVID__141"  # by ID
    transfer_form = "card"  # by Class Name
    transfer_amount_is_not_valid = "#page-content-wrapper > div.content.p-2.pt-5.pt-md-5.px-md-4 > div > div.row > div.col-md-10.col-lg-6 > div > div > div.w-100.mt-2 > span > div > span"  # by CSS

class AccountElement:
    name_field = "nameField"  # by ID
    save_changes_button = "/html/body/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/span/form/button"  # by XPath

class ReferrerElement:
    memberlist_tab = "/html/body/div/div/div/div[2]/div[2]/div/div/div[1]/ul/li[1]/a"  # by XPath
    user_id_link = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[1]/div/a"  # by Xpath
    user_id_exit = "w-100"  # by Class Name
    report_tab = "/html/body/div/div/div/div[2]/div[2]/div/div/div[1]/ul/li[2]/a"  # by XPath
    report_deposit = "card-body"  # by Class Name
    bet_record_tab = "/html/body/div/div/div/div[2]/div[2]/div/div/div[1]/ul/li[3]/a"  # by XPath
    bet_record_filter = "custom-select"  # by Class Name
    logout_button = "logout"  #  by Class Name

class NotificationElement:
    notification = "/html/body/div/div/div/div[2]/div[2]/div/div/a[1]/div"  # by XPath
    notification_detail = "show"  # by Class Name




