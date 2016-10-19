import binascii
import os

prefix_vehicle = 'uploads/vehicle/'
prefix_profile = 'uploads/profile/'


def upload_vehicle_image(instance, filename):
    key = binascii.b2a_hex(os.urandom(5))
    file_base, extension = filename.split(".")
    path_file = u"{0:s}/{1:s}.{2:s}".format(
        str(instance.vehicle.id), str(key), extension)
    return os.path.join(prefix_vehicle, path_file)


def upload_user_profile(instance, filename):
    file_base, extension = filename.split(".")
    path_file = "user/{0:s}.{1:s}".format(str(instance.user.id), extension)
    return os.path.join(prefix_profile, path_file)