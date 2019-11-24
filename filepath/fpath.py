''' fpath
'''

from pathlib import Path
import os


class WPath():
    def __init__(self, path):
        self._path = Path(path)

    def touch(self, mtime, atime=None):
        if atime is None:
            atime = mtime
        os.utime(self._path, (atime, mtime))

    def __getattr__(self, name):
        value = self.__dict__.get(name)
        if not value:
            value = getattr(self._path, name)
        return value


def main():
    path = WPath('.')
    t = 0
    for f in path.glob('*'):
        t = max(t, f.stat().st_ctime)

    path.touch(t)


if __name__ == '__main__':
    main()
