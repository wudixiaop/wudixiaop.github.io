Title: 在 Unity uGUI 中绘制圆形图片
Date: 2015-04-15 23:30
Category: 一点一滴
Tags: Unity3D

最近项目需要在 Unity 的新 UI 系统中实现圆形头像的功能，之前想通过 Mask 控件的方式来实现，但是一番努力后毫无头绪，只能祭上shader了。

大体的思路就是在一个空的 Object 上面挂上 RawImage 组件，组件的 Material 挂上本文中的 shader。截取的逻辑是选取图片正中心 (0.5, 0.5) 为圆的中心点，绘制图片在圆内的像素点为图片的像素，然后图片在圆外的像素点设置为 alpha 为 0 的点，
如 `(0, 0, 0, 0)`。逻辑是在 fragment shader 里面实现(shader 代码中的`frag`)。

下面直接放出 shader:

    :::shader
    Shader "Sprites/Circle"
    {
      Properties
      {
        [PerRendererData] _MainTex ("Sprite Texture", 2D) = "white" {}
        _Color ("Tint", Color) = (1,1,1,1)
        _Center("Center", vector) = (0.5, 0.5, 1.0, 1.0)
        _RadiusScale("Radius Scale", Range(0, 1)) = 0.5
        _HorizontalScale("Horizontal Scale", Range(0, 1.0)) = 1.0
        _VerticalScale("Vertical Scale", Range(0, 1.0)) = 1.0
      }

      SubShader
      {
        Tags
        {
          "Queue"="Overlay"
          "IgnoreProjector"="True"
          "RenderType"="Transparent"
          "PreviewType"="Plane"
          "CanUseSpriteAtlas"="True"
        }

        Cull Off
        Lighting Off
        ZWrite Off
        Blend One OneMinusSrcAlpha

        Pass
        {
        CGPROGRAM
          #pragma vertex vert
          #pragma fragment frag
          #pragma multi_compile _ PIXELSNAP_ON
          #include "UnityCG.cginc"

          struct appdata_t
          {
            float4 vertex   : POSITION;
            float4 color    : COLOR;
            float2 texcoord : TEXCOORD0;
          };

          struct v2f
          {
            float4 vertex   : SV_POSITION;
            fixed4 color    : COLOR;
            half2 texcoord  : TEXCOORD0;
          };

          fixed4 _Color;
          float _RadiusScale;
          float4 _Center;
          float _HorizontalScale;
          float _VerticalScale;

          v2f vert(appdata_t IN)
          {
            v2f OUT;
            OUT.vertex = mul(UNITY_MATRIX_MVP, IN.vertex);
            OUT.texcoord = IN.texcoord;
            OUT.color = IN.color * _Color;
            #ifdef PIXELSNAP_ON
            OUT.vertex = UnityPixelSnap (OUT.vertex);
            #endif

            return OUT;
          }

          sampler2D _MainTex;

          fixed4 frag(v2f IN) : SV_Target
          {
            fixed4 c;
            c = tex2D(_MainTex, IN.texcoord) * IN.color;

            // adjust center and horizontal/verital scale
            //
            float2 scale = (_HorizontalScale, _VerticalScale);
            float rs = length((_Center.xy - IN.texcoord.xy) / scale.xy);

            if(rs < 0.5 * _RadiusScale)
            {

              c.rgb *= c.a;
            }
            else
            {
              c = (0, 0, 0, 0);
            }

            return c;
          }
        ENDCG
        }
      }
    }


Github 地址： <https://raw.githubusercontent.com/wudixiaop/Nana/master/Shader/Sprite-Circle.shader>
