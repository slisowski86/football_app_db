PGDMP     9    8    
            x            FootballStats    12.4    12.4     #           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            $           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            %           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            &           1262    16441    FootballStats    DATABASE     �   CREATE DATABASE "FootballStats" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Polish_Poland.1250' LC_CTYPE = 'Polish_Poland.1250';
    DROP DATABASE "FootballStats";
                postgres    false            �            1259    16485    clubs    TABLE     X   CREATE TABLE public.clubs (
    id integer NOT NULL,
    club_name character varying
);
    DROP TABLE public.clubs;
       public         heap    postgres    false            �            1259    16480    nations    TABLE     f   CREATE TABLE public.nations (
    id integer NOT NULL,
    nationality_name character varying(250)
);
    DROP TABLE public.nations;
       public         heap    postgres    false            �            1259    16454    player_score    TABLE     \  CREATE TABLE public.player_score (
    player_id integer NOT NULL,
    appearances integer,
    mins integer,
    goals integer,
    assists integer,
    yel integer,
    red integer,
    shots_per_game double precision,
    pass_score double precision,
    aerialswon double precision,
    man_of_the_match integer,
    rating double precision
);
     DROP TABLE public.player_score;
       public         heap    postgres    false            �            1259    16459    player_stats    TABLE     �   CREATE TABLE public.player_stats (
    player_id integer NOT NULL,
    perfdef integer,
    perfattack double precision,
    perfposs integer,
    total double precision
);
     DROP TABLE public.player_stats;
       public         heap    postgres    false            �            1259    16448    players    TABLE     �   CREATE TABLE public.players (
    id integer NOT NULL,
    name character varying(250),
    age integer,
    nationality_id integer,
    club_id integer
);
    DROP TABLE public.players;
       public         heap    postgres    false                       0    16485    clubs 
   TABLE DATA           .   COPY public.clubs (id, club_name) FROM stdin;
    public          postgres    false    206   p                 0    16480    nations 
   TABLE DATA           7   COPY public.nations (id, nationality_name) FROM stdin;
    public          postgres    false    205   �!                 0    16454    player_score 
   TABLE DATA           �   COPY public.player_score (player_id, appearances, mins, goals, assists, yel, red, shots_per_game, pass_score, aerialswon, man_of_the_match, rating) FROM stdin;
    public          postgres    false    203   �"                 0    16459    player_stats 
   TABLE DATA           W   COPY public.player_stats (player_id, perfdef, perfattack, perfposs, total) FROM stdin;
    public          postgres    false    204   B7                 0    16448    players 
   TABLE DATA           I   COPY public.players (id, name, age, nationality_id, club_id) FROM stdin;
    public          postgres    false    202   �C       �
           2606    16492    clubs Clubs_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.clubs
    ADD CONSTRAINT "Clubs_pkey" PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.clubs DROP CONSTRAINT "Clubs_pkey";
       public            postgres    false    206            �
           2606    16458    player_score Player_Score_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.player_score
    ADD CONSTRAINT "Player_Score_pkey" PRIMARY KEY (player_id);
 J   ALTER TABLE ONLY public.player_score DROP CONSTRAINT "Player_Score_pkey";
       public            postgres    false    203            �
           2606    16463    player_stats Player_Stats_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.player_stats
    ADD CONSTRAINT "Player_Stats_pkey" PRIMARY KEY (player_id);
 J   ALTER TABLE ONLY public.player_stats DROP CONSTRAINT "Player_Stats_pkey";
       public            postgres    false    204            �
           2606    16452    players Players_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.players
    ADD CONSTRAINT "Players_pkey" PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.players DROP CONSTRAINT "Players_pkey";
       public            postgres    false    202            �
           2606    16484    nations nations_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.nations
    ADD CONSTRAINT nations_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.nations DROP CONSTRAINT nations_pkey;
       public            postgres    false    205            �
           1259    16504    fki_club_foreign    INDEX     G   CREATE INDEX fki_club_foreign ON public.players USING btree (club_id);
 $   DROP INDEX public.fki_club_foreign;
       public            postgres    false    202            �
           1259    16498    fki_nations_key    INDEX     M   CREATE INDEX fki_nations_key ON public.players USING btree (nationality_id);
 #   DROP INDEX public.fki_nations_key;
       public            postgres    false    202            �
           2606    16499    players club_foreign    FK CONSTRAINT     }   ALTER TABLE ONLY public.players
    ADD CONSTRAINT club_foreign FOREIGN KEY (club_id) REFERENCES public.clubs(id) NOT VALID;
 >   ALTER TABLE ONLY public.players DROP CONSTRAINT club_foreign;
       public          postgres    false    2713    202    206            �
           2606    16493    players nations_key    FK CONSTRAINT     �   ALTER TABLE ONLY public.players
    ADD CONSTRAINT nations_key FOREIGN KEY (nationality_id) REFERENCES public.nations(id) NOT VALID;
 =   ALTER TABLE ONLY public.players DROP CONSTRAINT nations_key;
       public          postgres    false    202    2711    205            �
           2606    16505    player_score player_foreign    FK CONSTRAINT     �   ALTER TABLE ONLY public.player_score
    ADD CONSTRAINT player_foreign FOREIGN KEY (player_id) REFERENCES public.players(id) NOT VALID;
 E   ALTER TABLE ONLY public.player_score DROP CONSTRAINT player_foreign;
       public          postgres    false    2703    203    202            �
           2606    16510 !   player_stats player_stats_foreign    FK CONSTRAINT     �   ALTER TABLE ONLY public.player_stats
    ADD CONSTRAINT player_stats_foreign FOREIGN KEY (player_id) REFERENCES public.players(id) NOT VALID;
 K   ALTER TABLE ONLY public.player_stats DROP CONSTRAINT player_stats_foreign;
       public          postgres    false    2703    204    202                .  x�MU]w�8}�
��`?iH7�MC�����`� K�,�¯�+H��5�htg��UJ�W�#&4�-gf�3{����Y~ֶݹ��"�[uR�9ߊ�f7�䍲�%��N)��Q�uJ���q/*�>bc�����m�� jZ)�"M�ř��p=g��A���4�ֳ6�E:���x�4��Vo�"��n4F��q{�FtiI_Ûnv"��"�q���Iq�m'Қ���r�(&	͂QA7N>p�u+&)�NΊ	j�eوI/��b����]�>�74�ML
��� ��:��{1)�qx��x�\)}8�NL���k�h�2�h���ʸ����~�7K跲:�u�$U�`3�Nd)=0�!?%�	=�W�g�e��v"�Q�S���r���IEV�jl]�
�r�< dhڽ\x����:�8X���q4���j�]ȅ;(��.#�5��S�ҳ��@��r�={V��'
}f+�����3����"ϯA��,~t�����K���N��m��V�^��o�h�C9;"���9�FgYɵ��-RZ(��(&��F�F�1��:^xV���r� I��Ey4AQL�F]�str�����_�R�½Mv6ɹ6v�L��`�J�JulQ�r3��<X��_@q@�x���2��q���g�M���X�ɞ���a���%���bX��KQ�Qcw�JY��ȇOK��qb���v^�!t�[LSzQs&1M}�d^�c�W2��4�^	��8D����/�[�v�c������l�h��qطW<S�%k{�I!�`�q���bZ�*�W�UB(0��4[�)��&�q��h���9-E�����*�����8�+�E�*L ����݉��0_Q��c�F�i��Ђ\*�c!��n�+8Z�� j4N�I\��2F+/�4V�U<�5�P���:���?X�U#�@�D�.��(j@p�U5��Y�de�3�Q����k�6n�]}��>D�L�z��tu��)��IT��.*t��ބV��AH�N�AAS� B�c��*��'�FAIh����MXSZ�� Dc&Ӥc��w ƨ��ܻ>�/ޒ�F�R(�|��( ������!�zp{ā�ߍ-�7l�2�ʾvcx`G����j�L�.��x�#&���b)�'��P�E�5�C��y�������cj�� ��Q�!�'�3�X�E�9;�n�D�8aC6�����	�����������i��{l^�s��ȴ�3�ch"��X^�I7X��S)�}���g�a�	I_�2mTZX%�j�?m�9��x�T�;��d]܍��(ُ���$)`@�ޡ�J��I�/_�v�         �   x�%�AO�0������%����`�!Mܸx�E�I�&����n����{~�IR�%���X�����5�p�I~p	�)���	���E��˼Z�S�PP^��/�,�f��p��1��8P���pHw��$GM��1�%���'4���|e��[�pp��h4S�죚��X�Q��������i �Zx�A{�
6BW���%���j5I���,m[7�
>K�7c�ő�O��ΣZ�            x�m[Y�����X�=�f�����& J�,��*;}���#@�����T˳kO}�S���_��:������Yӓ�1���3
��c���'�����\�%|9��_���o�����Ku_�|�9�Gv�����zr��2��W2�������c� ��Ly�򝰛����������?4�l,�͸Z������[���"�o>������Q�%��S'�8�K6����R�yKJ��̗��3
��b�ko��Ш�؏�/���ʞ������a���f�ߵ�+.W�ꫴ��a�\��,��Wv9������2HM.��WhO���V�bnGWo�b~	��F�-�x���V^���R��K���d�M�E�Pj��}�>���o��d�j��7�5a:
�� ��ե6ܠw?��믻su�ĳ��\���g}��Zz�_5�Jasx�Xo.T����/xY9�1�\�?	[�'���|�F�`���8y�u{:��E��~��*jZ.\�b7�
u�N�"�����������+%=%v���@ȝ���+%83�������׽�;˺q��;zJ���m��ތvn��"u�*�ٝ��XHBT��(�z"rk�"�Z�3+��	Ϳ�Z�$1|�1��Տ�>��X��5��B�-�;��;
:F�q���%D����d��-4=8F�ׂ����+q;�=�l�)q3����B���z�D;-xOm��#��cg��r�LX({��{;FK?:���"�eU�Y<4�S7n���[���
O\���r=�t�^���4���7�v��lL]Iy����?�h�z;B3v�#D�~A�����v�L�~�Yݤ�iFFX�F�vU�ū«E��Í~����2O�u.�"/de��z��Q�ay]?�y깙��*mpA
�yudW��~�f9�P5J���T�ʚΕ������שG5�\���+C3�7/�O�H���}��ʤߑ�lG�p-7Eg�~����1FF���4
De�4�M�o�\z��UH��.��c�ܕ���5+���v�tI��yHB*���ۡ��э�>��w5a��r�<@��[Ih^�ҁ�g;�շ�=߯QC��(�D5�,5��T*��S�Q�B�9���C	��Rr�w�j&c+l�P��k�I�D��/�FHR^�WG
+Q,!�*X��PK��ż����ft�A���o?�U�/ԨF��;�)hTVih�w&����Ρ����J��	�*_]G��')���r�wR�mķ#,�OFdb��o9���X2������a��xc����0<p�l��)����L�_�`a�g�~+ ���)LD
�w)m�suYkH�]���˪~�s���zX�q��s-H�d�os�.�Bߩ���,����Rs_JB2��J�/ �s)G�&ʳ���yX[W�
wG��82DX�� �G��w���  ���Ve�&�>�	:F�ٹX�.e���	�%� �����F�,/Ss)���g�;��>	�?�G�6��ڟ����/J���7����bZxϴ�B���;�H��$�d�����t�$]]pjM��{�e�!��!`[s�@n��Ӟ�}a|E�s+�$���������ۑs!�����)�U�����* �����2Opo38�������}k�$�̰���4g�'6?��f�5�y]�|�5��ܮA��=	K7~s?p:�FĘ w#��C��([.(e�T��wnVV>�E";8N;�񮁮@�AM��E��0�)W6�p�����;êp��o (w.7�S�ls��O�v���~�.:�O&"�Q�h�4x�f�X�7�0H0p��G�Y8_�}���O/)?G�976\�+w��W<oвc�rg^�������@dȣ 5N&��b��*:z%�|�0��L��4��G��J,YqO����~#3�G�XĠY�*I�*�.�%����VY�p���rI�]��	W��!1"i����t����O�j�4�ռ1	�:]��]w���[���\l(���u
��g�Ga�#��n��A��'89�U�*��`�f#�@��
��#�,�Jq�u_])d�?`���(��l��T/4�6Ə����NR��?������T��à>i�iU�X����!���}��A���ԷB��Zd9 <��re�ɯП)��**s͋ٿF���lV��ZK�:S�ވ�	=ԉZ7uM��nX�Wp����LW	~*Ak�Mڢ:�sd�
�}�ZA��+JZ]�8ꤪ�ژ^sT����+ڶ��2�e��ZNZ�s&fUY�]	@mp��o�d?`G��)r,��^D��HI�H�T��F���N^��@�㞑�C�]�.����4.��o��
��K��KNo�c��p�{Lߝ�C�������c�����K��w\�PAG������IQo��A��f9f���Į�)�W��荥u��o�u�N���e�R��~j����B���������$�Q��6�;[��֓"ɡ��C��=�Wh�p��_a��)C�^l:W9;~WN\O��<����Z��.����Cib�6>;|��o◷T�Y�uN�i�϶ �:n%�R��5:,�d�e������쭆�\lh[��m+�����t�f縉���T��2mx����×m�-)�R�#U����J�|Rgk�'�3j��v5f�j��&�l�;TRV�CiW�CA=EU+�Fް����d���$���t���I�^x�֯8̨�-�PQ\����R��VƗ�q�)��p0�-����d��H��&ڹk�X\��+����Q��)c*å8���.'�\�Ԃ��q�1�v��xi%�8_�o�N��h����@*Q�m�޷3f��|N=�p'\��D=M�mhO{���3��������3�Z�4$�BiD����+,����e:dd��R�=ۧ־���8޳��-�b@^��鵓�ij���G8��V�9� ��l��%t
#/LT�P��::� �(���%T�����W숍�𱵟���<?'h�`��W�gWU�F��ĶO�?u��|��Y�M�É�>��[��j�2��'��eUӌ�p�D�sP����G.� �<��58(�}�B�QLVo���!att!�a゘����D�� 8��?R�D���kރ���Az�wDA���ˬ=ZN�,�����r�)��d_������BC��O��/�M���(���ȹY=�	�*��.19�/�_sn�����k�]ĔM;1��̯
��T�4\ۤ6$�q��Q��uƶF�|����:vm�'�6��G��*��ܬ~��5%V^��E����C��U.��pu2ZR׏1�����L�@x_a!�k�CI�ˢ?ӳ[�EQ���Ϲgƛ-&�p4q22��!�Ƨo�������j�UO����O����34A�O��#�N���T<�k��r;�U���]���5q�B��UK�8�Ut1�¢)�Z8�Qc=NF(��-Ii*���M���b.�b9ğY�텪,L[�.��E��9���������Z�L�^t ��\���9��w�]t�T��M���=%@�M4���h��q`�xeꑯ�P������l�"����J�=����$��S�`F��m��Z�k&w�8��g(gF��]�oj���^t�qZۡ�g�h6���+_2����Y��GfwU�T��Ի����:H� -F����hS��r�:�|�֮���ni�C�ծE�O{��{o�B����<�R4��7z��Z�L;��������d�ocb����#�6��#��:��-��6sZM��u��5UEu���}?��9"u�(y]�X��~ޒY���rp��p��h����ң����}Q3���>3�5G�4,U7�dhl��qf��D�a#zܸ���������m|���|�K=pԐ��� 6c5�oҔv�V/�~�A/��f��C�#j΄���])�R	��-"CH`D�"8�E/>�;v�,ϛ�7���#��g��i��=���Q*K�ɷ�r�S��w�K����)Յd����@��R:�cG�����7��� �  L>3�i;j�����N�i�T�Wt�-x�7��qS�g?� 1cײ�Q�s<���=��p���Ӎ4p�yP��jE���\����{����=���|�aʉQO&��5��I�!��G�S��uq����?<�ο2S�0��s��� u�#�r�{ǹ�	6P��wGMF�5�����t*��Ie��.tݕX�j�x�L�/j ���vJU��2����[k Sȵ�7�������%a'T¾3HlB���\H��Y9eZr�F�^�?�m��zım)��a�:W_�Sz]oI���r4V�W��-I�����~�C~��1t�y�-U��-<�� ���0"� di8Y<����.�����  ��P�z�x~.j~P�*���Z*2L����8q�{k�y��0�0�a�OG"�U �~A��R��{�d�˵[}��!���:�nb����ߢ�U>��.c�)��-)�(<�h 5$���qo��}Ɲ��U9�� �ɡ���b�j�F�qu<���!�'@�@�v�i�ZQL������#���z#��!]v�,<�	����ў�39��u�:r��L/`�&<�#e^��g��&f0�~����3�������v!�ܢK�5��O;	B���9_Kq��=yw0\����)izL��ɷ��n�*���#���ċt���%�Vn�.�el�g�'��e�_AYb�̝�3ν��"��W���B;�	�:�9s-r��	�RWp<�
9�@���PLE�c�x��˿��eѪ�������g��G� ���:��oD�����G9ӆ�� "��2�I��e;��5~r����Řί�N�Ê�m� ��Q�[ ����T��r�2b�btk��`*�ΝzY��WN�d�C�4��)4U��9yU�oV��P�^��*U�	��y�T�Ҩ�����FɄ�)�S��V�;E��k=�qAn*=�t��^3H��z����9}��:���%��v�d�̹Y�k�E��[$xh:�,d�����gۤM���c�s��JLK_mǿ�8�24D�HF�w�x/�q6�\�+��K�hQT�tֱX��?��.`ޡ�h�(����<r�*mz*�|��A	e�9t�}og����T�����G���u���2.�3Q~�Ѻ����}��e��B         Q  x�E�[��8�Ż�L|Sw���c�CٶfS��,>�@ �n}]w�W�[O��:�uԷ���5���u�g�[ߓ�ɬ��>��Y��p�{gVg�rAc��]�5�sk_��~�֮���j�u�;�{<~;�zstic]�}���z=6�eڽ��N��l�tF�'_oo�|�w����f����z�[�{�v�V��:&��uxP{c����b��:m��_��7CL<�(���;p�~k�	�a����r#���3�K���q�朇�cxvo�䙫���yنkV��N�f�����^Z�=�U�5z��b���e����\�l^���;��JP��^Vn07��]�3K��6�b��v����pϛ�il㫻d��\U�4�{����ƺ^\��>q� ��u��h���zD`e�3������a�q<�	z�Ն��- pg�r�#.��쫳E}�����۬]:w��0��0|�
^Ɗ7z��˫�`�͑�q?v7�.@W�6c+lS�O�R�r��gB�&G�Q�>�?�7j-S#p�ocڣ��^F&�j���e׆��Z��>�c�ӷ��_��p��HPc��8�����e6[D�74�8:e䪗m��-@@@p��M�%��������P���	C�hr£^`�5C�oU<Vga��vY��qg�ڸjo���P�.�֙�j�����
�A׬��;N�.ء�G����#��Ӆs1Nq"(n�n��|��/w�ƽL�M���N���.R奉��E�<��[��寔*�T��4��J�Ȍ0�P��dK�O�#L�����@�~�}�H���)1(d�S��m��?)Z�3���]������$T�K'B�3�'o��Ug9��_&����$uP���ƨ��LԲs������/��l�γʪ���z��+\�$�s�� No�z|�z�#.05��f�q)�ɣ�y���~���4Q�ũ�v��U�Ƙ_�w�L���h���f��kv��10Pg�V���^�����oHM\Msד0뚊�fs��l`�-Obvc��L*��p�܀ëy����Py|�d��76�.��o:!�[{o�v�Y�����x�	�,����k1:_d��s{���Cs~��bK0k�8�����BdKD�0����6���Ȋ����j �{��a�7\p���*�nc�G�]ޕ�ƕ<Y͠XԐ��t�!^��٤��Mxf7qr����)�'?�p YZ{Ӹ��<ߊ��
�6��4���tIJ�r1KJ_�<����R��wu�� �*]�4�/z�$E��.�n�c6`�d�J��/�#��}gDl	�xBt��c�b�$#������Qg�$	U���4��u'�fDY�$�*�&z,Ћ��$�_���q�aQr��wM~	@��I/�0&�T��S���m�2$�j�\2Y��/F�0��z��t�����!�\ޔ����#�1Q��9Y��V�ds��\c�t(���: �x��mfI
Oj�1���G����]�%�m��r"��h#U���5 �&K�K�Dש8���z+$.�N�/Wq�"Cy��Y�s!K�Չ؞)�7eE>7��^���K���8�*a3��3�����=�����)X[BW�7-�i@&`k�eN�! �HRw
+�'i�<w�ۄE�_��'y�_Tno4��r�VV�ĵ<v2n}:�����໻[�̨�e�,�-�FF�B
�:ZI�&�2>�YV���u�
�p�N�1KJ[�J�d+3�$��V-�b/� ���\� �8g@@zwS�[v%��_�";7c@2	)�j<*�n����22RÂ��@1��Z��%K���T��������q��Z�A6��M��r^�2�0
��C0d1�D��ğO�k�(p��*-O3��d��<�(�;+�눬i�ʇ�A�Ys���؇�sn�O�_�S�J�	��)�,tkW�7�gvN��F��E��VR%�"Q�&u�z�����
N���܋� ��+��_~�$T4�n;���/)tN��e��풷�DS?������ʱX>���|��CT@����`��"?��ٜ�Z�x���`����I(�|X��W���D1�u�Q&Ć�N�(}V3ay��B���R��D[<O���R�1��dbo'pw�����Ī�\���O�����n������i���s����ݔoa�;3>N/��9Km"p��L@��MF�T];G�/4h�;�	�2a���.�[�90C7���=��Gh)3��D�k�O��k���7�Kh �������)9���~��ȳʧ�xd��f2Q=ii���?���HK������*Ld��Zb`����Q�,*��f4���T����VV��b�!�%�Zo���DZ$lQd�EL�_�������g��u�VOE�ڬR��1~r�{3Jz!,�4�$�e���^q>����>BK�L��m��[��6g�nQ����"�"F�ԚnL�'��aJ;I��;|�5�}�~Ŭ�M���2�`��4Q�����cg�b���>��d��bJ�"Z����'�����p����X�����)�i��D.�*���l�'))-���UU��b5��H1�^�JѬA|���攣/�7����CP��0~q���Z��rɛK��Fܧ����}�f|�f�o�:�U�"啰9S)�+F�)�>�����g�i�D�7��:����O�r�l��ՠg��%��U��+�Қ0�l�p�c�'��.^z�mwd�q���G��#
$�J���c��M�<c�b�ю�Ż}�:[:7�0��g�7LS!!Ǭ���Z���@z�����i+��]�Ӿl:���z&����̵�i��q��'D�ɸ�X�#�$z�I�4�X
t�|��9)(�k��3k�����ñ��|YDy��W|�|�in���V���"ߡ�=�$sUk�eG��������Y�
�֒&�p@$a�[V!��v;{pB�9w�>Wy�P�؇�{F�U������&��XxJ���ǧ?lJcIϒR6�ڎ��D�&��e�˿�܊@Kk7=�TU�Oԯ���$��K���V};a����������Q;[ʊ����R���            x�MZ�r�8�]�_�ݬ���&�~T�U���S}��n 	aR�������$H�S���Ʉ#u������U��HEA��Zۛ��Zwk��S�8HԵ��m�o�QwNűJT��V�	�6��Jb��L=�n�z�³��AŹ��u�nt�����Y��[��w�A����:~[O��<[�R=����³}��zTq$�W8hx3}x�ڵ�w*^���J=R��ڹ���k��*YA�<�"�h�Aw[݇wv�ݻݨ8Q�*�(Vw���]x;�n�h�R�A��׍� �t��:�RU�������'mhYҐ� �ԝmM��lm�*�H����ܿ[�u��JEq��WS���_Qa��� *�O�i�[��0^�(�J]���Mx��a�u�呰C�?]��𦛶��	y ��{3�w��xcM��"���u?���[�6�ch,WanLԓY�n���YJhVQDɹ�ۇ篺ǽ\[����@ȭ���}�0��2�i��s�w����t	�U,}֍j�W�5�=|J����*����ڶ؉���7V����m+��QA��{��fjM/�+H"���L�E�2D�� ��q/�j�uÜY �-bO��<HRu��Ύ��ֺђ_�ܟ��-�gMG�*jP'Hru;m�s�k���K83H�S���k���TA� )�%r�H�MC��󼪂M!������;2���
�%HW�O��}x��w��N�!&O#uiR�����30v\c퍶5�@���q��	�)��[^��~����C� ��}k� ��M��H܆���6�u�Ɓ+�b���!�h�X\��0BɅ�[\ut��8��J]��)��F�}	�l�0�w���ڮ�p<�$I�E��m��c�Y��	��G��v�9.~-�,��w=G�Q\$rf)C��7��ͻ��� �;-����I��G�C!���� ��xZ���P ��k��n�� �Y�U�yy1=��]�/ZҖ�J�|Ep1��C��^̓<R�[�S��ZOw����x���%XW.Oԝ��.[ |g�wP�8�S�>�Q�l��P�8w�O�"�}�!<�L�%K��@��҄w��n%"9�T��6�[�i.B(�=�
x���~x��XFРX��M}��8ԓ>X�1$(�"�Qb�;�Ym@�rλ������V��
&�9Q��D#��*�X "���s}x�����mɒ�E�.�W�4lͨ�@6�B �UP���j�m�W�(�&*�|@_-�RI�D%Fx�77��Q�(p�},��-�Q�ԃ���S?jV��r�QPF�w��֟F��|bHe���� ��o=��̩4	�D�54L�7#E�%�ac�|����&:(� ݼÍ�Д&-s������"y\�����5�{�X>��g����[ˋX� �e�!D.���O1��Z)ؾEȝ��f�4����>��;�����%��>|�UV��+�z��B!<�T���y�[�\<U&5`e���zj��6��h��zZ�JVZp� �Ë��F���	jf��4H��E���5��Q�>E�i�j�~� �hHN?�DxПU��z�C�Q q�r1����wmg�	�[�D�J��@a0.�O�d~�J}��������<pG�7��~��k�fc�"i�2[p�4�<lU��� ��q��g�X�a��I��JmI��
^�Q���9��P��ԕv@0@d����,�眏��{ך��&%"pĺ�h�Ֆ��¼#xA�<��&3s��P�R�t֮���s5��9�=�ƼR����X.(Օ�6i}5aT�X\�!!�/;��s��"`�3��<���E�\wf'B��4rD������f&�%�)51�i�PRg�g���,ݚ~���*˰��:�2��g �n�E)�����m/�\�ư��@��r�ο����'3�ղ�Gg�N�.F�Y��z��q䜌����V��!`�R0\�	ʆ�B>�Z�F�5��uTN*�������q*c�!Y �ܼj#�Ϸ �D�9�of=g_�+ޘ7����GtK��iϢTF��H�:f*��B&� W��p�{:o�a�@Q|�j�n��c��
)3�7�ܟ��� k(��§ڂ�h�
�'�d������*�{O��K��s�f'X'��g����`�?Zԛ�i4o� �9������9��
�K�
��q�&Av���>�
/���d�?���$˩ٗ�	WM��6�l�H�}}a�l�s�)X$H��G��N��C"��z�}O�n�^#��VG~�=wk_ #����6�\� h��V��-�R��`��~�НAXV*�D���I}ȟ�J@]���������%�4�~���v�/���_PH����n�?�ܜ{cJ���k}�f6#��}0�s"�G�< ��($�@����Aq7�/�`Ý�[����f<6z֣@Ȁd���lF��$%�s0��ٵ���p��۠�CJ6X�q��
�>'��%m}ʢ�i�6�즱�R����x���� {��w*jI�DPD��Ѿ���"�.`*�h�b�2�o������w�����߃,ڳ��F���,��T�6�f�lͬ�-#;�-$1]G�!�נ�ҭ<N�× ����T��/f>P�:����C�y���t��гZ���)�b��v�~�]x6������P
���:='�������B�n���9g>$[��g#Sq�'���6�W�#W(��#��f��5�Ɣ���f�Ez��(�`l?���R�E ��~�;V��?GK�e*!�*{0�=��_;��~���d���� ���tki�K$�����>5%����g"���<�P���d�Dȃj��	��ܧ�x�8�n�z-�Dګ��)�运�O;�Oh��c!"��P�v��o�����yZY�7�[��� &�腬��� Yz��o9�J-K�$;\~i9�E���!��o�ː�����`ۯ��'���R��
k��ֶ��S�f�J��WX✒�Uk�y��-`9�n"^�R�N�RU�E�@�ǝFoTom���5b�x,0o&p�)�Tt*~����[�T�c�e��mO�"k��S�k�n����phc����M���ԋ^���5Zz����U~�7t���YodZ�-�gh02{ԛ7�_�E5���=����d����Em��hq��?{���J��p����i��[�T�b��n@�C%���g�(}��r5=�ϪB�¬߬ �ihk"�TQ�BG���i&�\'2������]{ �n9�f(�����0ڳ��དྷ����ԗ�@Ay��tT-r�;�[W��M	�[�A,����/.#$�F�AB�B�
���,�:�3���͹�k�d)�Dy�Cg� ��i�$��<�A����j>�z�w�E �(E���q���|�,S�9f����Ium�x� �Y��~k^���F��[/1����eD����4�$
r_��/�OۣF.�(�ʤߴS��o�����ɼ��؝�ksS�����nW{��.�W�_��@���f�i�M@Lj�艑�э7U����8�`�f.��:�AO���E�-��ג�y(K���IQ.����ZO�����<���~�k���`�gC�"А�p�4�
:�����C2F�ݚq��F(ܺ�q���#���!�Rwz7����j�$��u��I����4�$!��Z�Z���=[�g�T�O�#�%���}{�,N�����ä��ռ/CJ5'�x�k�{���'��w����у'w!;AI� ���-�d�ꁑ".7�KSOR2 /��c>	ɻJ���O������o�����f�X����2tb�?m��xF�p/�mI�Q�O�y%�Ԉ#�4�"�a��"YZk�~$�A�g �����(�T��T�8+���镆�/4b�=���ՙ��؝sϝ���������]�e��(�R�j�-�a��Kh��"�lS�	�?�K����r�9?�0� ��lR0�sR>̣{���`E��uNz{JPJn�g��|ѣ [  ���2e�d{����
�Ѯ��L&e�FT�GmV'm@R�'��[���-E�QJ{>�����Q��F�ָE�_ӲY��8�ϤzI�j���"� љ� ��l�1�@��NU�˱�s?�`���c<��?����M�����f
K����'RHD��d��u~~� �Х�IB��g'����oPvyv`|�"Z<á�{��驪��[7���H�����̝�u�5�)����Bql͆����Ώ�$M�kQ�%�ݺ���J������	��i%)���.�N�7�-�%-��*߼��7� ����%��o�>w/�Dc���/�u>�Gr�P�,U���ڷѬ�]��
�%�@q5�'Gj��ۜ��sInc5�q�Όux�vo�V k�
k3�q ?3a��1tG�jiV���%K��	yώ���Z�
�B���N�7��R�dK��8oi/�0D|̍8�9��e7]�K�\�c��ԜF�{���ܠX�Nx����u~	������\w�t���&m����@x��R����	U���x)egh�T���
�<������P�Abs&�VY��" {v�J5��@��v;wdđ~�k�tkZ�BE*�����M�V^[乸�jR�R=k;�Iw6����"�!Y	ks��sKq�lH�`��#�Ȟ��RAj��٤����f� ��l#f�`�Iu���`��H����[���L���<�M�.��(Á����C�u#J��[�t��P�-�{�8�I�h,�H�&q�߬���B5?p?���!Μ��j����m]�9�_T�8`���S��A�m�%^~�A?���'�(A���m��o_����i��O����9�ܗͳ�g��p{DB,����{�&�����4�Y7���Kʭ�����Ҝ���f	�ݯ�L@�m����q���B"!�@z���,�=�'���F�u��^^�ɛf�������vm��
~��ѵ|3��^Y\?P���q�����;O:���z,���R�d@������\�+�iî/�0�7+�����>�ݸ������� ��}�Ώ,�#KĿ3�Nd��[3�)S�F���O����X     