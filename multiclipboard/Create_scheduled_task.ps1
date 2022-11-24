$Action = New-ScheduledTaskAction -Execute 'python.exe' -Argument 'multiclipboard.py'
$Trigger = New-ScheduledTaskTrigger -AtLogOn
$Settings = New-ScheduledTaskSettingsSet 
$Task = New-ScheduledTask -Action $Action -Trigger $Trigger -Settings $Settings
$Username = $(whoami)
$Password = Read-Host "Please enter your password." -AsSecureString
$TaskPrincipal = New-ScheduledTaskPrincipal -userId $Username -LogonType S4U
Register-ScheduledTask -TaskName 'Multiclipboard' -InputObject $Task -User $Username -Password $Password
