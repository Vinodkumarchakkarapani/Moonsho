*** Settings ***
#Documentation       TC# 01  login with valid credentials for moonshot

Library     SeleniumLibrary
Library     Selenium2Library
#Library     Collections
Library     ../../py/properties.py
Library     ../../py/library.py
#Library     ../../py/HomePage.py
Resource    ../../PageClass/moonshot_loginpage.robot
Resource    ../../Objects/object.robot
#Resource    ../../Objects/object1.robot


*** Test Cases ***

TC_01_login with valid credentials for moonshot

    open browser
    login Moonshot app          ${username_moonshot}        ${password_moonshot}

TC_02_Verify the user is able to select the client as amazon from jump to client dropdown

    dashboard page

TC_03_Verify the user is able to click on Add plan button and select vision from add new plan pop-up

    select the vision plan from add new plan pop-up

TC_04_Verify the user is able to fill in all fields and create the plan in draft mode

    create a vision plan in draft mode

TC_05_Verify the user is able to navigate to plan summaries page and click on created plan

    view all the created plans from plan summaries page

TC_06_Verify if the user is able to select the first plan by clicking on "view all" link from latest activity

    select the created plan from all latest activity

TC_07_Verify if the user is able to edit and update the plan

    Edit and update plan

TC_08_Verify if the browser is closed automatically

    close the browser



















#    welcome page
#    ${welcome_page} =   properties.welcome_page
#    should be equal as strings          ${welcome_page}
###TC_02_User have to select the client as amazon
##
##TC_03_User is able to create a plan for amazon
##
##TC_04_ User is able to fill all the required fields in the plan
##
#TC_05_ User is able to save the plan as draft


