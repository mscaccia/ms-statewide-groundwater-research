import arcpy
import arcpy.sa as sa

#path to arc workspace
arcpy.env.workspace = r"C:\Users\10216172\OneDrive - State of Ohio\Desktop\MS_UC\WilliamsCoWells\WellsWilliamsCo.gdb"
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")

#input data
dem_raster = r"D:\DEM.gdb\DEM_Statewide"
well_points = r"C:\Users\10216172\OneDrive - State of Ohio\Desktop\MS_UC\WilliamsCoWells\WellsWilliamsCo.gdb\WellLogs_Williams"

# Temporary output in memory
temp_output = "in_memory\\temp_points"

# Extract DEM values to temporary points
sa.ExtractValuesToPoints(
    in_point_features=well_points,
    in_raster=dem_raster,
    out_point_features=temp_output,
    interpolate_values="NONE",
    add_attributes="VALUE_ONLY"
)


# Join the DEM values back to the original input points
arcpy.management.JoinField(
    in_data=well_points,
    in_field="WELL_LOG_NO",  # or another unique ID field
    join_table=temp_output,
    join_field="WELL_LOG_NO",
    fields=["RASTERVALU"]  # This is the default field name for DEM values
)
