Feature: Currency API
  Verify that the currency API fetches, stores and returns correct data.

  Scenario: API root is running
    Given the API is running
    When I visit the root endpoint
    Then I should receive a status 200 and message "API is running"

  Scenario: Fetch and save currency rates
    Given the API is running
    When I fetch currency rates
    Then the response should confirm "Rates fetched and saved"

  Scenario: Get list of currencies
    Given currency rates are fetched
    When I request the list of currencies
    Then I should receive a non-empty list containing "USD" or "EUR"

  Scenario: Get rates by specific date
    Given currency rates are fetched
    When I request rates for the first available date
    Then I should receive a list of rates with correct currency, rate and date

  Scenario: Database connection
    Given the database is available
    Then I should be able to query CurrencyRate without errors

  Scenario: Data integrity
    Given currency rates are fetched
    Then all rates should have valid currency, rate > 0, and valid date
