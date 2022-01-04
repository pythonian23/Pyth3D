class Drawer:
    def __init__(self, *args, **kwargs):
        self.__lib_init__(*args, **kwargs)

    def __lib_init__(self, *args, **kwargs):
        pass

    def __draw__(self, coord0, coord1, coord2, *args, **kwargs):
        pass

    def __update__(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        self.__update__(*args, **kwargs)

    def polygon(self, *args, **kwargs):
        for i in range(1, len(args) - 1):
            self.__draw__(args[0], *args[i:i + 2], **kwargs)
