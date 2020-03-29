Feature: Get Request - Sending Request and Validating the response

  Scenario: To Verify Response format
    Given I set REST API URL
    When I send Get Request api endpoint
    Then Response BODY should have correct format

  Scenario Outline: To Verify that Response contains values
    Given I set REST API URL
    When I send Get Request api endpoint
    Then Response BODY should contain <Value> value
    Examples:
      | Value       |
      | id          |
      | main        |
      | Description |
      | icon        |

  Scenario Outline: To Verify Response contain key value pair
    Given I set REST API endpoint
    When I send Get Request api endpoint
    Then <key> should have <Value> value
    Examples:
      | Key  | Value         |
      | name | Mountain View |