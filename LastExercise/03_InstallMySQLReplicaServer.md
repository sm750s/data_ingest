
### MySQL/MariaDB Installation La
#### Configure MySQL with a replica server
Choose one of these plans to follow:
  - You can use the steps documented here for MariaDB or here for MySQL.
  - The steps below are MySQL-specific.
    - If you are using RHEL/CentOS 7.x, use MariaDB.

### MySQL installation - Plan Two Detail
  1. Download and implement the official MySQL repo
    - Enable the repo to install MySQL 5.5
    - Install the mysql package on all nodes
    - Install mysql-server on the server and replica nodes
    - Download and copy the JDBC connector to all nodes.
  2. You should not need to build a /etc/my.cnf file to start your MySQL server
    - You will have to modify it to support replication. Check MySQL documentation.
  3. Start the mysqld service.
  4. Use /usr/bin/mysql_secure_installation to:
    1. Set password protection for the server
    2. Revoke permissions for anonymous users
    3. Permit remote privileged login
    4. Remove test databases
    5. Refresh privileges in memory
    6. Refreshes the mysqld service
