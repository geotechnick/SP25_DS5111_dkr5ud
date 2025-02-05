# How to set up your VM so we have ssh access for pull/push/clone/fetch
The instructions are a compact form of [Github's instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)


## Instructions (NB: I use my email and id for clarity, just substitute your own as you go through)
*  `ssh-keygen -t ed25519 -C "efrainolivaresuva@gmail.com"`
    - Use default file name, and press enter to 'not' use a passkey at the prompts
* Go to github and click on your avatar (upper right)
* Click on Settings, then look on left hand side menu
* Click on SSH and GPG Keys
* Add a new SSH key
* Name it so it matches your vm, in my case `25SP_efrain_dpy8wq`
* Now on the vm, cat the content of the pub side of the key, and paste it into the field
    - `cat id_ed25519.pub`
* You can then test with `ssh -T -i ed25519 git@github.com` and you should see your github name echo back (NB: no .pub, you're using the private side key)

After I created the key, this is what I see when I run that test command

```bash
ubuntu@ip-172-31-83-121:~/.ssh$  ssh -T -i id_ed25519 git@github.com
Hi EfrainOlivaresUVA! You've successfully authenticated, but GitHub does not provide shell access.
ubuntu@ip-172-31-83-121:~/.ssh$
```

Note the 'Hi EfrainOlivaresUVA'.  If you see your username then you are good to go to next step.
