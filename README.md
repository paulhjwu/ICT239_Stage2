# ICT239_Stage2

I change something here

adding something then want to synch

Something more 

sudo apt install gnome-keyring gnupg2 pass -y

It does not fail actually

What is the status now?

Did not see what you typed earlier

still having errors

I am fine now


1) Download docker-credential-pass from https://github.com/docker/docker-credential-helpers/releases

2) tar -xvf docker-credential-pass.tar.gz

3) chmod u+x docker-credential-pass

4) mv docker-credential-pass /usr/bin

5) You will need to setup docker-credential-pass (following steps are based of https://github.com/docker/docker-credential-helpers/issues/102#issuecomment-388634452)

5.1) install gpg and pass (apt-get install gpg pass)

5.2) gpg --generate-key, enter your information. You should see something like this:

pub   rsa3072 2018-10-07 [SC] [expires: 2020-10-06]
      1234567890ABCDEF1234567890ABCDEF12345678
Copy the 123... line

5.3) pass init 1234567890ABCDEF1234567890ABCDEF12345678 (paste)

5.4) pass insert docker-credential-helpers/docker-pass-initialized-check and set the next password "pass is initialized" (without quotes).

5.5) pass show docker-credential-helpers/docker-pass-initialized-check. You should see pass is initialized.

5.6) docker-credential-pass list

6) create a ~/.docker/config.json with:

{
"credsStore": "pass"
}