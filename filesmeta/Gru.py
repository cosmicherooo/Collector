class Gru():

    def __init__(self):

        self._extensions = {}



    def add_minion(self, minion):

        ex = minion.ex
        for e in ex:
            self._extensions[e] = minion

    def get_meta_inf(self, path):

        def get_extension(path_to_a_file):
            last_part = path_to_a_file.split("/")[-1]
            if "." in last_part:
                ex = path_to_a_file.split(".")[-1]
            else:
                ex = None

        res = {}
        dict_common_metadata = CommonMetaMinion().get_meta_inf(path)
        ex = get_extension(path)
        dict_spec_metadata = self._extensions[ex].get_meta_inf(path)

        def final_data_func(dict_common, dict_spec):

            try:
                final_dict = {**dict_common, **dict_spec}
                return final_dict

            except:
                "Special data is somehow broken!"
                return dict_common

        final_metadata = final_data_func(dict_common_metadata,
                                         dict_spec_metadata)

        return final_metadata
