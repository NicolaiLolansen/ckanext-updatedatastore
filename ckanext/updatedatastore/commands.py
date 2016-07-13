import sys
import copy
import ckanapi
from ckan.logic import get_action
from ckan.lib.cli import CkanCommand
import time

class Update(CkanCommand):

    ''' Updates all CSV resources in the Datastore by using the Datapusher
        Usage:
          update 
            - Updates all CSV resources in the datastore
    '''

    summary = __doc__.split('\n')[0]
    usage = __doc__

    def command(self):
        self._load_config()
	print("Welcome to datastore updater")
	
	try: 
	    ckan = ckanapi.LocalCKAN()
        except:
	    print("Could not instantiate CKAN")
	    sys.exit()

	datasetName = '' #Find all dataset
    	try:
            datasetList = ckan.action.package_autocomplete(q='', limit=10000)
   	except:
            print("Could not find dataset, or something went wrong.. exiting")
            sys.exit()

        for i in datasetList:
            dataset = ckan.action.package_show(id=i["name"])
            for i in dataset["resources"]:
                if (i["format"] == "CSV" or i["format"] == "csv") and i["url_type"] != "upload":
                    url = i["url"]
                    print("updated CSV on", dataset["name"])
                    ckan.action.resource_update(id=i["id"],package_id=i["package_id"],name=i["name"],format=i["format"],url=i["url"]+"&")
                    time.sleep(5)
		    ckan.action.resource_update(id=i["id"],package_id=i["package_id"],name=i["name"],format=i["format"],url=url)
		    time.sleep(10)
