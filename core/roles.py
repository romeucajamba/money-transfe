from rolepermissions.roles import AbstractUserRole


class People(AbstractUserRole):
    avaliable_permissions = {
        'make_transfer': True,
        'rceive_transfer': True
    }

class Compay(AbstractUserRole):
    avaliable_permissions = {
        'make_transfer': False,
        'rceive_transfer': True
    }