from library.db_connection import database


def validate_unique_service_name(data):
    service_name = data.get('service_name')
    service = database.config.find_one({"service_name": service_name})
    if not service:
        return True
    return False


def make_serizable(obj):
    obj['_id'] = str(obj.get('_id'))
    return obj

def add_config(data):
    if validate_unique_service_name(data):
        config_id = database.config.insert_one(data)
        config_obj = database.config.find_one({"_id": config_id.inserted_id})
        return make_serizable(config_obj)
    else:
        changed_data = {k: v for k, v in data.items() if v is not None}
        update_report = database.config.update_one(
            {"service_name": data["service_name"],},
            {"$set": changed_data}
        )
        if update_report.modified_count > 0:
            return {"message": "Updated Successfully"}
        else:
            return {"message": " failed to update data"}
        

   