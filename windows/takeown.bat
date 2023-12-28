REM Change ownership and permissions of all files in folder and subfolders to current user
takeown /F %1 /R /D Y
icacls %1 /grant:r %USERNAME%:(F) /T /C
