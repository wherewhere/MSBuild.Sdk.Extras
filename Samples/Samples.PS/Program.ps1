$version = [System.Environment]::Version;
Write-Host $version;
$version = [System.Runtime.InteropServices.RuntimeInformation]::FrameworkDescription;
Write-Host $version;
Read-Host "Press any key to exit...";
