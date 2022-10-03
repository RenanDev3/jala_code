def search_asset_by_status(items=[], asset_status=''):
    if items == []:
        return []
    elif asset_status == '':
        result_list = []
        result_list = [ item for item in items]
        return result_list
    else:
        result_list = []
        result_list = [ item for item in items if item['asset_status'] == asset_status ]
        return result_list


def search_asset_by_technical_specs(items=[], search_tokens=''):
    result_list = []
    # desired_fields = ["serial_no", "asset_type", "hardware_standard", "technical_specs", "asset_status"]
    search_tokens = list(search_tokens)
    if items == []:
        return result_list
    else:
        result_list = [item for item in items if set(search_tokens).issubset(
            (item['technical_specs']).lower().replace(' / ', ' ').split(' ')) ]
        return result_list