/*

Author: Joseph Rosas, Data Scientist
Date: June 21st, 2020
Purpose: Display refresh date for data source in Microsoft Power BI

*/

let

Source = #table(type table[Date Last Refreshed=datetime], {{DateTime.LocalNow()}}),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"Date Last Refreshed", "Last Refresh"}})

in

#"Renamed Columns"
