***Settings***
Library    SeleniumLibrary


***Test Cases***
Open Browser And Navigate
    Open Browser    https://translate.google.com/    Chrome
    Maximize Browser Window
    [Teardown]    Close All Browsers
