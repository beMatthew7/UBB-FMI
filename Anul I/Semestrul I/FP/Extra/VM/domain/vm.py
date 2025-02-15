class VM:
    def __init__(self, id, nume, cpu_capacity, disk_type, price_hour):
        self.__id = id
        self.__nume = nume
        self.__cpu_capacity = cpu_capacity
        self.__disk_type = disk_type
        self.__price_hour = price_hour

    def get_id(self):
        return self.__id
    
    def get_nume(self):
        return self.__nume
    
    def get_cpu_capacity(self):
        return self.__cpu_capacity 

    def get_disk_type(self):
        return self.__disk_type

    def get_price_hour(self):
        return self.__price_hour
       