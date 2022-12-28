Feature:
  In order to find some useful or relaxing information
  As Any User
  I want to browse available posts

  Scenario: list of posts
    Given There are several posts in the database
    And There are authors of these posts in the database
    When I go to the page GET /api/posts/
    Then I can see three posts ordered by id

  Scenario: create a post
    Given There are no posts in the database
    And There is only my user in the database
    When I send information about my post to POST /api/post/
    Then I receive a post information back in 201 response
    And My post is stored in the database with the same data I provided before

  Scenario: retrieve a post
    Given There are two posts in the database
    And there is only my user in the database
    When I go to GET /api/posts/{id_of_post}/
    Then I receive a post data with id I provided
    And Received post data is the same as in the database