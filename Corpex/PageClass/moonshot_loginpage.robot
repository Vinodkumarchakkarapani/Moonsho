*** Settings ***
#Library    Browser
Library         SeleniumLibrary
#Library     Selenium2Library
#Library     Collections
#Library     Selenium2LibraryExt

Library     ../py/library.py
Library     ../py/properties.py
Resource    ../Objects/object.robot
#Resource    ../Objects/object1.robot
#Resource    ../Objects/object2.robot


*** Variables ***
${navigation}   xpath=//input[@formcontrolname="display_Name"]

*** Keywords ***
Open browser
    [Arguments]
    library.open browser    ${url}

login Moonshot app
    [Arguments]                   ${username_moonshot}        ${password_moonshot}


    library.login_to_moonshot     ${username_moonshot}        ${password_moonshot}
#    capture element screenshot    /html/body/app-root/app-login/div/div/div/div[1]/img       loginmoonshot.png
    sleep    10
    library.pop_up_username           ${pop-username}
    sleep    10
    library.pop up password           ${pop-password}
    library.pop up button

dashboard page
    sleep   60
#     library.display name
#    ${display_name} =    library.display name
#    log to console     display name ${display_name}
#    should be equal as strings    ${display_name}   United Healthcare Vision Benefit Summary Region Class

#    library.welcome page
#    ${welcome_page}=  library.welcome page
#    should be equal  ${welcome_page}    Ashvitha Prasad
#    log to console  ${welcome_page}
#    ${welcome_page} = re.match()
   library.jump to click dropdown
   sleep    10
   library.amazon dropdown value

select the vision plan from add new plan pop-up


#    log to console    ${dashboard}
#    library.amazon dashboard
##    ${dashboard} =   library.amazon dashboard
#    should be equal as strings      ${dashboard}     Amazon Dashboard
#    log to console     ${dashboard}
   library.add plan button
   sleep    10
   library.search vision              ${search_vision}
   library.vision link dropdown
   sleep    10
   library.save and add button


create a vision plan in draft mode
#    [Arguments]      ${display_name_text}   ${display_name}
    sleep   10
    library.scroll_up
    library.policy number        ${policy_number}
    sleep   10
    library.plan name             ${plan_name}
    library.select document category
    library.select secondary document
    library.select generic document
    library.select business level
    library.select carrier
    library.plan ID             ${plan_id}
    library.plan start renewal date
    sleep    10
    library.plan status
    library.issuing location
    library.commission          ${commission}
    library.tier
    library.search tags text
    should be equal    ${search_tag}     Plan Summary
#    log to console      ${search_tag}

#    should be true      library.display to client
    library.region selector     ${region_selector}
    library.class selector      ${class_selector}

    library.display name text
    sleep    5
    library.display name message
    sleep    5
#    ${username_string}=     get value       library.username label
##    should be equal     ${username_label.strip()}     ${username_string.strip()} bui
#    ${get_activity_name}=    library
#${text} =    Get Text    xpath=//td[contains(text(), "O BOTICARIO")]    ==    BOTICARIO
#    ${get_display_name}     builtin.get variables       ${navigation}
#    FOR    ${item}  IN    @get_display_name
#        log to console    ${item.text}
#    END


#    ${display_name_value}=   builtin.get variables    //input[@formcontrolname="display_Name"]
##
#    ${text}=    convert to string    ${display_name_value}
#    ${actual}=   convert to string    United Healthcare Vision Benefit Summary Region Class 2022
#
#    should be equal     ${item.text}  ${actual}
##    ${display_name}=   seleniumlibrary.get v    xpath="/html/body/app-home/main/article/div/div/app-dynamic-forms/form/div[1]/div/div[24]/input"    United Healthcare Vision Benefit Summary Region Class 2022
#    page should contain     United Healthcare Vision Benefit Summary Region Class 2022
#    log to console    ${display_name}
#    ${display_name} =    get display message    library.display name message

#    ${display_name}=    get text    library.display name message
#    ${display_name_text}=     ${display_name}

#    should be equal      ${display_name}   United Healthcare Vision Benefit Summary Region Class 2022


#    Should Be Equal    ${display_name}    ${display_name_text}
#    log to console    ${text}  ${actual}
    Should Be Equal    ${display_name_text}   United Healthcare Vision Benefit Summary Region Class 2022


    sleep    10
    library.save and add button

    sleep   10
    library.scroll up

view all the created plans from plan summaries page
    library.plan summaries dropdown
    sleep   5
    library.scroll up
    library.plan year button
    library.group by

select the created plan from all latest activity
    library.view all link text
    library.select existing plan


Edit and update plan
    sleep    10
    library.edit plan button
    library.edit policy number      ${edit_policy_number}
    library.update button

close the browser
    library.close browser