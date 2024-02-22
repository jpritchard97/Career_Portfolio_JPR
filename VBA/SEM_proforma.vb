Sub InsertImagesWithCaptionsAndResize()
    Dim dialog As FileDialog
    Dim fileName As Variant
    Dim caption As String
    Dim pic As InlineShape
    Dim rng As Range
    Dim imagesPerPage As Integer
    Dim currentImageCount As Integer
    Dim pageWidth As Single
    Dim pageHeight As Single
    Dim desiredWidth As Single
    Dim desiredHeight As Single
    Dim leftMargin As Single
    Dim topMargin As Single
    Dim imageSpacing As Single
    Dim rowCount As Integer
    Dim colCount As Integer
    Dim i As Integer
    Dim currentLeft As Single
    Dim currentTop As Single
    Dim imgBox As Shape
    Dim captionBox As Shape

    ' Define how many images to insert per page
    imagesPerPage = 4
    currentImageCount = 0

    ' Set the desired width and height for the images (in points)
    desiredWidth = CentimetersToPoints(9.68)
    desiredHeight = CentimetersToPoints(6.96)

    ' Get page dimensions and margins for a landscape page
    pageWidth = ActiveDocument.PageSetup.pageWidth
    pageHeight = ActiveDocument.PageSetup.pageHeight
    leftMargin = ActiveDocument.PageSetup.leftMargin
    topMargin = ActiveDocument.PageSetup.topMargin

    ' Calculate the horizontal and vertical spacing between images
    rowCount = 2 ' Two rows
    colCount = 2 ' Two columns
    imageSpacing = (pageWidth - (2 * leftMargin) - (colCount * desiredWidth)) / (colCount - 1)
    Dim verticalSpacing As Single
    verticalSpacing = (pageHeight - (2 * topMargin) - (rowCount * desiredHeight)) / (rowCount - 1)

    ' Create a file dialog to select images
    Set dialog = Application.FileDialog(msoFileDialogFilePicker)

    ' Allow multiple file selection
    dialog.AllowMultiSelect = True

    ' Show the dialog and exit if canceled
    If dialog.Show <> -1 Then Exit Sub

    ' Set the initial range to the beginning of the document
    Set rng = ActiveDocument.Range(Start:=ActiveDocument.Content.Start, End:=ActiveDocument.Content.Start)

    ' Loop through selected files
    For Each fileName In dialog.SelectedItems
        ' Get the file name without path
        caption = Mid(fileName, InStrRev(fileName, "\") + 1)

        ' Insert the image
        Set pic = ActiveDocument.InlineShapes.AddPicture( _
            fileName:=CStr(fileName), _
            LinkToFile:=False, _
            SaveWithDocument:=True, _
            Range:=rng)

        ' Resize the image to match the desired size
        pic.Width = desiredWidth
        pic.Height = desiredHeight

        ' Calculate the current row and column for the image
        Dim currentRow As Integer
        Dim currentCol As Integer
        currentRow = currentImageCount \ colCount
        currentCol = currentImageCount Mod colCount

        ' Calculate the position for the image
        currentLeft = leftMargin + (currentCol * (desiredWidth + imageSpacing))
        currentTop = topMargin + (currentRow * (desiredHeight + verticalSpacing))

        ' Create a text box for the image
        Set imgBox = ActiveDocument.Shapes.AddTextbox( _
            Orientation:=msoTextOrientationHorizontal, _
            Left:=currentLeft, _
            Top:=currentTop, _
            Width:=desiredWidth, _
            Height:=desiredHeight)

        ' Set text wrapping for the image text box to "In front of text"
        imgBox.TextFrame.TextRange.ParagraphFormat.Alignment = wdAlignParagraphCenter
        imgBox.WrapFormat.Type = wdWrapFront

        ' Remove fill and line color for the image text box
        imgBox.Fill.Visible = msoFalse
        imgBox.Line.Visible = msoFalse

 

        ' Insert the image inside the text box
        pic.Range.Cut
        imgBox.TextFrame.TextRange.Paste

        ' Create a text box for the caption below the image
        Set captionBox = ActiveDocument.Shapes.AddTextbox( _
            Orientation:=msoTextOrientationHorizontal, _
            Left:=currentLeft, _
            Top:=currentTop + desiredHeight, _
            Width:=desiredWidth, _
            Height:=desiredHeight / 4) ' Adjust the height for the caption

        ' Set text wrapping for the caption text box to "In front of text"
        captionBox.TextFrame.TextRange.ParagraphFormat.Alignment = wdAlignParagraphCenter
        captionBox.WrapFormat.Type = wdWrapFront

        ' Remove fill and line color for the caption text box
        captionBox.Fill.Visible = msoFalse
        captionBox.Line.Visible = msoFalse

        ' Insert the caption inside the caption text box
        captionBox.TextFrame.TextRange.Text = caption

        ' Increment the current image count
        currentImageCount = currentImageCount + 1

        ' Check if it's time to insert a page break
        If currentImageCount >= imagesPerPage Then
            ' Insert a page break
            rng.Collapse Direction:=wdCollapseEnd
            rng.InsertBreak Type:=wdPageBreak
            ' Reset the current image count
            currentImageCount = 0
            ' Move the range to the beginning of the next page
            Set rng = ActiveDocument.Range(Start:=rng.End, End:=rng.End)
        End If
    Next fileName
End Sub

Function CentimetersToPoints(ByVal centimeters As Single) As Single
    ' Converts centimeters to points (1 cm = 28.35 points)
    CentimetersToPoints = centimeters * 28.35
End Function
