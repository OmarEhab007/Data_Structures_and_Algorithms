import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    # if the initial path is a file returns the path otherwise an empty string
    if os.path.isfile(path):
        file = path
        if file.endswith('.' + suffix):
            return file
        return ''

    # create a list of file and subdirectories names in the given directory
    listOfFile = os.listdir(path)
    pathFiles = list()

    # Iterate over all the elements
    for element in listOfFile:
        # create path
        fullPath = os.path.join(path, element)
        # If element is a directory then find the files in this directory
        if os.path.isdir(fullPath):
            pathFiles = pathFiles + find_files(suffix, fullPath)
        else:
            if element.endswith('.' + suffix):
                pathFiles.append(fullPath)

    return pathFiles
