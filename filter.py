import os

files = os.listdir('C:/Users/User/Pictures/Screenshots')

for file in files:
    foldername = os.path.getctime(file)
    print(foldername)

# {
#     $foldername = $file.CreationTime.ToString('yyyy-MM')
#     $topath = "$rootpath\$foldername"
#     if(-not(Test-Path $topath -PathType Container)){
#         New-Item $topath -ItemType Directory
#     }
#     Move-Item $file.FullName $topath
# }

"""
$rootpath = 'C:\Path\To\Pictures'
$files = Get-ChildItem $rootpath -File
foreach($file in $files) {
    $foldername = $file.CreationTime.ToString('yyyy-MM')
    $topath = "$rootpath\$foldername"
    if(-not(Test-Path $topath -PathType Container)){
        New-Item $topath -ItemType Directory
    }
    Move-Item $file.FullName $topath
}
"""