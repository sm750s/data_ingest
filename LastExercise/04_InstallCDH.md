
### Cloudera Manager Install Lab
#### Install a cluster and deploy CDH
Adhere to the following requirements while creating your cluster:
  - Do not use Single User Mode. Do not. Don't do it.
  - Ignore any steps in the CM wizard that are marked (Optional)
  - Install the Data Hub Edition
  - Install CDH using parcels
  - Deploy only the Core set of CDH services.
  - Deploy three ZooKeeper instances.
    - CM does not tell you to do this but complains if you don't

1. Open Cloudera Manager Console from a browser
![Image of Install CDH 001](screenshots/install-cdh-001.png)

2. Put target nodes' FQDN
![Image of Install CDH 002](screenshots/install-cdh-002.png)

3. Select nodes on the list
![Image of Install CDH 003](screenshots/install-cdh-003.png)

4. Put account information for agent installation
> TODO: take a screenshot

5. Check the installation steps on each nodes
![Image of Install CDH 004](screenshots/install-cdh-004.png)

6. Set roles on each nodes
![Image of Install CDH 005](screenshots/install-cdh-005.png)

7. Check roles on each nodes
![Image of Install CDH 006](screenshots/install-cdh-006.png)

8. Set Database information for each services
![Image of Install CDH 007](screenshots/install-cdh-007.png)

9. Check cluster setting
![Image of Install CDH 008](screenshots/install-cdh-008.png)

10. Check cluster setting steps on each services
![Image of Install CDH 009](screenshots/install-cdh-009.png)

11. Final message of cluster installation
![Image of Install CDH 010](screenshots/install-cdh-010.png)
