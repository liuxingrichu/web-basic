web����������ɲ��֣�
��1��html ����
    1��һ�������ʶ�����
    2��������Ա
        ��Ҫ����html����
        ������̨���г���
            --��дhtml�ļ�����ģ�����ã�
            --���ݿ��ȡ���ݣ��滻��html�ļ�ָ��λ�ã�Web��ܣ�
    3�����ز���
        ��ʽһ��ֱ�����������
        ��ʽ����Pycharm�򿪲���
    4����дhtml�ļ�
        --doctype��Ӧ��ϵ
        --html��ǩ����ǩ�ڲ�����д���ԣ��ñ�ǩ����дһ��
        --ע�ͷ����� <!-- ע�͵����� -->
    5����ǩ����
        �Զ��պϱ�ǩ(�Ƚ���)
            <meta charset="UTF-8"/>
            <br />
        �����պϱ�ǩ
            <title>�����ڶ�</title>
    6 head��ǩ
        <meta /> ���롢��ת��ˢ�¡��ؼ��֡�������IE����
            <meta http-equiv="X-UA-COMPATIBLE" content="IE=IE9;IE=IE8;"/>
        title��ǩ
        <link />��ͼ�꣬Ƿ
        <style /> ��CSS
        <script>Ƿ
    7 body��ǩ
        &nbsp;�ո�&gt;����&lt;С��
        h��ǩ������
        p��ǩ������
        br��ǩ������ 
        ��ǩ���ࣺ
            ���ڱ�ǩ
                span���װ壺���������ԣ�
            �鼶��ǩ
                h��ǩ���Ӵ�Ӵ֣���p��ǩ������֮���м�ࣩ��br��ǩ��
                div��ǩ���װ壩
            ���ַ�����
                chrome����� �Ҽ�-��Ԫ�����-������Ŵ�ͼ��-���ƶ�������鿴
                    �÷�ʽ�������ڶ�λԪ�ء��鿴��ʽ��
        ��ǩ֮�����Ƕ��
        ��ǩ���ڵ���˼��
            ���㶨λ��������CSS������JS����
        chrome���Ԫ��
            ���㶨λ�Ͳ鿴��ʽ
        inputϵ�� + form��ǩ
            type="text"     ��name��value����
            type="password" ��name��value���� 
            type="button"   ��value����
            type="submit"   ��value����
            type="radio"    ��value��checked����һ������name���ԣ�name��ͬ�򻥳⣩
            type="checkbox" ��value��checked���ɶ������name���ԣ�name������������ȡ���ݣ�
            type="file"     ����form���е�enctype="multipart/form-data"����
            type="reset"    ����
            <textarea>Ĭ��ֵ</textarea>    ��name����
            select��ǩ       ��name���ԣ��ڲ���option value��size������ʾ��multiple��ѡ�ж���
        a��ǩ�����ύ����̨��
            ʹ�ó�����
            ��1�������ӣ�ʵ�ֵ�ת
            ��2��ê��ê�� href="#ĳ��ǩ��ID" ע����ǩID�����ظ�
        img��ǩ���ԣ�
            src     ͼƬ��Դ
            title   ��ʾ
            alt     ͼƬ�Ҳ���ʱ����ʾ�ַ�
        �б��ǩ
            ul  ���ģʽ
                li 
            ol  ����ģʽ
                li 
            dl
                dt  ����
                dd  ����
        table����ǩ
           thead    ��ͷ
                tr  ��
                    th  ��
           tbody    ������
                tr  ��
                    td  ��
           colspan='n'  ���ںϲ�n����Ԫ��
           rowspan='n'  ���кϲ�n����Ԫ��
        label��ǩ
            �������ʱ��ʹ������id�ı�ǩ����ȡ���
            һ�����input��ǩʹ�� 
        fieldset��ǩ
            legend ���ɱ߿�
    8 get������post����������
    ��1��get��������������ݣ���䵽url�У�url���ڿ�����д���ݣ��ٷ��ŵ�����ˣ�
        post�������������ݣ���䵽body�У��ٷ��ŵ�����ˡ�
    ��2��get������post������������ݣ�������ͨ��ץ����ʽ����ȡ���ݣ�
        ���������ַ�ʽ����ȫ֮˵��
    ��Ҫ����20����ǩ����
    
��2��CSS  ����
    ��ɫ��λ��
    ��дCSS��ʽ��
    1. �ڱ�ǩ�ϣ�����style����
    2. head��ǩ�У���дstyle��ǩ
        -idѡ���������Ƽ�ʹ�ã�
            #i1{
                background-color:red;
                height: 49px;
            }
        - classѡ����
            .����{
               ...
               }
            <��ǩ class="����">xx</��ǩ>
        - ��ǩѡ����
            div{
                ...
            }
            ����div��ǩ�����ϴ���ʽ
        - �㼶ѡ����(�ո�)
           span div .c2{
                ...
           }
        - ���ѡ���������ţ�
            .c1 .c2 .c3{
                ...
            }
        - ����ѡ����
            ��ѡ�񵽵ı�ǩ����ͨ�����Խ���һ��ɸѡ
        PS��
            ���ȼ�����ǩ�ϵ�style���ȣ���д˳�򣬾ͽ�ԭ��������ȣ�
    2.5 css��ʽҲ����д��css�ļ���
        <link rel="stylesheet" href="commons.css"/>
    3.ע��
        /*
        xxx
        */
    4.�߿�
        ��ȡ���ʽ����ɫ��border��4px solid red��
        ��������
    5 ���ø�ʽ
        height               �߶� 
        width                ��ȣ����ء��ٷֱȣ�
        font-size            �����С 
        text-align:center    ˮƽ�������
        line-height          ��ֱ�������ݱ�ǩ�߶Ⱦ���
        font-weight          ����Ӵ�
        color                ������ɫ
    6 float
        ��ʵ�ֱ�ǩ�������鼶��ǩҲ���Զѵ�
        ����ǩ���Ƹ����ӱ�ǩ��
            <div style="clear:both;"></div>
    7 display
        display: none;      �ñ�ǩ����ʾ
        display: inline;    ת���ڱ�ǩ
        display: block;     ת�鼶��ǩ
        display: inline-block;
            ��ǩ�߱����ڱ�ǩ�����ԣ�ͬʱ�������ø߶ȡ���ȡ�padding��margin
        *���ڱ�ǩ
            �޷����ø߶ȡ���ȡ�padding��margin
        *�鼶��ǩ
            �����ø߶ȡ���ȡ�padding��margin
    8 �߾�padding margin
        �ڱ߾ࣺpadding
        ��߾ࣺmargin
        margin: 8px auto    ���У�auto�����ң�8pxΪ����
        margin: auto        �������Ҿ���
        
���������ص�عˣ�
1 �鼶��ǩ�����ڱ�ǩ
2 form��ǩ
    <!--�ϴ��ļ���Ҫʹ��multipart/form-data-->
    <form action="url���ύ�ĵ�ַ��" method="get" enctype="multipart/form-data">
        <div>�鼶��ǩ</div>
        <input  type="text" name="q"/>
        <input type="text" name="b"/>
        <!--�ϴ��ļ�-->
        <input type="file" name="f"/>
    </form>
    GET����������ƴ�ӵ�url��
        http://xxx?q=�û������ֵ
        http://xxx?q=�û������ֵ&b=�û����������
    POST��
        ����ͷ
        ��������
3 display
    block; inline; inline-block;
4 float
    <div>
        <div style="float:left;">�ӱ�ǩ</div>
        <!--����ӱ�ǩ��������������ǩ�ĳ���-->
        <div style="clear:both;"><div>
    </div>
5 margin: 0 auto;    ��߾�
6 padding   �ڱ߾ࣨ�����ű仯��

��3��JS   ��̬����

