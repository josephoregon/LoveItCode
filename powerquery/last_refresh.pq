let

Source = #table(type table[Date Last Refreshed=datetime], {{DateTime.LocalNow()}}),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"Date Last Refreshed", "Last Refresh"}})

in

#"Renamed Columns"
