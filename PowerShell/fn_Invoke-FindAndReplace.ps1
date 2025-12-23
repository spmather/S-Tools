#!/bin/pwsh
# Author : spmather
# Date   : 2025-11-13
# Version: 0.1
#                                                                                                    Column 120 is here`

function Invoke-FindandReplace {
<#
.SYNOPSIS

Uses find and replace function to speedily redact sensitive data.


.DESCRIPTION

This function is intended to be a single find and replace function with the use of
regex or strings to find and replace sensitive data.  For example, with use in an
environment where you need to redact IP addresses from a log.


.EXAMPLE

Find unique string
Invoke-FindandReplace -FilePath ./Simulated_Senstive_Documents/Simulated_Sensitive_Log.txt -Find 'Secret' -Unique

Find and replace
$FilePath = "./Simulated_Senstive_Documents/Simulated_Sensitive_Log.txt"
Invoke-FindandReplace $FilePath -Find 'Secret' -Replace 'Redacted'

Bulk find and replace (note:  For substutution cypher, please use Format-ScrambledEggs)
$CSV = Import-Csv ./example.csv
ForEach ($Line in $CSV) {Invoke-FindandReplace $FilePath -Find $CSV.Find -Replace $CSV.Replace}



#>

    [CmdletBinding()]
    param(
        [Alias("Path")]
        [parameter(
            Mandatory                       = $true,
            ValueFromPipeLineByPropertyName = $true,
            Position                        = 0
        )]
        [string]$FilePath,
        
        [parameter(
            Mandatory                       = $true,
            ValueFromPipeLineByPropertyName = $false,
            Position                        = 1
        )]
        [string]$Find,
        
        [parameter(
            Mandatory                       = $false,
            ValueFromPipeLineByPropertyName = $false,
            Position                        = 2
        )]
        [string]$Replace,

        [parameter(
            Mandatory                       = $false
        )]
        [switch]$Unique
    )
        

    Begin {

        # Start timer
        $Start = Get-Date

        # Windows or Linux
        If ($env:OS -eq "Windows_NT") {
            Write-Debug "OS is Windows"
        }
        Else {
            Write-Debug "OS is non-Windows"
        }

        Try {
            Test-Path $FilePath
        }
        Catch {
            Write-Error "Failed to find"
        }

        $SplitValue = @(
            '"',
            "'",
            ' ',
            '\',
            '/',
            '-',
            '_',
            '=',
            '+',
            '^',
            '>',
            '<'
        )
    }


    Process {

        #  This looks weird, but Select-String does not output string objects when using -Pattern parameter.  
        #  Casting [string] will not work either.

        Get-Content -Path $FilePath | Select-String -Pattern $Find | Out-File Temp:/outfile1.txt
        ForEach ($String in (Get-Content Temp:/outfile1.txt)) {
            $String.Split($SplitValue) | Out-File Temp:/outfile2.txt -Append

            If ($Unique) {
                $UniqueList = Get-Content Temp:/outfile2.txt | Select-String -Pattern $Find | Sort-Object | `
                    Select-Object -Unique
            }
            ElseIf (!($Unique)) {
                $UniqueList = Get-Content Temp:/outfile2.txt | Select-String -Pattern $Find
            }

        }
   
        If ($Replace) {
            (Get-Content -Path $FilePath).Replace($Find,$Replace) | Set-Content $FilePath
        }
    }

    End {
        $Stop = Get-Date
        $CompletedInSeconds = ($Stop).Subtract($Start)

        Write-Output "Function completed in [$CompletedInSeconds]"
    }
}

Write-Host "Function loaded.  Please use Get-Help Invoke-FindandReplace for help." -ForegroundColor Cyan

#fin