*** Settings ***
Library    geocoding_mock.py
Library    RequestsLibrary

*** Test Cases ***
Test Search Addresses With Mocked HTTP
    [Tags]    happy path
    ${mocked_result}=    Create List    {"display_name": "Магазин 1"}    {"display_name": "Магазин 2"}    {"display_name": "Магазин 3"}
    ${response}=    Create Dictionary    json=${mocked_result}
    Create Session    mocked_session    https://nominatim.openstreetmap.org
    ${headers}=    Create Dictionary    Content-Type    application/json
    ${resp}=    GET On Session    mocked_session    /search    params=${response}    headers=${headers}
    ${status}=    Set Variable    ${resp.status_code}
    Run Keyword If    '${status}' == '200'    Decode Response    ${resp}
    ...    ELSE    Log    Response status code is not 200
    Delete Session    mocked_session

*** Keywords ***
Decode Response
    [Arguments]    ${response}
    Run Keyword If    '${response.text}' != ''    Log    Decoded JSON: ${response.json()}
    ...    ELSE    Log    Response body is empty