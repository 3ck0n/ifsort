# Image Folder Sort
Image Folder Sort (IFSort) analysis unstructured files and generates a folder structure to sort them.

Structure is based on this scheme
- Archivename YYYY
  - MM Month
     - DD name of series
       - Original files

Background: Got a Gigabytes of unsorted image data which is organised in thousands of folders. Before analyse them with Adobe Lightroom a raw file structure should be used in a way other raw files are already organized.

## Usage

1. Modify variables in analyse.py to your source and target folders
2. Run analyse.py 
3. A file report.json is generated, analyse them manually to make sure, everything is ok
4. Run move.py
