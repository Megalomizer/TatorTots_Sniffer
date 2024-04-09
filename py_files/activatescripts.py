from flask import Flask, render_template, redirect
import run as mainpy

def changeSnifferActivity():
    mainpy.snifferActivityTracker
    mainpy.spooferActivityTracker

    if mainpy.snifferActivityTracker=="Active":
        mainpy.snifferActivityTracker="Inactive"
    else:
        mainpy.snifferActivityTracker="Active"

    return mainpy.index(spooferbtntext=mainpy.spooferActivityTracker, snifferbtntext=mainpy.snifferActivityTracker)

def changeSpooferActivity():
    mainpy.snifferActivityTracker
    mainpy.spooferActivityTracker

    if mainpy.spooferActivityTracker=="Active":
        mainpy.spooferActivityTracker="Inactive"
    else:
        mainpy.spooferActivityTracker="Active"
    
    return mainpy.index(spooferbtntext=mainpy.spooferActivityTracker, snifferbtntext=mainpy.snifferActivityTracker)
