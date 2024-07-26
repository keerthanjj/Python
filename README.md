[![Codacy Badge](https://app.codacy.com/project/badge/Grade/950da88a5574485887a6ba97aa26c25e)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JDA-Product-Development/plat-jdp-bulk-pipeline-setup&amp;utm_campaign=Badge_Grade)
# plat-jdp-bulk-pipeline-setup

## Abstract

This service handles the below 
- Onboard a new realm
- Check the status of realm onboarding 
- Listening to LIAM events
- Schema access to functional role in snowflake
- Migrate the metadata from one realm to another
- Offboard a realm

## Local setup
To run the service locally, first, set up a virtual environment with Python 3.9 and install all packages in requirements.txt.

### Environment variables
"Then, In a shell supply the following environment variables:"
``````
ENVIRONMENT_VARIABLE_AEH_FLAG=false
ENVIRONMENT_VARIABLE_AEP_API_URL=https://api-tst-private.jdadelivers.com/dp/bulkpipelinesetup/v1/platformOnboardRealm
ENVIRONMENT_VARIABLE_APIM_API_BASE_URL=https://api-tst.jdadelivers.com/
ENVIRONMENT_VARIABLE_APIM_CHANGES_CLIENT_ID=acb25f5b-e63b-48c3-820f-9054c1fa6dad
ENVIRONMENT_VARIABLE_APIM_CHANGES_LIAM_TOKEN_URL=https://blueyonderinteroptestus.b2clogin.com/blueyonderinteroptestus.onmicrosoft.com/B2C_1A_ClientCredential/oauth2/v2.0/token
ENVIRONMENT_VARIABLE_APIM_CHANGES_SCOPE=https://blueyonderinteroptestus.onmicrosoft.com/6ad21424-b4b2-462e-80df-252ec22dd6a9/.default
ENVIRONMENT_VARIABLE_AUTHENTICATION_ENABLED=false
ENVIRONMENT_VARIABLE_AUTOSCALING_MAX_REPLICAS=3
ENVIRONMENT_VARIABLE_AUTOSCALING_MIN_REPLICAS=2
ENVIRONMENT_VARIABLE_AZURE_EVENTHUB=evhn-jdp-by-dev-01.servicebus.windows.net:9093
ENVIRONMENT_VARIABLE_AZURE_EVENTHUB_CONSUMER_TOPIC=liam.realm.notification
ENVIRONMENT_VARIABLE_AZURE_EVENTHUB_GROUP_ID=REALM-ONBOARDING-AUTOMATION-007
ENVIRONMENT_VARIABLE_BULK_INGESTION_ENVIRONMENT=dev
ENVIRONMENT_VARIABLE_BULK_INGESTION_INSTANCE=01
ENVIRONMENT_VARIABLE_BULK_INGESTION_REGION=eus2
ENVIRONMENT_VARIABLE_COST_CENTER_ID=474000
ENVIRONMENT_VARIABLE_COST_TAGGING_TEAM=plat_lpdm
ENVIRONMENT_VARIABLE_COST_TAGGING_TYPE=Dev
ENVIRONMENT_VARIABLE_DATAPLATFORM_ENTITLEMENT_MODULE_ID=2002000002
ENVIRONMENT_VARIABLE_GEOGRAPHY=us
ENVIRONMENT_VARIABLE_HOST=0.0.0.0
ENVIRONMENT_VARIABLE_LIAM_EVENT_TYPE_CREATED=iam.realm.created
ENVIRONMENT_VARIABLE_LIAM_EVENT_TYPE_DELETED=iam.realm.deleted
ENVIRONMENT_VARIABLE_LIAM_EVENT_TYPE_ENTITLEMENT_ADDED=iam.realm.entitlement.added
ENVIRONMENT_VARIABLE_LIAM_EVENT_TYPE_UPDATED=iam.realm.updated
ENVIRONMENT_VARIABLE_NETWORK_ACCESS=internal
ENVIRONMENT_VARIABLE_RBAC_PERMISSION_REALM_ADMIN=by.dp.realm.admin
ENVIRONMENT_VARIABLE_RBAC_PERMISSION_URL=https://api-tst-private.jdadelivers.com/iam/realm/v1/subjects/{subject_id}/searchPermissions
ENVIRONMENT_VARIABLE_RESOURCES_CPU=1.2
ENVIRONMENT_VARIABLE_RESOURCES_MEMORY_MB=1024
ENVIRONMENT_VARIABLE_RESOURCES_QUALITY_OF_SERVICE=best-effort
ENVIRONMENT_VARIABLE_SNOWFLAKE_ACCOUNT_NAME=ov40102.east-us-2.azure
ENVIRONMENT_VARIABLE_SNOWFLAKE_DATABASE_NAME=DEV_PLAT_LPDM_UPGRADE_DB2
ENVIRONMENT_VARIABLE_SNOWFLAKE_DATABASE_URL=by-us_dev
ENVIRONMENT_VARIABLE_SNOWFLAKE_ROLE=DEV_PLAT_LPDM_SERVICE_ELT_FR
ENVIRONMENT_VARIABLE_SNOWFLAKE_SA_LPDM_BLKPIPSET_USERNAME=sa_lpdm_dev_blkpipset
ENVIRONMENT_VARIABLE_SNOWFLAKE_SCHEMA_NAME=BY_METADATA
ENVIRONMENT_VARIABLE_SNOWFLAKE_SECURITY_ADMIN_ROLE=DEV_PLAT_LPDM_SECURITYADMIN_FR
ENVIRONMENT_VARIABLE_SNOWFLAKE_SYSTEM_ADMIN_ROLE=DEV_PLAT_LPDM_SYSADMIN_FR
ENVIRONMENT_VARIABLE_SNOWFLAKE_WAREHOUSE_NAME=DEV_PLAT_LPDM_SERVICE_ELT_WH
ENVIRONMENT_VARIABLE_STRATOSPHERE_DEBUG_MODE=false
ENVIRONMENT_VARIABLE_STRATOSPHERE_ENVIRONMENT=staging
ENVIRONMENT_VARIABLE_STRATOSPHERE_MANAGED_AZURE_KEY_VAULT_NAME=ENVIRONMENT_VARIABLE_STRATOSPHERE_MANAGED_AZURE_KEY_VAULT_NAME
ENVIRONMENT_VARIABLE_STRATOSPHERE_SA_CLIENT_ID=stratosphere-sa-jdp-blk-dev-eus2-01
ENVIRONMENT_VARIABLE_STRATOSPHERE_UNMANAGED_STORAGE_ACCOUNT_NAME=storjdpblkdeveus201
ENVIRONMENT_VARIABLE_STREAMING_API_URL=https://api-tst-private.jdadelivers.com/dp/streaming/config/v1/realm/{0}/onboard?type\=all
ENVIRONMENT_VARIABLE_VASCO_DOWNSTREAM_TOPIC_NAME=vasco.transform.topic
ENVIRONMENT_VARIABLE_VASCO_ENTITLEMENT_MODULE_ID=9000000011
ENVIRONMENT_VARIABLE_WAREHOUSE_FLAG=false
ENVIRONMENT_VARIABLE_WAREHOUSE_MAX_CLUSTER_COUNT=10
ENVIRONMENT_VARIABLE_WAREHOUSE_PURPOSE=PLAT_LPDM
ENVIRONMENT_VARIABLE_WAREHOUSE_SIZE=XSMALL
PORT=8000
STRATOSPHERE_PROJECT_NAME=STRATOSPHERE_PROJECT_NAME
STRATOSPHERE_SECRETS_DIR=/Users/xxx/xxx/xxx/BY/plat-jdp-bulk-pipeline-setup/STRATOSPHERE_SECRETS_DIR(Adjust the path as needed).
``````

### Secrets
In order to use secrets, a directory structure in the shape of `STRATOSPHERE_SECRETS_DIR/STRATOSPHERE_PROJECT_NAME/ENVIRONMENT_VARIABLE_STRATOSPHERE_MANAGED_AZURE_KEY_VAULT_NAME` has to be present in the file system, where the value of `STRATOSPHERE_SECRETS_DIR` has to be an absolute path while the successive variables have to have the values of subdirectories within `STRATOSPHERE_SECRETS_DIR`. Inside terminal ,
Use this command 
``````
mkdir -p STRATOSPHERE_SECRETS_DIR/STRATOSPHERE_PROJECT_NAME/ENVIRONMENT_VARIABLE_STRATOSPHERE_MANAGED_AZURE_KEY_VAULT_NAME
``````

`ENVIRONMENT_VARIABLE_STRATOSPHERE_MANAGED_AZURE_KEY_VAULT_NAME` folder, place one file for each secret, that has the name of the secret as its file name and contains the value of the secret. 

#### Secrets this service uses
 `snowflake-sa-lpdm-dev-euw-01-blkpipset-password`: password for user `ENVIRONMENT_VARIABLE_SNOWFLAKE_SA_LPDM_BLKPIPSET_USERNAME` in the Snowflake account [https://by-us_dev.snowflakecomputing.com/](https://by-us_dev.snowflakecomputing.com/). 
 
 `jdp-by-dev-eus2-01-blkpipset-global-kafka-JaasConfig`, 
 
 `liam-apim-api-dev-eus2-01-client-secret`, 
 
 `storage-account-storjdpblkdeveus201-access-key1`, 
 
 `stratosphere-sa-jdp-blk-dev-eus2-01-client-secret`. 
 
### Starting the service
Given the above prerequisites are met, start the service with

```uvicorn service.app:app --reload```

Or with a run configuration in PyCharm that specifies the above environment variables, starts a "module name" (in the "script path" dropdown) and has `uvicorn` specified as module and `service.app:app --reload` specified as parameters.

For Testing:
To run all unittestcase at once,
In terminal use below command 
``````
set UNIT_TESTING=true
coverage run -m pytest tests
``````
