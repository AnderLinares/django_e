import os
prefix_profile = 'uploads/profiles/'


def upload_location_profile(instance, filename):
    file_base, extension = filename.split(".")
    path_file = "{0:s}/{1:s}.{2:s}".format(
        str(instance.user.id), str(instance.id), extension)
    return os.path.join(prefix_profile, path_file)


def upload_location_organization(instance, filename):
    file_base, extension = filename.split(".")
    path_file = "{0:s}/{1:s}.{2:s}".format(
        str(instance.user.id), str(instance.id), extension)
    return os.path.join(prefix_profile, path_file)
