Sub copy2()

Sheets("result").Activate
Dim lastrowdata, lastrowresults, datarow, resultrow, found As Integer

'Clear results sheet and replace it with the template
Sheets("result").Cells.Clear
Sheets("template").Range("A1:F29").Copy Destination:=Sheets("result").Range("A1")

'find length of sheets for iterations
lastrowdata = Sheets("data").Cells(Rows.Count, 1).End(xlUp).Row
lastrowresults = Sheets("result").Cells(Rows.Count, 1).End(xlUp).Row


MsgBox "Updating"
'MsgBox lastrowdata
'MsgBox lastrowresults

'Replace empty product with "-" so empty cells dont match each other
For productrow = 1 To lastrowdata
    If IsEmpty(Sheets("data").Cells(productrow, 3).Value) Then
        Sheets("data").Cells(productrow, 3).Value = "-"
    End If
    Next productrow

'Iterate over results and data. Load portfolios into appropriate regions.
For resultrow = 1 To 200
    For datarow = 1 To lastrowdata
        If Sheets("data").Cells(datarow, 3).Value = Cells(resultrow, 1).Value Then
            Sheets("result").Rows(resultrow).Insert shift:=xlShiftDown
            Sheets("data").Rows(datarow).Copy Sheets("result").Rows(resultrow)
            resultrow = resultrow + 1
        'Load region values
        ElseIf Sheets("data").Cells(datarow, 1).Value = Cells(resultrow, 1).Value Then
            Sheets("data").Cells(datarow, 6).Copy Sheets("result").Cells(resultrow, 6)
            
        End If
    Next datarow
    
Next resultrow

End Sub