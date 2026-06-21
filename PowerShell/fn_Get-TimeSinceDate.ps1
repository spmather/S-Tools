#!/bin/pwsh

# SPMATHER
# 2025-12-16 
# v1.0.2 2026-06-21
# Starts a timer

# Example:  Get-TimeSinceDate -date "2025-12-21 15:03:00Z"          # Winter Solstice 2025
# Example:  Get-TimeSinceDate -date "2025-12-21 15:03:00Z" -Repeat  # Winter Solstice 2025


function Format-TimeSinceDate {  # Private
    param (
        [Parameter(
            Mandatory         = $True,
            ValueFromPipeline = $True
        )]
        [String]$Date
    )

    $DateTimeRegex = '\d{3}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}Z'

    If ($Date -notmatch $DateTimeRegex) {
        Write-Error "Date format failed.  Please use this format for full datetime yyyy-MM-dd HH:mm:ssZ "
        Break
    }

    $Start    = Get-Date
    $End      = (Get-Date -Date $Date).ToUniversalTime()
    $TimeSpan = New-TimeSpan -Start $Start -End $End
    $TSD      = $TimeSpan.Days
    $TSH      = $TimeSpan.Hours
    $TSM      = $TimeSpan.Minutes
    $TSS      = $TimeSpan.Seconds

    $Formated = "{0} Days, {1} Hours, {2} Minutes, {3} Seconds" -f $TSD,$TSH,$TSM,$TSS
    Return $Formated
}


function Get-TimeSinceDate {  # Public
    param(
        [Parameter(
            Mandatory         = $True,
            ValueFromPipeline = $True
        )]
        [String]$Date,

        [Parameter(
            Mandatory = $False
        )]
        [Switch]$Repeat
    )

    If ($Repeat) {
        Write-Output 'Use [ctrl] + [c] to quit' | Write-Host -ForegroundColor "Cyan"
        While ($True) {
            Format-TimeSinceDate -Date $Date
            Start-Sleep -Seconds 1
        }
    }
    ElseIf (!($Repeat)) {
        Start-TimerActual -Date $Date
    }
}



# fin
