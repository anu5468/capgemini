Feature: HealthPackage

  Background:Healthpackage module should be present
    Given user is able to launch browser
    When user is able to click on the labtest module
    Then user is able to click on the healthpackage module
    And user is able to select one package
#    Then user is able to click on select
    Then user is able to select one patient
    And user is able to click on add patient details

  Scenario Outline:
    Then user is able to enter phonenumber "<number>"
    And user is able to click on continue
    And user is able to click on cont
    Then user is able to click on add patient button
    Then user is able to click on plus icon
    And user is able to enter patient name "<pname>"
    And user is able to enter age "<age>"
    Then user is able to select radio button
    Then user is able to click on submit
    And user is able to click on add new address
    And user is able to enter contact name "<cname>"
    Then user is able to enter pincode "<pcode>"
    Then user is able to enter flatnumber "<flatno>"
    And user is able to enter street name "<sname>"
    And user is able to select home
    Then user is able to click on save address
    Then user is able to click on slot selection continue
    And user is able to click on paycash button
#    Then user is able to click on place order


    Examples:
      | number     |      | pname   |     | age |    | cname |   | pcode  |   | flatno |     | sname  |
      | 8904245127 |      | ahayoy  |     | 24  |    |  anu  |   | 400001 |   | 4      |     | mgroad |
#      | 9738735529 |      | shaian  |     | 43  |    | sanu  |   | 400001 |   | 4      |     | jcroad |
#      | 9738735529 |      | shri    |     | 98  |    | anu   |   | 400001 |   | 5      |     | kcroad |
#      | 9738735529 |      | kadhar  |     | -5  |    | sri   |   | 572222 |   | 65     |     | mtroad |
#      | 911367641  |      | sohel   |     | 15  |    | sri   |   | 576909 |   | 87     |     | jkroad |