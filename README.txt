
1. install behave
2. install modules from setupAPI file
3. run behave from console
4. use the .env file to change current credentials and urls






"""
Sample console output (Scenario 1 + summary)

repos\AirAPI> behave
>>
Using default path "./features"
Trying base directory: C:\Users\martin\source\repos\AirAPI\features
Feature: AIR API contacts tests # features/ContactSearchGET.feature:1

  @search @contact
    Given an authorized session                                                                # behave_rest/steps/__init__.py:13 0.001s
    When I make a GET request to "https://api.aircall.io/v1/contacts/search" with parameters   # behave_rest/steps/__init__.py:37
      | phone_number |
      | +33652556756 |


-----------REQUEST-----------
GET https://api.aircall.io/v1/contacts/search?phone_number=%2B33652556756
User-Agent: python-requests/2.28.2
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
Authorization: Basic 

None

-----------RESPONSE-----------
200 OK
Date: Fri, 20 Jan 2023 01:24:53 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 509
Connection: keep-alive
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
x-content-type-options: nosniff
x-download-options: noopen
x-permitted-cross-domain-policies: none
referrer-policy: strict-origin-when-cross-origin
cache-control: max-age=0, private, must-revalidate
x-request-id: 2dbcbea6-2806-4c4f-ae1c-980ff3f6594d
x-runtime: 0.106498
vary: Origin
x-envoy-upstream-service-time: 108
server: envoy

{"contacts":[{"id":130626794,"direct_link":"https://api.aircall.io/v1/contacts/130626794","first_name":"TestName","last_name":"TestLastName","company_name":null,"information":"TestInfo","is_shared":true,"created_at":1672995969,"updated_at":1672995969,"emails":[{"id":258591489,"label":"Office","value":"test@acme.com"}],"phone_numbers":[{"id":258591488,"label":"TestNumber","value":"+33652556756"}]}],"meta":{"count":1,"total":1,"current_page":1,"per_page":20,"next_page_link":null,"previous_page_link":null}}

Operation took 1.445s
    When I make a GET request to "https://api.aircall.io/v1/contacts/search" with parameters   # behave_rest/steps/__init__.py:37 1.452s
      | phone_number |
    And the response status code should be among 200, 201                                      # behave_rest/steps/__init__.py:70 0.000s
    And the response parameter "phone_numbers" should equal "+33652556756"                     # behave_rest/steps/__init__.py:81
Checking if phone_numbers equals "+33652556756"
Key FOUND: phone_numbers
    And the response parameter "phone_numbers" should equal "+33652556756"                     # behave_rest/steps/__init__.py:81 0.001s
Found match for value: +33652556756
.....................
.....................
1 feature passed, 0 failed, 0 skipped
6 scenarios passed, 0 failed, 0 skipped
30 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m7.517s
