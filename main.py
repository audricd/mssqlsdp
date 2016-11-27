# Red Hat Microsoft SQL Support Diagnostic Package v0.1
# Audric D'Hoest github.com/audricd
import sys
import subprocess

# welcome message
l1 = "Microsoft SQL Support Diagnostic Package for Red Hat (WORK IN PROGRESS, NON OPERATIONAL YET)"
l2 = "This script will gather basic system information for helping troubleshooting MSSQL server issues"

print(l1)
print(l2)

# TO DO:
# create log folder based on current date
# launch below functions and zip the results per log date

# info to retrieve
def fprocesses():
    processes = open("processes.txt", "w");
    subprocess.Popen("ps aux", stdout=processes)
    print ("exporting process list...")


def fnetsat():
    netstat = open("netstat.txt", "w");
    subprocess.Popen("netstat", stdout=netstat)
    print ("exporting active connections...")


def fdf():
    df = open("df.txt", "w");
    subprocess.Popen("df", stdout=df)
    print ("exporting disk information...")


def fServiceStatus():
    servicestatus = open("servicestatus.txt", "w");
    subprocess.Popen("systemctl status mssql-server -l", stdout=servicestatus)
    print ("exporting MSSQL Server service status logs...")


def fIfconfig():
    ifconfig = open("ifconfig.txt", "w");
    subprocess.Popen("ifconfig", stdout=ifconfig)
    print ("exporting IP configuration...")


def fRhrelease():
    rhrelease = open("rhrelease.txt", "w");
    subprocess.Popen("cat /etc/redhat-release", stdout=rhrelease)
    print ("exporting Red Hat release info...")


def fUname():
    uname = open("uname.txt", "w");
    subprocess.Popen("uname -a", stdout=uname)
    print ("exporting kernel information...")


def fPackageinfo():
    packageinfo = open("packageinfo.txt", "w");
    subprocess.Popen("yum info mssql-server", stdout=packageinfo)
    print ("exporting MSSQL-Server package information")

def fPyVer():
    pyver = open("pyver.txt", "w");
    subprocess.Popen("python -V", stdout=pyver)
    print ("exporting Python version...")


# step 1. check OS and if MSSQL-server is installed
stringstep1 = ("First, we need to check if this is a Red Hat box, and if MSSQL is installed")
print (stringstep1)
package = subprocess.Popen("rpm -q mssql-server", shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

# wait for the process to terminate
packagesqlout, packagesqlerr = package.communicate()
packagesqlerrcode = package.returncode

try:
    release = open('/etc/redhat-release', 'r').read()
    print ("You are using " + release + "and " + packagesqlout)
except:
    print("You are not using Red Hat and " + packagesqlout)

