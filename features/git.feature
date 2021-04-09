Feature: git

    Scenario: toolchain configuration for git
        When the user runs 'ignite --toolchain git --first-name John --last-name Doe --email john.doe@company.com'
        Then the git user profile is set with the user's name
        And the git email is set with user's email
        And the git commit template is configured