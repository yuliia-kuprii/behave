Feature: Edit and delete a poll

 Scenario Outline: Create Poll from nav bar
        When I open Poll form from navigation bar
        And type User <name>
        And click save name button
        And type the Poll <title> in form
        And type a Poll <description> in form
        And select first date and time
        And select second date and time
        And click save button in form
        Then Poll is visible on the current page with <title>

        Examples: edit poll data
        | name       | title               | new_title           | description   |
        | Linda Pears| Automated poll 01   | edited title poll 01| description_1 |

  Scenario Outline: Edit poll
    When I click on My Polls
    And open Polls details with <title>
    And open edit mode
    And change to <new_title>
    And click save button to edit
    Then poll has a new <new_title>

    Examples: edit poll data
        | title               | new_title           | description   |
        | Automated poll 01   | edited title poll 01| description_1 |


    Scenario Outline: Delete Polls
        When I click on My Polls
        And open Polls details with <new_title>
        And Delete it
        And confirm deletion
        Then poll's <title> is not in the list

    Examples: edit poll data
        | title               | new_title | description   |
        | Automated poll 01   | edited title poll 01| description_1 |