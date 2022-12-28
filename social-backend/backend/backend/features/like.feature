Feature:
  In order to check how viral my last post is
  As My User
  I want to check the amount of likes my last post gathered

  Scenario: likes for a specific post
    Given There is only one post in the database
    And There is three users in the database
    And Post has two likes from 2 different users (not mine)
    When I go to GET /api/posts/{post_id}/
    Then I receive a post information with two likes from different users

  Scenario: get specific like data
    Given There is only one post in the database
    And There is only my user in the database
    And Post has one like from me
    When I go to GET /api/likes/{like_id}/
    Then I receive a like information that is same with like object that is stored in the DB