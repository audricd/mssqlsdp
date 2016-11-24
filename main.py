# Microsoft SQL Support Diagnostic Package v0.1
# Audric D'Hoest github.com/audricd
import sys
import subprocess


def fprocesses():
    processes = open("processes.txt", "w");
    subprocess.Popen("ps aux", stdout=processes)


def fnetsat():
    netstat = open("netstat.txt", "w");
    subprocess.Popen("netstat", stdout=netstat)


def fdf():
    df = open("df.txt", "w");
    subprocess.Popen("df", stdout=df)


def fServiceStatus():
    servicestatus = open("servicestatus.txt", "w");
    subprocess.Popen("systemctl status mssql-server -l", stdout=servicestatus)


def fIfconfig():
    ifconfig = open("ifconfig.txt", "w");
    subprocess.Popen("ifconfig", stdout=ifconfig)


def fRhrelease():
    rhrelease = open("rhrelease.txt", "w");
    subprocess.Popen("cat /etc/redhat-release", stdout=rhrelease)


def fUname():
    uname = open("uname.txt", "w");
    subprocess.Popen("uname -a", stdout=uname)


def fPackageinfo():
    packageinfo = open("packageinfo.txt", "w");
    subprocess.Popen("yum info mssql-server", stdout=packageinfo)


def fPyVer():
    pyver = open("pyver.txt", "w");
    subprocess.Popen("python -V", stdout=pyver)