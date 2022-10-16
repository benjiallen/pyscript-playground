# Tests to run in playwright

## Scenario: search with only close matches

Search "ben"
Expect only "close matches" heading with 3 results

## Scenario: activate close match button

Search "ben"
Activate the first button
Expect an exact match, check details of match

## Scenario: search by handle with exact and close matches

Search "benjaminp"
Expect "exact match" and "close matches" heading
Check details of exact match
Check the number of close matches

## Scenario: search by name with spaces

Search "brian curtin"

## Scenario: activate reports button

Search "benjaminp"
Expect "reports" heading
Activate the first button
Expect an exact match, check details of match

## Scenario: activate manager button

Search "benjaminp"
Expect "manager" heading
Activate the first button
Expect an exact match, check details of match

## Check the presence of live region

Search "ben" and activate search button
Expect "search completed" added to notify area

## Notes

Should i be checking the value of the button and other attributes?
