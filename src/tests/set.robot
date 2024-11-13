*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
When setting value to 99 the value is 99
  Go To                 ${HOME_URL}
  input text            sv                         99
  Click Button          Aseta
  Page Should Contain   nappia painettu 99 kertaa
