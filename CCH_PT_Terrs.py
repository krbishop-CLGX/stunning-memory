# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:40:13 2020

@author: krbishop
"""
Start The run to line 34


import archook
archook.get_arcpy()
import arcpy
#Import County and Muni layer
arcpy.env.workspace = "C:\_SpyderFrontier\CCH_PT_Terrs"
arcpy.env.overwriteOutput = True 
arcpy.MakeFeatureLayer_management("C:\_SpyderFrontier\CCH_PT_Terrs\County_2021_07.shp", "County_2021_07_Layer")
arcpy.MakeFeatureLayer_management("C:\_SpyderFrontier\CCH_PT_Terrs\Municipal_2021_07.shp", "Municipal_2021_07_Layer")
arcpy.Union_analysis (["Municipal_2021_07_Layer", "County_2021_07_Layer"], "Muni_County_Union.shp")

arcpy.MakeFeatureLayer_management("Muni_County_Union.shp","Muni_County_Union_Layer",'''"CITY_NAME" ='' ''')
arcpy.CopyFeatures_management("Muni_County_Union_Layer", "c:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union_Layer")
#arcpy.MakeFeatureLayer_management("C:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union_Layer.shp", "Muni_County_Union_Layer2")
#Run manual topology here. When sliver free, continue!
#Manually delete the records in the muni_county_union_layer that have"CITY_NAME" =''
# arcpy.SelectLayerByAttribute_management("cities_lyr", "SUBSET_SELECTION", "POPULATION > 10000")
arcpy.CalculateField_management("C:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union_Layer.shp", "FIPSSTCO", '!FIPSSTCO_1! ', "PYTHON")
arcpy.CalculateField_management("C:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union_Layer.shp", "STATE", '!STATE_1! ', "PYTHON")
arcpy.CalculateField_management("C:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union_Layer.shp", "COUNTY", '!COUNTY_1! ', "PYTHON")
arcpy.CalculateField_management("C:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union_Layer.shp", "ST_PL_FIPS", '!ST_PL_FI_1! ', "PYTHON")
arcpy.CalculateField_management("C:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union_Layer.shp", "PL_FIPS", '!PL_FIPS_1! ', "PYTHON")
arcpy.CalculateField_management("C:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union_Layer.shp", "CLASS_CODE", '!CLASS_CO_1! ', "PYTHON")
arcpy.CalculateField_management("C:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union_Layer.shp", "INC_FLAG", '!INC_FLAG_1! ', "PYTHON")
arcpy.CalculateField_management("C:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union_Layer.shp", "DT_ANX", '!DT_ANX_1! ', "PYTHON")
arcpy.CalculateField_management("C:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union_Layer.shp", "DT_UPD", '!DT_UPD_1! ', "PYTHON")
arcpy.CalculateField_management("C:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union_Layer.shp", "DT_VRF", '!DT_VRF_1! ', "PYTHON")
arcpy.CalculateField_management("C:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union_Layer.shp", "GNIS_CODE", '!CO_GNIS! ', "PYTHON")

Next STEP *****MANUAL****
#arcpy.MakeFeatureLayer_management("Muni_County_Union.shp","Muni_County_Union_remove",'''"CITY_NAME" ='' ''')
#arcpy.DeleteFeatures_management("Muni_County_Union_remove")
#arcpy.DeleteFeatures_management('Muni_County_Union_LayerDELETE')
#arcpy.Merge_management(["Muni_County_Union.shp","Muni_County_Union_Layer.shp"], "C:\_SpyderFrontier\CCH_PT_Terrs\SalesUseTax_wrk_2021_07")
arcpy.CopyFeatures_management("C:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union_Layer.shp", "Countywcityatt")


arcpy.MakeFeatureLayer_management("Muni_County_Union.shp","Muni_County_Union_Layer2",'''"CITY_NAME" ='' ''')
arcpy.DeleteFeatures_management("Muni_County_Union_Layer2")

arcpy.CopyFeatures_management("C:\_SpyderFrontier\CCH_PT_Terrs\Muni_County_Union.shp", "cityatt")


arcpy.Merge_management(["cityatt.shp","Countywcityatt.shp"], "C:\_SpyderFrontier\CCH_PT_Terrs\Merge")# 1arcpy.SelectLayerByAttribute_management("Muni_County_Union", "NEW_SELECTION", "[CITY_NAME] = ''")

arcpy.MakeFeatureLayer_management("C:\_SpyderFrontier\CCH_PT_Terrs\Merge.shp", "SalesUseTax_wrk_2021_07")#arcpy.MakeFeatureLayer_management("Muni_County_Union.shp","Muni_County_Union_LayerDELETE",'''"CITY_NAME" ='' ''')

Run from here:
    
    
arcpy.AddField_management("C:\_SpyderFrontier\CCH_PT_Terrs\SpecialTaxDistrict_2021_07.shp", "STD_ID_Len", "TEXT", 71, "", "", "", "NULLABLE")
arcpy.CalculateField_management("C:\_SpyderFrontier\CCH_PT_Terrs\SpecialTaxDistrict_2021_07.shp", "STD_ID_Len", '!STD_ID!', "PYTHON")
arcpy.AddField_management("C:\_SpyderFrontier\CCH_PT_Terrs\SalesUseTax_wrk_2021_07.shp", "FIPSSTCOPL", "TEXT", 10, "", "", "", "NULLABLE")
arcpy.CalculateField_management("C:\_SpyderFrontier\CCH_PT_Terrs\SalesUseTax_wrk_2021_07.shp", "FIPSSTCOPL", '!FIPSSTCO! + !PL_FIPS!', "PYTHON")
arcpy.Union_analysis (["SpecialTaxDistrict_2021_07.shp", "SalesUseTax_wrk_2021_07.shp"], "UniSpTDSales")
arcpy.FeatureToPolygon_management(["UniSpTDSales.shp"],"C:\_SpyderFrontier\CCH_PT_Terrs\UniFeatPoly","", "NO_ATTRIBUTES", "")


arcpy.DeleteField_management("UniFeatPoly.shp", ["FID_UniSpT", "OBJECTID", "STD_WHOLE", "STD_ID", "STD_NAME", "STATE", "STATECODE", "STD_TYPE", "COUNTY", "CITY_NAME", "ASSOC_CITY", "SALESTAX", "TELCOTAX", "CABLETAX", "UTILITYTX", "LEASING", "EFFECTV_D", "FIPSSTCO", "CO_GNIS", "ST_PL_FIPS", "PL_GNIS", "NOTES", "Source", "Shape_Leng", "Shape_Area", "STD_ID_Len", "FID_SalesU", "FID_Munici", "OBJECTID_1", "FIPSSTCO_1", "STATE_1", "COUNTY_1", "CITY_NAM1", "CITY_TYPE", "ST_PL_FI_1", "PL_FIPS", "CLASS_CODE", "INC_FLAG", "DT_ANX", "DT_UPD", "DT_VRF", "GNIS_CODE", "CHANGE", "FIPSSTCOPL", "ST_PL_FI_1" "EFFECTV_D", "CITY_NAM_1", "ratio", "FID_County", "OBJECTID_2", "FIPSSTCO_2", "STATE_12", "COUNTY_12", "CITY_NAM_2", "CITY_TYP_1", "ST_PL_FI_2", "PL_FIPS_1", "CLASS_CO_1", "INC_FLAG_1", "DT_ANX_1", "DT_UPD_1", "DT_VRF_1", "CO_GNIS_1", "PARCEL_ALN"])

arcpy.FeatureToPoint_management("UniFeatPoly.shp", "C:\_SpyderFrontier\CCH_PT_Terrs\UniFeatPnt", "INSIDE")
arcpy.MultipartToSinglepart_management("UniSpTDSales.shp","C:\_SpyderFrontier\CCH_PT_Terrs\UniMultSing")
arcpy.DeleteField_management("UniMultSing.shp", ["STD_WHOLE", "FID_Specia", "EFFECTV_D", "CITY_NAM_1", "STD_ID", "STD_NAME", "STATE", "STATECODE", "STD_TYPE", "COUNTY", "CITY_NAME", "ASSOC_CITY", "SALESTAX", "TELCOTAX", "CABLETAX", "UTILITYTX", "LEASING", "EFFECTIV_D", "FIPSSTCO", "CO_GNIS", "ST_PL_FIPS", "PL_GNIS", "NOTES","Source", "Shape_Leng", "Shape_Area", "FID_SalesU", "FID_Munici", "OBJECTID_1", "FIPSSTCO_1", "STATE_1", "COUNTY_1", "CITY_NAM1", "CITY_TYPE", "ST_PL_FI_1", "PL_FIPS", "CLASS_CODE", "INC_FLAG", "DT_ANX", "DT_UPD", "DT_VRF", "GNIS_CODE","CHANGE","ratio", "FID_County", "OBJECTID_2", "FIPSSTCO_2", "STATE_12", "COUNTY_12", "CITY_NAM_2", "CITY_TYP_1", "ST_PL_FI_2", "PL_FIPS_1", "CLASS_CO_1", "INC_FLAG_1", "DT_ANX_1", "DT_UPD_1", "DT_VRF_1", "CO_GNIS_1", "PARCEL_ALN", "ORIG_FID"])

target_features = "C:\_SpyderFrontier\CCH_PT_Terrs\UniMultSing.shp"
join_features = "C:\_SpyderFrontier\CCH_PT_Terrs\UniFeatPnt.shp"
out_feature_class = "C:\_SpyderFrontier\CCH_PT_Terrs\CCH_Poly_Terrs"

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)


arcpy.AddField_management("C:\_SpyderFrontier\CCH_PT_Terrs\CCH_Poly_Terrs.shp", "STD_1", "TEXT", 50, "", "", "", "NULLABLE")
arcpy.AddField_management("C:\_SpyderFrontier\CCH_PT_Terrs\CCH_Poly_Terrs.shp", "STD_2", "TEXT", 50, "", "", "", "NULLABLE")
arcpy.AddField_management("C:\_SpyderFrontier\CCH_PT_Terrs\CCH_Poly_Terrs.shp", "STD_3", "TEXT", 50, "", "", "", "NULLABLE")
arcpy.AddField_management("C:\_SpyderFrontier\CCH_PT_Terrs\CCH_Poly_Terrs.shp", "STD_4", "TEXT", 50, "", "", "", "NULLABLE")
arcpy.AddField_management("C:\_SpyderFrontier\CCH_PT_Terrs\CCH_Poly_Terrs.shp", "STD_5", "TEXT", 50, "", "", "", "NULLABLE")
arcpy.AddField_management("C:\_SpyderFrontier\CCH_PT_Terrs\CCH_Poly_Terrs.shp", "Concat", "TEXT", 200, "", "", "", "NULLABLE")
arcpy.DeleteField_management("UniFeatPoly.shp", ["FID_UniSpT", "OBJECTID", "STD_WHOLE", "STD_ID", "STD_NAME", "STATE", "STATECODE", "STD_TYPE", "COUNTY", "CITY_NAME", "ASSOC_CITY", "SALESTAX", "TELCOTAX", "CABLETAX", "UTILITYTX", "LEASING", "EFFECTV_D", "FIPSSTCO", "CO_GNIS", "ST_PL_FIPS", "PL_GNIS", "NOTES", "Source", "Shape_Leng", "Shape_Area", "STD_ID_Len", "FID_SalesU", "FID_Munici", "OBJECTID_1", "FIPSSTCO_1", "STATE_1", "COUNTY_1", "CITY_NAM1", "CITY_TYPE", "ST_PL_FI_1", "PL_FIPS", "CLASS_CODE", "INC_FLAG", "DT_ANX", "DT_UPD", "DT_VRF", "GNIS_CODE", "CHANGE", "FIPSSTCOPL", "ST_PL_FI_1" "EFFECTV_D", "CITY_NAM_1", "ratio", "FID_County", "OBJECTID_2", "FIPSSTCO_2", "STATE_12", "COUNTY_12", "CITY_NAM_2", "CITY_TYP_1", "ST_PL_FI_2", "PL_FIPS_1", "CLASS_CO_1", "INC_FLAG_1", "DT_ANX_1", "DT_UPD_1", "DT_VRF_1", "CO_GNIS_1", "PARCEL_ALN"])

ADD to ARC and 
Run ConCat rows:
#Input: CCH_Poly_terrs.shp
#.Case Field: ORIG_FID
#.Read From Field: STD_ID_Len
#.Copy to Field: Concat
#.Delimiter: ,


