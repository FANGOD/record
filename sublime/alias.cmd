@echo off

:: Temporary system path at cmd startup

set PATH=%PATH%;"D:\Sublime Text3"

:: Add to path by command


:: Commands

DOSKEY ll=dir /B

DOSKEY subl=subl $*

DOSKEY sublime=sublime_text $*  
