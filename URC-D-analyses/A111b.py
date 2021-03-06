# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# A111b.py
# Created on: 2021-09-29 19:23:20.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: A111b <Distance__value_or_field_> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Distance__value_or_field_ = arcpy.GetParameterAsText(0)
if Distance__value_or_field_ == '#' or not Distance__value_or_field_:
    Distance__value_or_field_ = "25 Meters" # provide a default value if unspecified

# Local variables:
dambovita_lines = "A.1.1.1b\\dambovita_lines"
OSM_roads_dambovita = "A.1.1.1b\\OSM_roads_dambovita"
OSM_roads_Buffer = "C:\\Users\\danie\\Documents\\ArcGIS\\Default.gdb\\OSM_roads_Buffer"
OSM_roads_Intersect1 = "C:\\Users\\danie\\Documents\\ArcGIS\\Default.gdb\\OSM_roads_Intersect1"
dambovita_lines_roads_shp = "E:\\00_Cloud\\Surfdrive\\Shared\\URC-Daniele\\01_indicators\\A.1.1.1a\\input\\construction\\dambovita_lines_roads.shp"
Modified_Input_Features = dambovita_lines_roads_shp
dambovita_lines_roads_shp__2_ = Modified_Input_Features
dambovita_lines_roads_shp__4_ = dambovita_lines_roads_shp__2_
dambovita_lines_roads_shp__3_ = dambovita_lines_roads_shp__4_
a111b = "E:\\00_Cloud\\Surfdrive\\Shared\\URC-Daniele\\01_indicators\\A.1.1.1a\\output\\a111b"
a111b__2_ = a111b
Expression = "\"HIGHWAY\" = 'cycleway'"
OSM_roads_Select = "C:\\Users\\danie\\Documents\\ArcGIS\\Default.gdb\\OSM_roads_Select"
OSM_roads_Select_Buffer = "C:\\Users\\danie\\Documents\\ArcGIS\\Default.gdb\\OSM_roads_Select_Buffer"
OSM_roads_Select_Buffer_Inte = "C:\\Users\\danie\\Documents\\ArcGIS\\Default.gdb\\OSM_roads_Select_Buffer_Inte"
dambovita_lines_cycle_shp = "E:\\00_Cloud\\Surfdrive\\Shared\\URC-Daniele\\01_indicators\\A.1.1.1a\\input\\construction\\dambovita_lines_cycle.shp"
Modified_Input_Features__2_ = dambovita_lines_cycle_shp
dambovita_lines_cycle_shp__2_ = Modified_Input_Features__2_
dambovita_lines_cycle_shp__4_ = dambovita_lines_cycle_shp__2_
dambovita_lines_cycle_shp__3_ = dambovita_lines_cycle_shp__4_
a111b__3_ = a111b__2_
a111b__5_ = a111b__3_
a111b__4_ = a111b__5_
a111b__6_ = a111b__4_

# Process: Buffer (2)
arcpy.Buffer_analysis(OSM_roads_dambovita, OSM_roads_Buffer, Distance__value_or_field_, "FULL", "ROUND", "NONE", "", "PLANAR")

# Process: Intersect (2)
arcpy.Intersect_analysis("A.1.1.1b\\dambovita_lines #;C:\\Users\\danie\\Documents\\ArcGIS\\Default.gdb\\OSM_roads_Buffer #", OSM_roads_Intersect1, "ALL", "", "INPUT")

# Process: Dissolve (2)
arcpy.Dissolve_management(OSM_roads_Intersect1, dambovita_lines_roads_shp, "segment", "", "MULTI_PART", "DISSOLVE_LINES")

# Process: Add Geometry Attributes
arcpy.AddGeometryAttributes_management(dambovita_lines_roads_shp, "LENGTH", "METERS", "", "")

# Process: Add Field
arcpy.AddField_management(Modified_Input_Features, "tot_lenght", "FLOAT", "8", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(dambovita_lines_roads_shp__2_, "tot_lenght", "!LENGTH!", "PYTHON_9.3", "")

# Process: Delete Field (2)
arcpy.DeleteField_management(dambovita_lines_roads_shp__4_, "LENGTH")

# Process: Copy Rows
arcpy.CopyRows_management(dambovita_lines_roads_shp__3_, a111b, "")

# Process: Select
arcpy.Select_analysis(OSM_roads_dambovita, OSM_roads_Select, Expression)

# Process: Buffer
arcpy.Buffer_analysis(OSM_roads_Select, OSM_roads_Select_Buffer, Distance__value_or_field_, "FULL", "FLAT", "NONE", "", "PLANAR")

# Process: Intersect
arcpy.Intersect_analysis("C:\\Users\\danie\\Documents\\ArcGIS\\Default.gdb\\OSM_roads_Select_Buffer #;A.1.1.1b\\dambovita_lines #", OSM_roads_Select_Buffer_Inte, "ALL", "", "INPUT")

# Process: Dissolve
arcpy.Dissolve_management(OSM_roads_Select_Buffer_Inte, dambovita_lines_cycle_shp, "segment", "", "MULTI_PART", "DISSOLVE_LINES")

# Process: Add Geometry Attributes (2)
arcpy.AddGeometryAttributes_management(dambovita_lines_cycle_shp, "LENGTH", "METERS", "", "")

# Process: Add Field (2)
arcpy.AddField_management(Modified_Input_Features__2_, "cyc_lenght", "FLOAT", "6", "2", "", "", "NON_NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (2)
arcpy.CalculateField_management(dambovita_lines_cycle_shp__2_, "cyc_lenght", "!LENGTH!", "PYTHON_9.3", "")

# Process: Delete Field
arcpy.DeleteField_management(dambovita_lines_cycle_shp__4_, "LENGTH")

# Process: Join Field
arcpy.JoinField_management(a111b, "SEGMENT", dambovita_lines_cycle_shp__3_, "segment", "cyc_lenght")

# Process: Add Field (3)
arcpy.AddField_management(a111b__2_, "value", "DOUBLE", "8", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (3)
arcpy.CalculateField_management(a111b__3_, "value", "!CYC_LENGHT!/ !TOT_LENGHT!*100", "PYTHON_9.3", "")

# Process: Add Field (4)
arcpy.AddField_management(a111b__5_, "A.1.1.1b", "SHORT", "1", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (4)
arcpy.CalculateField_management(a111b__4_, "A.1.1.1B", "ifBlock ( !VALUE!)", "PYTHON_9.3", "def ifBlock(value):\\n if value<50:\\n  return 1\\n elif value>=50 and value<75:\\n  return 2\\n elif value>3:\\n  return 3\\n")

