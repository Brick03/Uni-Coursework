#!/usr/bin/env bats
load bats-extra

# local version: 1.6.0.1
# bash-specific test: Input validation

@test 'year not divisible by 4: common year' {
  run bash leapyear.sh 2015

  assert_success
  assert_output "false"
}

@test 'year divisible by 2, not divisible by 4 in common year' {
  run bash leapyear.sh 1970

  assert_success
  assert_output "false"
}

@test 'year divisible by 4, not divisible by 100: leapyear year' {
  run bash leapyear.sh 1996

  assert_success
  assert_output "true"
}

@test 'year divisible by 4 and 5 is still a leapyear year' {
  run bash leapyear.sh 1960

  assert_success
  assert_output "true"
}

@test 'year divisible by 100, not divisible by 400: common year' {
  run bash leapyear.sh 2100

  assert_success
  assert_output "false"
}

@test 'year divisible by 100 but not by 3 is still not a leapyear year' {
  run bash leapyear.sh 1900

  assert_success
  assert_output "false"
}

@test 'year divisible by 400: leapyear year' {
  run bash leapyear.sh 2000

  assert_success
  assert_output "true"
}

@test 'year divisible by 400 but not by 125 is still a leapyear year' {
  run bash leapyear.sh 2400

  assert_success
  assert_output "true"
}

@test 'year divisible by 200, not divisible by 400 in common year' {
  run bash leapyear.sh 1800

  assert_success
  assert_output "false"
}

@test 'No input should return an error' {
  run bash leapyear.sh

  assert_failure
  assert_output "Usage: leapyear.sh <year>"
}

@test 'Too many arguments should return an error' {
  run bash leapyear.sh 2016 4562 4566

  assert_failure
  assert_output "Usage: leapyear.sh <year>"
}

@test 'Float number input should return an error' {
  run bash leapyear.sh 2016.54

  assert_failure
  assert_output "Usage: leapyear.sh <year>"
}

@test 'Alpha input should return an error' {
  run bash leapyear.sh 'abcd'

  assert_failure
  assert_output "Usage: leapyear.sh <year>"
}
