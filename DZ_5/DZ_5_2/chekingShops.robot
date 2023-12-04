*** Settings ***
Library  geocoding.py

*** Test Cases ***
check characters
    [Documentation]  Checking addresses and number of shops
    ${city}=  Set Variable  Санкт-Петербург
    ${name}=  Set Variable  Nike
    ${file_name}=  Set Variable  addresses.txt
    ${count1}=  search_addresses  ${city}  ${name}
    ${count2}=  get_shop_name  ${file_name}
    Should Be Equal  ${count1}  ${count2}
