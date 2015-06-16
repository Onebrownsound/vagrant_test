from string import Template

# Global dictionary declaration, which houses all various configurations for each particular OS Choice
OPERATING_SYSTEMS = {

    "Centos_6.5": {"name": "chef/centos-6.5",
                   "description": "A standard CentOS 6.5 x64 base install",
                   },

    "Ubuntu_12.04_LTS_64bit_Server": {"name": "hashicorp/precise64",
                                      "description": "A standard CentOS 6.5 x64 base install",
                                      },

    "Lucid_32": {"name": "lucid32",
                 "description": "TODO",
                 },
    "Windows_Xp": {"name": "Windows_Xp",
                 "description": "Windows Xp 32 bit edition",
                 },

}

# This constant houses the baseline config file AS A TEMPLATE OBJECT
# Template objects may not be treated as regular strings
# In order to extract strings from a template object use the TEMPLATEOBJECT.safe_substitute() method,
# Which will return the template object as a string with the appropriate substitutions
BASE_VAGRANT_CONFIG = Template("""Vagrant.configure("2") do |config|
  config.vm.box ="${operating_system}"
  config.vm.provision :shell, path: "bootstrap.sh"
  config.vm.provider "virtualbox" do |v|
    v.gui = true
  end

end""")

# function responsible for prompting user for OS Choice
def PromptUserChoice():
    print "Greetings these are the follow choices for operatin systems ", OPERATING_SYSTEMS.keys(), " Please select one (case matters)"
    # mUserOsChoice is a string which represents the users choice for operating system
    # is case sensitive and be aware for underscores
    return raw_input()

def WriteVagrantConfig(mUserOsChoice):
    print ("...Writing Vagrant Configurations To File...")
    # The next line will open the Vagrant configuration as a file object known as f
    try:
        with open("Vagrantfile", "w+") as f:
            f.write(BASE_VAGRANT_CONFIG.safe_substitute(operating_system=OPERATING_SYSTEMS[mUserOsChoice]["name"]))
    except IOError:
        print("Apparently Vagrantfile does not exist.")
    print("Vagrantfile Succesfully Initialized")

def main():
    # Set mUserOsChoice to null, and repeat prompt until user response matches a key in OPERATING_SYSTEMS
    mUserOsChoice = None
    while (mUserOsChoice not in OPERATING_SYSTEMS.keys()):
        mUserOsChoice = PromptUserChoice()
    WriteVagrantConfig(mUserOsChoice)


if __name__=="__main__":
    main()
