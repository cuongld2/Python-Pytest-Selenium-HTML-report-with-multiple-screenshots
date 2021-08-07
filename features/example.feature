@example
Feature: example
    Scenario Outline: Publishing the article
        Given Go to <page1>
        When Go to <page2>
        Then Go to <page3>

        Examples:
        |page1|page2|page3|
        |dev.to|facebook.com|twitter.com|
