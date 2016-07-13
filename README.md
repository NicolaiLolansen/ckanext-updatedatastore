# ckanext-updatedatastore
Uses the DataPusher to push every CSV resource from URL to the DataStore, using a Paster command

Installing
NB! This module is developed on CKAN v2.5.2, compatibility with other version is not ensured

### Activate virtualenv
```
source /usr/lib/ckan/default/bin/activate
cd /usr/lib/ckan/default/src
git clone git@github.com:NicolaiMogensen/ckanext-updatedatastore.git
cd ckanext-updatedatastore
```

### Install Extension
```
python setup.py develop
sudo nano /etc/ckan/default/production.ini
```
### Enable plugin in configuration
```
 ckan.plugins = datastore ... updatedatastore
```
## Usage
The extension creates a command for periodical update of the Datastore. To execute the command periodically, add following cron job:

## this job runs daily at 03:55
```
55 3 * * * cd /usr/lib/ckan/default/src/ckanext-updatedatastore && /usr/lib/ckan/default/bin/python /usr/lib/ckan/default/bin/paster update --config=/etc/ckan/default/production.ini
```

