version_tag=$1
for d in ./component-definitions/* ; do
    compdef=$(basename "$d")
    if [ "$compdef" != "IBM_FS_FR_COMBINED" ]; then
       echo "Assembling ${compdef}" 
       if [ "$1" != "" ]; then 
          trestle author component-assemble --name $compdef --markdown md_components/$compdef --output $compdef --version $version_tag 
       else
          trestle author component-assemble --name $compdef --markdown md_components/$compdef --output $compdef 
       fi
    else 
       echo "Skipping ${compdef}"
    fi 
done
