#!/bin/pwsh

# spmather
# 2026-07-27
# v1.0.0


function Show-ProgressSpinner {
<#


    Function will not clear correctly when there is a new line immediately preceding the spinner i.e.: "`r`n $(Show-ProgressSpinner -SpinCount 10)"


   .EXAMPLE 
    Run a single rotation in the default color, which is gray for both light and dark mode compatibility.
    Show-ProgressSpinner
    
   .EXAMPLE 
    Run 1000 rotations in cyan.
    Show-ProgressSpinner -SpinCount 1000 -Color Cyan

   .EXAMPLE
    Use at the end of a ForEach loop on Linux:
    (1..255) | ForEach-Object {. /bin/ping -c 2 -t 10 192.168.0.$_; Write-Output "Working on a ping to 192.168.0.$($_) $(Show-ProgressSpinner -SpinCount 10)"}

    Use at the end of a ForEach loop in Windows:
    (1..255) | ForEach-Object {Test-NetConnection -ComputerName 192.168.0.$_ -ErrorAction SilentlyContinue ; Write-Output "Working on a ping to 192.168.0.$($_) $(Show-ProgressSpinner)"}
    
#>

    
    param(
        [Parameter(
            Mandatory = $False
        )]
        [int32] $SpinCount = 1,

        [Parameter(
            Mandatory = $False
        )]
        [ValidateSet(
            "Black","DarkBlue","DarkGreen","DarkCyan","DarkRed","DarkMagenta",
            "DarkYellow","Gray","DarkGray","Blue","Green","Cyan","Red","Magenta",
            "Yellow","White"
        )]
        [string] $Color = "Gray",

        [Parameter(
            Mandatory = $False
        )]
        [int32] $SpinWaitInMilliseconds = 50
    )

    $EmptyStr = ""
    
    $SpinList = @(
        '|',
        '/',
        '-',
        '\'
    )

    For ($i = 1 ; $i -le $SpinCount ; $i++) {
        ForEach ($Spin in $Spinlist) {
            Write-Host -Object "`r$($Spin)" -ForegroundColor $Color -NoNewline
            Start-Sleep -Milliseconds $SpinWaitInMilliseconds
        }
        Write-Host -Object "`r$EmptyStr" -ForegroundColor $Color -NoNewline
    }
}

Write-Output "Function Show-ProgressSpinner was imported successfully" | Write-Host -ForegroundColor Cyan

# fin
