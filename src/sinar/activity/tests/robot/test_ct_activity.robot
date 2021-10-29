# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s sinar.activity -t test_activity.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src sinar.activity.testing.SINAR_ACTIVITY_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/sinar/activity/tests/robot/test_activity.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Activity
  Given a logged-in site administrator
    and an add Activity form
   When I type 'My Activity' into the title field
    and I submit the form
   Then a Activity with the title 'My Activity' has been created

Scenario: As a site administrator I can view a Activity
  Given a logged-in site administrator
    and a Activity 'My Activity'
   When I go to the Activity view
   Then I can see the Activity title 'My Activity'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Activity form
  Go To  ${PLONE_URL}/++add++Activity

a Activity 'My Activity'
  Create content  type=Activity  id=my-activity  title=My Activity

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Activity view
  Go To  ${PLONE_URL}/my-activity
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Activity with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Activity title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
