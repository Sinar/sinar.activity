# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s sinar.activity -t test_project_activity.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src sinar.activity.testing.SINAR_ACTIVITY_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/sinar/activity/tests/robot/test_project_activity.robot
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

Scenario: As a site administrator I can add a ProjectActivity
  Given a logged-in site administrator
    and an add ProjectActivity form
   When I type 'My ProjectActivity' into the title field
    and I submit the form
   Then a ProjectActivity with the title 'My ProjectActivity' has been created

Scenario: As a site administrator I can view a ProjectActivity
  Given a logged-in site administrator
    and a ProjectActivity 'My ProjectActivity'
   When I go to the ProjectActivity view
   Then I can see the ProjectActivity title 'My ProjectActivity'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add ProjectActivity form
  Go To  ${PLONE_URL}/++add++ProjectActivity

a ProjectActivity 'My ProjectActivity'
  Create content  type=ProjectActivity  id=my-project_activity  title=My ProjectActivity

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the ProjectActivity view
  Go To  ${PLONE_URL}/my-project_activity
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a ProjectActivity with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the ProjectActivity title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
