```
[centos@cm1 ~]$ sudo yum install -y wget
[centos@cm1 ~]$ sudo wget https://archive.cloudera.com/cm5/redhat/7/x86_64/cm/cloudera-manager.repo -P /etc/yum.repos.d/
[centos@cm1 ~]$ sudo sed -i 's/x86_64\/cm\/5/x86_64\/cm\/5.15.2/g' /etc/yum.repos.d/cloudera-manager.repo
[centos@cm1 ~]$ sudo rpm --import https://archive.cloudera.com/cm5/redhat/7/x86_64/cm/RPM-GPG-KEY-cloudera
[centos@cm1 ~]$ sudo yum install -y oracle-j2sdk1.7
[centos@cm1 ~]$ sudo yum install -y cloudera-manager-daemons cloudera-manager-server
sudo yum install cloudera-manager-daemons cloudera-manager-server
sudo yum install mariadb-server
sudo vi /etc/my.cnf
[centos@cm1 ~]$ sudo systemctl enable mariadb
Created symlink from /etc/systemd/system/multi-user.target.wants/mariadb.service to /usr/lib/systemd/system/mariadb.service.
[centos@cm1 ~]$
[centos@cm1 ~]$ sudo systemctl start mariadb
[centos@cm1 ~]$ sudo /usr/bin/mysql_secure_installation
[centos@cm1 ~]$ sudo wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.46.tar.gz ~/
[centos@cm1 ~]$ tar zxvf mysql-connector-java-5.1.46.tar.gz
[centos@cm1 mysql-connector-java-5.1.46]$ mysql -u root -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 9
Server version: 5.5.60-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE DATABASE scm DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; GRANT ALL ON scm.* TO 'scm'@'%' IDENTIFIED BY 'training';
CREATE DATABASE amon DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; GRANT ALL ON amon.* TO 'amon'@'%' IDENTIFIED BY 'training';
Query OK, 1 row affected (0.00 sec)

CREATE DATABASE rmon DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; GRANT ALL ON rmon.* TO 'rmon'@'%' IDENTIFIED BY 'training';
Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> CREATE DATABASE amon DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; GRANT ALL ON amon.* TO 'amon'@'%' IDENTIFIED BY 'training';
CREATE DATABASE hue DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; GRANT ALL ON hue.* TO 'hue'@'%' IDENTIFIED BY 'training';
Query OK, 1 row affected (0.00 sec)

CREATE DATABASE metastore DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; GRANT ALL ON metastore.* TO 'metastore'@'%' IDENTIFIED BY 'training';
Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> CREATE DATABASE rmon DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; GRANT ALL ON rmon.* TO 'rmon'@'%' IDENTIFIED BY 'training';
CREATE DATABASE sentry DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; GRANT ALL ON sentry.* TO 'sentry'@'%' IDENTIFIED BY 'training';
Query OK, 1 row affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> CREATE DATABASE hue DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; GRANT ALL ON hue.* TO 'hue'@'%' IDENTIFIED BY 'training';
CREATE DATABASE oozie DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; GRANT ALL ON oozie.* TO 'oozie'@'%' IDENTIFIED BY 'training';Query OK, 1 row affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> CREATE DATABASE metastore DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; GRANT ALL ON metastore.* TO 'metastore'@'%' IDENTIFIED BY 'training';
Query OK, 1 row affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> CREATE DATABASE sentry DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; GRANT ALL ON sentry.* TO 'sentry'@'%' IDENTIFIED BY 'training';
Query OK, 1 row affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> CREATE DATABASE oozie DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; GRANT ALL ON oozie.* TO 'oozie'@'%' IDENTIFIED BY 'training';
Query OK, 1 row affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| amon               |
| hue                |
| metastore          |
| mysql              |
| oozie              |
| performance_schema |
| rmon               |
| scm                |
| sentry             |
+--------------------+
10 rows in set (0.00 sec)



MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.00 sec)



[centos@cm1 mysql-connector-java-5.1.46]$ sudo /usr/share/cmf/schema/scm_prepare_database.sh mysql scm scm training
JAVA_HOME=/usr/java/jdk1.7.0_67-cloudera
Verifying that we can write to /etc/cloudera-scm-server
Creating SCM configuration file in /etc/cloudera-scm-server
Executing:  /usr/java/jdk1.7.0_67-cloudera/bin/java -cp /usr/share/java/mysql-connector-java.jar:/usr/share/java/oracle-connector-java.jar:/usr/share/java/postgresql-connector-java.jar:/usr/share/cmf/schema/../lib/* com.cloudera.enterprise.dbutil.DbCommandExecutor /etc/cloudera-scm-server/db.properties com.cloudera.cmf.db.
[                          main] DbCommandExecutor              INFO  Successfully connected to database.
All done, your SCM database is configured correctly!

[centos@cm1 mysql-connector-java-5.1.46]$ sudo systemctl start cloudera-scm-server
[centos@cm1 mysql-connector-java-5.1.46]$ sudo tail -f /var/log/cloudera-scm-server/cloudera-scm-server.log


```

```
$ sudo useradd training -g wheel
$ sudo passwd training
Changing password for user training.
New password:
BAD PASSWORD: The password contains the user name in some form
Retype new password:
passwd: all authentication tokens updated successfully.


[centos@w1 .ssh]$ su - training
Password:
[training@w1 ~]$ mkdir .ssh
[training@w1 ~]$ vi .ssh/authorized_keys
[training@w1 ~]$ chmod 600 .ssh/authorized_keys
[training@w1 ~]$
[training@m1 ~]$ sudo cat /etc/hosts



[training@cm1 home]$ sudo visudo
## Allows people in group wheel to run all commands
#%wheel ALL=(ALL)       ALL

## Same thing without a password
%wheel  ALL=(ALL)       NOPASSWD: ALL

```


### Cloudera Manager Install Lab
#### Path B install using CM 5.15.x
[The full rundown](https://www.cloudera.com/documentation/enterprise/5-15-x/topics/install_cm_cdh.html) is here. You will have to modify your package repo to get the right release. The default repo download always points to the latest version.

Use the documentation to complete the following objectives:

  - Install a supported Oracle JDK on your first node
  - Install a supported JDBC connector on all nodes
  - Create the databases and access grants you will need
  - Configure Cloudera Manager to connect to the database
  - Start your Cloudera Manager server -- debug as necessary
  - Do not continue until you can browse your CM instance at port 7180
