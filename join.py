import arcpy

#path to arc workspace
arcpy.env.workspace = r"C:\Users\10216172\OneDrive - State of Ohio\Desktop\MS_UC\WilliamsCoWells\WellsWilliamsCo.gdb"
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")


#input data
well_points = r"C:\Users\10216172\OneDrive - State of Ohio\Desktop\MS_UC\WilliamsCoWells\WellsWilliamsCo.gdb\WellLogs_Williams"
geo_forms = r"C:\Users\10216172\OneDrive - State of Ohio\Desktop\MS_UC\WilliamsCoWells\GEO_FORM_WilliamsCo.csv"

#join the two tables based on a common field
arcpy.management.JoinField(
    in_data=well_points, 
    in_field="WELL_LOG_NO",
    join_table=geo_forms,
    join_field="WELL_LOG_NO"
)

