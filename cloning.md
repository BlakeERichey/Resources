# Linux  
## Create SSH Key
`ssh-keygen -t ed25519 -C "Add Key Comment"`  
If you are using a legacy system that doesn't support the Ed25519 algorithm, use:  
`ssh-keygen -t rsa -b 4096 -C "Add Key Comment"`  

## Start SSH Agent  
`eval "$(ssh-agent -s)"`  

## Add SSH key to SSH Agent  
`ssh-add ~/.ssh/id_ed25519`  

*Then add Public SSH key to github profile*  