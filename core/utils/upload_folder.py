import binascii
import os

prefix_vehicle = 'uploads/vehicle/'
prefix_customer = 'uploads/customer/'
prefix_product = 'uploads/product/'
prefix_organization = 'uploads/organization/'


def upload_vehicle_image(instance, filename):
    key = binascii.b2a_hex(os.urandom(5))
    file_base, extension = filename.split(".")
    path_file = u"{0:s}/{1:s}.{2:s}".format(
        str(instance.vehicle.id), str(key), extension)
    return os.path.join(prefix_vehicle, path_file)


def upload_product_image(instance, filename):
    key = binascii.b2a_hex(os.urandom(5))
    file_base, extension = filename.split(".")
    path_file = u"{0:s}/product-{1:s}.{2:s}".format(
        str(instance.id), str(key), extension)
    return os.path.join(prefix_product, path_file)


def upload_organization_image(instance, filename):
    key = binascii.b2a_hex(os.urandom(5))
    file_base, extension = filename.split(".")
    path_file = u"{0:s}/organization-{1:s}.{2:s}".format(
        str(instance.id), str(key), extension)
    return os.path.join(prefix_organization, path_file)


def upload_user_profile(instance, filename):
    key = binascii.b2a_hex(os.urandom(5))
    file_base, extension = filename.split(".")
    path_file = u"{0:s}/user-{1:s}.{2:s}".format(
        str(instance.user.id), str(key), extension)
    return os.path.join(prefix_customer, path_file)