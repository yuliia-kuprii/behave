Feature: Create and Delete a Poll from home page and nav bar

#    Scenario Outline: Create Poll from home page
#        When I see CreatePoll button on the page
#        And I click on CreatePoll button from page
#        And type Poll <title>
#        And click save button on the page
#        Then Poll is visible on the current page with <title>
#
#    Examples: Data for home page
#        | title               |
#        | Automated poll 01   |
#

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

        Examples: Data for nav bar
        | name          | title             |   description |
        | Linda Pears   | Automated poll 01 | Automated description 01 |

#    Scenario: List of My polls
#        When I click on My Polls
#        Then I see a list of my polls


