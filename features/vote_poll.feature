Feature: Vote on a Poll

    Scenario Outline: Create Poll from home page
        When I see CreatePoll button on the page
        And I click on CreatePoll button from page
        And type Poll <title>
        And click save button on the page
        Then Poll is visible on the current page with <title>

    Examples:
        | title               |
        | Automated poll 01   |

    Scenario Outline: Vote on a Poll
      When I go to Vote section
      And type User <name>
      And click save name button
      And I select a nearest day
      And I select <day_time> and <end_time>
      And selected time is highlighted
      Then the time is Saved
      And selected day is highlighted

      Examples: day data
        | name |  day_time| end_time |
        | Linda|  00:00   | 02:00    |

    Scenario Outline: View results after voting
      When I go to Vote section
      And I select a nearest day
      And I select <day_time> and <end_time>
      And the time is Saved
      And go to Details section
      Then charts are displayed
#      And aligned with <day> selected

      Examples:
         | day_time|end_time |
         | 12:00  | 13:00    |



