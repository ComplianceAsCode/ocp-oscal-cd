for d in ./component-definitions/* ; do
    compdef=$(basename "$d")
    if [ "$compdef" != "IBM_FS_FR_COMBINED" ]; then
       echo "Regenerating ${compdef}" 
       trestle author component-generate --output md_components/$compdef --name $compdef
    else 
       echo "Skipping ${compdef}"
    fi 
done
