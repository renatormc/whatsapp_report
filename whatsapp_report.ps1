try {
    $wd = Get-Location
    Push-Location "$PSScriptRoot"
    uv run main.py -w "$wd" @args
}
finally {
    Pop-Location
}
