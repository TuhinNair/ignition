Feature: hello

    Scenario: run hello with no name
        Given we have ignition installed
        When hello is passed in as a command
        Then the default hello message is printed out to stdout

    Scenario: run hello with a specific name input
        Given we have ignition installed
        When the hello command is passed in with a name option
        Then a hello <name> message is printed out to stdout
