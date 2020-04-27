# Python Finalized Field Calculator
# Grant Haynes
# December 2019
# Purpose to iterate over all the low flow data
# and populate the finalized readings

import arcpy

table = arcpy.GetParameterAsText(0)

cursor = arcpy.UpdateCursor(table)
for row in cursor:
    timeCounter = 5
    while timeCounter < 60:
        lookAheadTime = timeCounter + 5
       
        if row.getValue("PH_{}_min".format(str(timeCounter))) is not None and row.getValue("PH_{}_min".format(str(lookAheadTime))) is None:
            row.setValue("Stop_PH", row.getValue("PH_{}_min".format(str(timeCounter))))

        if row.getValue("temp_{}_min".format(str(timeCounter))) is not None and row.getValue("Temp_{}_min".format(str(lookAheadTime))) is None:
             row.setValue("Stop_Temp", row.getValue("Temp_{}_min".format(str(timeCounter))))

        if row.getValue("SPC_{}_min".format(str(timeCounter))) is not None and row.getValue("SPC_{}_min".format(str(lookAheadTime))) is None:
            row.setValue("Stop_SPC", row.getValue("SPC_{}_min".format(str(timeCounter))))

        if row.getValue("DO_{}_min".format(str(timeCounter))) is not None and row.getValue("DO_{}_min".format(str(lookAheadTime))) is None:
            row.setValue("Stop_DO", row.getValue("DO_{}_min".format(str(timeCounter))))

        if row.getValue("ORP_{}_min".format(str(timeCounter))) is not None and row.getValue("ORP_{}_min".format(str(lookAheadTime))) is None:
            row.setValue("Stop_ORP", row.getValue("ORP_{}_min".format(str(timeCounter))))

        if row.getValue("Turbidity_{}_min".format(str(timeCounter))) is not None and row.getValue("Turbidity_{}_min".format(str(lookAheadTime))) is None:
            row.setValue("Stop_Turbidity", row.getValue("Turbidity_{}_min".format(str(timeCounter))))
        timeCounter = timeCounter + 5
    cursor.updateRow(row)     