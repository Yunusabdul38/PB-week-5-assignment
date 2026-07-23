#!/usr/bin/env python
# coding: utf-8

# In[1]:


############## PLEASE RUN THIS CELL FIRST! ###################

# import everything and define a test runner function
from importlib import reload
from helper import run
import ecc
import helper
import op
import script
import tx


# ### Exercise 1
# 
# Write the `op_checkmultisig` function of `op.py`.
# 
# #### Make [this test](/edit/code-ch08/op.py) pass: `op.py:OpTest:test_op_checkmultisig`

# In[2]:


# Exercise 1

reload(op)
run(op.OpTest("test_op_checkmultisig"))


# In[3]:


from helper import encode_base58_checksum
h160 = bytes.fromhex('74d691da1574e6b3c192ecfb52cc8984ee7b6c56')
print(encode_base58_checksum(b'\x05' + h160))


# ### Exercise 2
# 
# Write `h160_to_p2pkh_address` that converts a 20-byte hash160 into a p2pkh address.
# 
# #### Make [this test](/edit/code-ch08/helper.py) pass: `helper.py:HelperTest:test_p2pkh_address`

# In[4]:


# Exercise 2

reload(helper)
run(helper.HelperTest("test_p2pkh_address"))


# ### Exercise 3
# 
# Write `h160_to_p2sh_address` that converts a 20-byte hash160 into a p2sh address.
# 
# #### Make [this test](/edit/code-ch08/helper.py) pass: `helper.py:HelperTest:test_p2sh_address`

# In[5]:


# Exercise 3

reload(helper)
run(helper.HelperTest("test_p2sh_address"))


# In[6]:


from helper import hash256
modified_tx = bytes.fromhex('0100000001868278ed6ddfb6c1ed3ad5f8181eb0c7a385aa0836f01d5e4789e6bd304d87221a000000475221022626e955ea6ea6d98850c994f9107b036b1334f18ca8830bfff1295d21cfdb702103b287eaf122eea69030a0e9feed096bed8045c8b98bec453e1ffac7fbdbd4bb7152aeffffffff04d3b11400000000001976a914904a49878c0adfc3aa05de7afad2cc15f483a56a88ac7f400900000000001976a914418327e3f3dda4cf5b9089325a4b95abdfa0334088ac722c0c00000000001976a914ba35042cfe9fc66fd35ac2224eebdafd1028ad2788acdc4ace020000000017a91474d691da1574e6b3c192ecfb52cc8984ee7b6c56870000000001000000')
s256 = hash256(modified_tx)
z = int.from_bytes(s256, 'big')
print(hex(z))


# In[7]:


from ecc import S256Point, Signature
from helper import hash256
modified_tx = bytes.fromhex('0100000001868278ed6ddfb6c1ed3ad5f8181eb0c7a385aa0836f01d5e4789e6bd304d87221a000000475221022626e955ea6ea6d98850c994f9107b036b1334f18ca8830bfff1295d21cfdb702103b287eaf122eea69030a0e9feed096bed8045c8b98bec453e1ffac7fbdbd4bb7152aeffffffff04d3b11400000000001976a914904a49878c0adfc3aa05de7afad2cc15f483a56a88ac7f400900000000001976a914418327e3f3dda4cf5b9089325a4b95abdfa0334088ac722c0c00000000001976a914ba35042cfe9fc66fd35ac2224eebdafd1028ad2788acdc4ace020000000017a91474d691da1574e6b3c192ecfb52cc8984ee7b6c56870000000001000000')
h256 = hash256(modified_tx)
z = int.from_bytes(h256, 'big')
sec = bytes.fromhex('022626e955ea6ea6d98850c994f9107b036b1334f18ca8830bfff1295d21cfdb70')
der = bytes.fromhex('3045022100dc92655fe37036f47756db8102e0d7d5e28b3beb83a8fef4f5dc0559bddfb94e02205a36d4e4e6c7fcd16658c50783e00c341609977aed3ad00937bf4ee942a89937')
point = S256Point.parse(sec)
sig = Signature.parse(der)
print(point.verify(z, sig))


# ### Exercise 4
# 
# Validate the second signature from the transaction above.

# In[8]:


# Exercise 4

from io import BytesIO
from ecc import S256Point, Signature
from helper import encode_varint, hash256, int_to_little_endian
from script import Script
from tx import Tx, SIGHASH_ALL

hex_tx = '0100000001868278ed6ddfb6c1ed3ad5f8181eb0c7a385aa0836f01d5e4789e6bd304d87221a000000db00483045022100dc92655fe37036f47756db8102e0d7d5e28b3beb83a8fef4f5dc0559bddfb94e02205a36d4e4e6c7fcd16658c50783e00c341609977aed3ad00937bf4ee942a8993701483045022100da6bee3c93766232079a01639d07fa869598749729ae323eab8eef53577d611b02207bef15429dcadce2121ea07f233115c6f09034c0be68db99980b9a6c5e75402201475221022626e955ea6ea6d98850c994f9107b036b1334f18ca8830bfff1295d21cfdb702103b287eaf122eea69030a0e9feed096bed8045c8b98bec453e1ffac7fbdbd4bb7152aeffffffff04d3b11400000000001976a914904a49878c0adfc3aa05de7afad2cc15f483a56a88ac7f400900000000001976a914418327e3f3dda4cf5b9089325a4b95abdfa0334088ac722c0c00000000001976a914ba35042cfe9fc66fd35ac2224eebdafd1028ad2788acdc4ace020000000017a91474d691da1574e6b3c192ecfb52cc8984ee7b6c568700000000'
hex_sec = '03b287eaf122eea69030a0e9feed096bed8045c8b98bec453e1ffac7fbdbd4bb71'
hex_der = '3045022100da6bee3c93766232079a01639d07fa869598749729ae323eab8eef53577d611b02207bef15429dcadce2121ea07f233115c6f09034c0be68db99980b9a6c5e754022'
hex_redeem_script = '475221022626e955ea6ea6d98850c994f9107b036b1334f18ca8830bfff1295d21cfdb702103b287eaf122eea69030a0e9feed096bed8045c8b98bec453e1ffac7fbdbd4bb7152ae'
sec = bytes.fromhex(hex_sec)
der = bytes.fromhex(hex_der)
redeem_script = Script.parse(BytesIO(bytes.fromhex(hex_redeem_script)))
stream = BytesIO(bytes.fromhex(hex_tx))

tx_obj = Tx.parse(stream)
z = tx_obj.sig_hash(0, redeem_script)
point = S256Point.parse(sec)
sig = Signature.parse(der)
print(point.verify(z, sig))


# ### Exercise 5
# 
# Modify the `sig_hash` and `verify_input` methods to be able to verify p2sh transactions.
# 
# #### Make [this test](/edit/code-ch08/tx.py) pass: `tx.py:TxTest:test_verify_p2sh`

# In[9]:


# Exercise 5

reload(tx)
run(tx.TxTest("test_verify_p2sh"))

