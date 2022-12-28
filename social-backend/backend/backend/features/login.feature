Feature:
  In order to use this site
  As My User
  I want to log in

  Scenario: logging in
    Given there is my user in database
    When I send my credentials to /api/token/
    Then It returns a valid JWT token to me
    And I can verify that token by sending to /api/token/verify/
