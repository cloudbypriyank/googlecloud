

## [YouTube Solution Link](https://www.youtube.com/watch?v=Y9SCb-8iwPE)
### Run the below commands in the Cloud Shell Terminal.

```cmd
export Region=<YOUR_REGION>
```

```cmd
export Zone=<YOUR_ZONE>
```

## Task 1: 

```cmd
gcloud compute networks create securenetwork --subnet-mode custom
```

## Task 2: 

```cmd
gcloud compute networks subnets create securenetwork-subnet --network=securenetwork --region $Region --range=192.168.16.0/20
```

## Task 3:

```cmd
gcloud compute firewall-rules create rdp-ingress-fw-rule --allow=tcp:3389 --source-ranges 0.0.0.0/0 --target-tags allow-rdp-traffic --network securenetwork
```

## Task 4: 

```cmd
gcloud compute instances create vm-bastionhost --zone=$Zone --machine-type=e2-medium --network-interface=subnet=securenetwork-subnet --network-interface=subnet=default,no-address --tags=allow-rdp-traffic --image=projects/windows-cloud/global/images/windows-server-2016-dc-v20220513
```

## Task 5: 

* The below command will make an instance with `No External IP Address` which is `required` in task 5.
```cmd
gcloud compute instances create vm-securehost --zone=$Zone --machine-type=e2-medium --network-interface=subnet=securenetwork-subnet,no-address --network-interface=subnet=default,no-address --tags=allow-rdp-traffic --image=projects/windows-cloud/global/images/windows-server-2016-dc-v20220513
```
### *You can now end your lab at task 5 and check if the green tick came beside the lab or not.*
### *If you see the green tick, then congratulations! Your work here was successful.*

* If you want to perform the `task 6` then you should have to run the below command.
```
gcloud compute instances create vm-securehost --zone=$Zone --machine-type=e2-medium --network-interface=subnet=securenetwork-subnet --network-interface=subnet=default,no-address --tags=allow-rdp-traffic --image=projects/windows-cloud/global/images/windows-server-2016-dc-v20220513
```

## Task 6: 

```cmd
gcloud compute reset-windows-password vm-securehost --user app_admin --zone $Zone
```

If asking choose y/n then press "y", and then hit Enter.

* Now, copy the username and password for app_admin user, we need this to login into bastion vm.

## Manual Steps (*Necessary to perform)

* Click on `Add roles and features`.




* Click *next* > *next* > *Install*

