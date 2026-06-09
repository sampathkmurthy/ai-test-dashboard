*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    chrome
${OPTIONS}    add_argument("--headless")

*** Keywords ***
Open Headless Browser
    Open Browser    https://the-internet.herokuapp.com/login    ${BROWSER}    options=${OPTIONS}
