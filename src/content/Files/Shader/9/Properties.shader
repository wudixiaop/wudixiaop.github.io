Shader "Custom/Properties" {
	Properties {
		_RangeType ("Range 类型", Range(0,1)) = 0.5
		_FloatType ("Float 类型", Float) = 1.0
		_IntType ("Int 类型", Int) = 1
		_ColorType ("Color 类型", Color) = (1, 1, 1, 1)
		_VectorType ("Vector 类型", vector) = (0, 0, 0, 0)
		_2DType ("2D纹理类型", 2D) = "while" {}
		_CubeType ("Cube 类型", Cube) = "black" {}
		_3DType ("3D纹理类型", 3D) = "gray" {}
		_RectType("Rectangle", Rect) = "" {}
	}

	SubShader {
		Tags { "RenderType"="Opaque" }
		LOD 200
		
		CGPROGRAM
		// Physically based Standard lighting model, and enable shadows on all light types
		#pragma surface surf Standard fullforwardshadows

		// Use shader model 3.0 target, to get nicer looking lighting
		#pragma target 3.0

		struct Input {
			float2 uv_MainTex;
		};

		void surf (Input IN, inout SurfaceOutputStandard o) {
			// Albedo comes from a texture tinted by color
			o.Alpha = (0, 0, 0, 0);
		}
		ENDCG
	} 
	FallBack "Diffuse"
}
