*** Settings ***
Library  main.py

*** Test Cases ***

check characters
    [Documentation]  Checking that the number of characters is 826
    ${status_1}=  Set Variable  Alive
    ${status_2}=  Set Variable  Dead
    ${status_3}=  Set Variable  unknown
    ${count}=  count_elements  ${status_1}  ${status_2}  ${status_3}
    Should Be Equal  ${count}  ${826}
