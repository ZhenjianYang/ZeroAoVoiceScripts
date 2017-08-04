@echo off

set curp=%~dp0
set toolsp=%curp%\..\tools
set PYTHONPATH=%toolsp%\EDDecompiler\Decompiler;%toolsp%\PyLibs

set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a

set input=%curp%\tmp\scena
set output=%curp%\tmp\psp.tmp.py.%curd%

md "%output%"

py "%toolsp%\EDDecompiler\Decompiler\ZeroScenarioScript.py" "%input%"
move /y "%input%\*.py" "%output%\"
