<html>
<table>
<tr>
<td><div align=center><img src="https://mscorpmedia.azureedge.net/mscorpmedia/2016/03/SQL-Loves-Linux_2_Twitter-002-640x358.png" height=300></div>
<br>
<div align=center><img src=https://s18.postimg.org/aih0iu79l/rhmssqlsdp1.png></div>
<tr>
<td>
<ul>
<li>
Microsoft SQL Support Diagnostic Package for Red Hat (WORK IN PROGRESS, NON OPERATIONAL YET)
<li>
This script will gather basic system information for helping troubleshooting MSSQL server issues
<li>
This is currently being developed and tested on RedHat Enterprise 7.3, with current preview of MSSQL-Server and Python 2.7.6
</ul>
<tr>
<td>
<h2><u>Current features:</u></h2>
<ul>
<li>OS detection (reads off <tt>/etc/redhat-release</tt>)
<li>MSSQL-Server RPM package detection (runs <tt>rpm -q mssql-server</tt>)
</ul>
<tr>
<td>
<h2><u>TO-DO:</u></h2>
<ul>
<li>Collect system info (so far would be process list, netstat, df, systemctl log, ifconfig, uname, and Python version)
<li>zip everything
<li>error handling in general
</ul>
<tr>
<td>
<h2><u>Instructions:</u></h2>
<ul>
<li><tt>git clone https://github.com/audricd/rhmssqlsdp.git</tt>
<li><tt>python main.py</tt>
<tr>
<td>
<h2><u>Changelog:</u></h2>
<ul>
<li><b>v0.1</b> OS and MSSQL-Server rpm package working with RHEL 7.3 and Python 2.7.5 (27/11/2016)
<li><b>v0.0.1</b> init. just working notes
</table>
