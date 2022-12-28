Feature:
  In order to be able to use all features of this site
  As My User
  I want to be able to register my user and log in

  Scenario: logging in
    Given There is my user in database
    When I send my credentials to POST /api/token/
    Then It returns a valid JWT token to me
    And I can verify that token by sending to POST /api/token/verify/

  Scenario: register a user
    Given There are no users in the database
    When I send my data to POST /api/signup/
    Then It returns me the same data I specified and 201 response status
    And There is one user in DB that has the data I provided
