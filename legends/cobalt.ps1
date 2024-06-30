$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("C:\Users\warlocksmurf\legends.lnk")
$Shortcut.TargetPath = "powershell.exe"
$Shortcut.Arguments = "-window hidden -noni -enc JGJ5dGVzPVtTeXN0ZW0uSU8uRmlsZV06OlJlYWRBbGxCeXRlcygnQzpcVXNlcnNcd2FybG9ja3NtdXJmXGZsYWcuanBnJyk7Zm9yKCRpPTA7JGkgLWx0ICRieXRlcy5MZW5ndGg7JGkrKyl7JGJ5dGVzWyRpXT0kYnl0ZXNbJGldLWJ4b3IgMzV9O1tTeXN0ZW0uSU8uRmlsZV06OldyaXRlQWxsQnl0ZXMoJ0M6XFVzZXJzXHdhcmxvY2tzbXVyZlx6ZWxkYS5qcGcnLCRieXRlcyk="

$Shortcut.Save()
