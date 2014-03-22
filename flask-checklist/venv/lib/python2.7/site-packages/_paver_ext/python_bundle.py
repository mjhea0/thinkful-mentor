# ============================================================================
# PAVER EXTENSION (pavement.py)
# ============================================================================
# REQUIRES: paver >= 1.0
# DESCRIPTION:
#   Provides some tasks to bundle python packages.
#
# SEE ALSO:
#  * http://pypi.python.org/pypi/Paver/
#  * http://www.blueskyonmars.com/projects/paver/
# ============================================================================

from paver.easy import path, task, options, debug, info, error
import os

# ----------------------------------------------------------------------------
# CONFIGURATION:
# ----------------------------------------------------------------------------
#options(
#    bundle=Bunch(
#        archive  = "python-bundle.zip",
#        packages = [ "sphinx", "jinja2" ]
#    ),
#)

# ----------------------------------------------------------------------------
# TASKS:
# ----------------------------------------------------------------------------
@task
def bundle():
    """Bundle required Python packages as ZIP archive."""
    packages = options.bundle.packages
    builddir = path("build")/"bundle"
    builddir.makedirs()
    errors = 0
    for package in packages:
        try:
            info("bundle %s ..." % package)
            module   = __import__(package)
            pkgfile  = path(module.__file__)
            basedir  = pkgfile.dirname()
            destdir  = builddir/package
            if destdir.exists():
                destdir.rmtree()
            basedir.copytree(destdir)
        except StandardError, e:
            info("FAILED %s: %s" % (package, e))
            errors += 1

    archive = options.bundle.get("archive", "python-bundle.zip")
    stored_files = make_zip_archive(archive, builddir)

    # -- SUMMARY:
    message1  = "bundle {pkgno} packages into {archive} "
    message1 += "(with {errorno} errors, files: {fileno})"
    message   = message1.format(archive=archive, pkgno=len(packages),
                    errorno=errors, fileno=stored_files)
    output  = info
    if errors:
        message = "FAILED: {message}".format(message=message)
        output  = error
    output(message)

# ----------------------------------------------------------------------------
# UTILS:
# ----------------------------------------------------------------------------
def make_zip_archive(archive_name, basedir, files=None, file_pattern="*"):
    import zipfile
    archive_name = path(archive_name).abspath()
    curdir = os.getcwd()
    os.chdir(basedir)
    files_count = 0

    try:
        # -- STEP: Collect files.
        files2 = []
        if files is None:
            dirs = path(".").listdir(pattern="*")
            files2.extend(dirs)
        else:
            for file_ in files:
                if "*" in file_:
                    parts = path(".").glob(pattern=file_)
                    parts = [ part.normpath()   for part in parts ]
                    files2.extend(parts)
                else:
                    file_ = path(".")/file_
                    files2.append(file_.normpath())
        files3 = []
        for file_ in files2:
            if file_.isdir():
                files3.extend(file_.walkfiles(file_pattern))
            else:
                files3.append(file_)
        files = files3

        # -- STEP: Store files in archive.
        archive = zipfile.ZipFile(archive_name, "w", zipfile.ZIP_DEFLATED)
        for filename in files:
            debug("ZIP: Store %s ..." % filename)
            archive.write(filename)
        files_count = len(archive.namelist())
        archive.close()
    finally:
        os.chdir(curdir)
    return files_count

