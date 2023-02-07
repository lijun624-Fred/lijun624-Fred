import os
import role_assign

def group_copy_membership():
    with open('grouplist.txt', 'r') as groups:
        while True:
            groupname = groups.readline()
            if not groupname:
                break
            groupname = groupname.strip('\n')
            cmd_group_list = "az ad group member list --group " + groupname + " |grep userPrincipalName|awk '{print $2}'"
            memberlist = os.popen(cmd_group_list).read()
            nt_member = memberlist.replace(role_assign.old_domain, role_assign.new_domain).split('\n')
            if nt_member[-1] == '': nt_member.pop()  #remove the empty element in the end
            for member in nt_member:
                cmd_add_membership = "az ad group member add --group " + groupname + " --member-id " + member
                print(cmd_add_membership)

if __name__ == "__main__":
    group_copy_membership()
