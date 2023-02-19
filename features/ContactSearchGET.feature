Feature: AIR API contacts tests

  @search @contact

  Scenario Outline: Basic search for contact by phone number
    Given an authorized session
      When I make a GET request to "https://api.aircall.io/v1/contacts/search" with parameters
    |phone_number|
    |+33652556756|
    Then the response status code should equal 200
    And the response status code should be among 200, 201
    And the response parameter "<key>" should equal "<value>"

Examples: Phone numbers and emails
| key | value |
| phone_numbers | +33652556756 |
| emails | test@acme.com |


  Scenario Outline: Basic search for contact by email
    Given an authorized session
      When I make a GET request to "https://api.aircall.io/v1/contacts/search" with parameters
    | email |
    | test@acme.com |
    Then the response status code should equal 200
    And the response status code should be among 200, 201
    And the response parameter "<key>" should equal "<value>"

Examples: Phone numbers and emails
| key | value |
| phone_numbers | +33652556756 |
| emails | test@acme.com |



  Scenario Outline: Basic search for contact by phone number and email
    Given an authorized session
      When I make a GET request to "https://api.aircall.io/v1/contacts/search" with parameters
    |phone_number| email |
    |+33652556756| test@acme.com |
    Then the response status code should equal 200
    And the response status code should be among 200, 201
    And the response parameter "<key>" should equal "<value>"

Examples: Phone numbers and emails
| key | value |
| phone_numbers | +33652556756 |
| emails | test@acme.com |