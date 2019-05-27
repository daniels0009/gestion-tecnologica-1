Feature: User-Defined Datatype as Step Parameter

  Scenario Outline: Sum two numbers
    Given I have a calculator
    When I add "<x>" and "<y>"
    Then the calculator returns "<sum>"

    Examples:
        |  x    |  y   | sum    |
        |  3    |  2   |  5     |
        |  -2   |  -1  |  -3    |
        |  2.3  |  3.2 |  5.5   |
        |  -2.3 |  1.1 |  -1.2  |
