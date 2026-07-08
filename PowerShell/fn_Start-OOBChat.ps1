#!/bin/pwsh

# SPMATHER
# Created 2025-05-15
# Upated 2026-07-07
# Version 2.0.0
#  Added gnome-terminal (Zorin, Ubuntu, other gnome based distros) compatibility

# Use case:  if a chat is down and you need to share information

# ################################################
#                                       Formatter
# ################################################

function Format-OOBChat {
    param(
        [Parameter(
            ValueFromPipeline = $True
        )]
        [string]$InputText
    )

    begin {

        if ($PSVersionTable.Platform -eq "UNIX") {
            $WhoAmI   = /bin/whoami
            $Computer = /bin/hostname
        } 
        elseif ($PSVersionTable.Platform -ne "UNIX") {
            $Whoami   = whoami.exe
            $Computer = hostname.exe
        }

        $Date     = Get-Date -Format "yyyy-MM-dd @ HH:mm:ss"
    }

    process {
        $FormattedText = [string]$Whoami + " " + "on" + " " + [string]$Computer + " " + "at" + " " + $Date + " " + "says" + "`n" + "$InputText" + "`n"
        $FormattedText
    }

    end {
        Write-Debug "Format-OOBChat fn has formatted text [$($FormattedText)]"
    }
}

# ################################################
#                                            Open
# ################################################


function Open-OOBChat {
    param(
        [Parameter(
            Position  = 0,
            Mandatory = $True
        )]
        [string]$Path
    )

    begin {
        If (!(Test-Path -Path $Path)) {
            New-Item -Path $Path -ItemType File
        }
    }

    process {
        if ($PSVersionTable.Platform -eq "UNIX") {
            # gnome only for now.  options for tmux in progress
            /bin/gnome-terminal -- /bin/pwsh -NoExit -CommandWithArgs "Get-Content -Wait -Path $Path"
        }
        elseif ($PSVersionTable.Platform -ne "UNIX") {
            Start-Process -FilePath Powershell.exe -ArgumentList "-noexit","Get-Content -Wait -Path $Path"
        }
    }

    end {
        Write-Debug "Chat window fn ended"
    }
}

# ################################################
#                                  Start Chatting
# ################################################


function Start-OOBChat {
    param(
        [Parameter(
            Position  = 0,
            Mandatory = $True,
            HelpMessage = "Input the text file path where both people have read and write:  "
        )]
        [string]$Path
    )

    begin {
        Write-Output "Setting up chat local files ... please wait"
        $Parent = $PSScriptRoot

        If (!(Test-Path -Path "$Parent\Chats")) {
            New-Item -Path $Parent -Name Chats -ItemType Directory
        }

        $LocalChatFolder = "$Parent\Chats"

        Write-Output "Setting up remote files ... please wait"
        if ($PSVersionTable.Platform -ne "UNIX") {
            $host.UI.RawUI.WindowTile = "Chatting"
        }
        Clear-Host
    }

    process {
        Open-OOBChat -Path $Path
        $WhileCheck = $True
        Clear-Host

        While ($WhileCheck) {
            Write-Output "Type Exit to exit the program"
            $Message = Read-Host "Type a message "

            If ($Message -eq "Exit") {
                Break
            }

            try {
                Format-OOBChat -InputText $Message | Out-File $Path -append
                Clear-Host
            } 
            catch {
                Write-Error "Message really couldn't be sent"
            }
        }
    }

    end {
        Copy-Item -Path $Path -Destination $LocalChatFolder
        function prompt {"$(Get-Location)> "}
        if ($PSVersionTable.Platform -ne "UNIX") {
            $host.UI.RawUI.WindowTitle = $Null
        }
        Write-Debug "Exiting cleanly"
    }
}

Write-Output "To run, use Start-OOBChat -Path <file where both people have read/write permissions" | Write-Host -ForegroundColor Cyan

# fin
