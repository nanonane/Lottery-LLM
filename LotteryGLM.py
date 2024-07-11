import os
import moxing as mox

#拷贝chatglm2模型到chatglm2目录下
work_dir = '/home/ma-user/work'
chatglm_path = os.path.join(work_dir, 'chatglm2')

if not os.path.exists(chatglm_path):
    os.mkdir(chatglm_path)

    obs_path = 'obs://tongchenghao-pfs/gallery-models/chatglm2.tar'
    ma_path = os.path.join(chatglm_path, 'chatglm2.tar')
    mox.file.copy(obs_path, ma_path)

mox.file.copy_parallel('obs://modelarts-labs-bj4-v2/course/ModelBox/frpc_linux_amd64', '/home/ma-user/work/frpc_linux_amd64')