Xpath functions

1)FUll visible text - text(),-- //a[text()="Make Appointment"]
2)Partial visible Text - 1)Contains():- used to generate xpath with partial text ie.  //a[contains(text(),"Make")]

,starts-with(),ends-with()

#Normalize space used for a name that contain white space
xpath using normalize space testa login button - //button[normalize-space(text())='Login']
