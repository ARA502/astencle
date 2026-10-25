import streamlit as st
from PIL import Image, ImageOps, ImageFilter

st.set_page_config(page_title="مُولد الاستنسل الذكي", page_icon="🎨", layout="centered")

st.title("🎨 مُولد الاستنسل ورسومات الشعار الذكي")
st.write("ارفعي أي صورة أو شعار، وحوليها فوراً إلى رسم استنسل فني عالي التباين بخطوط عريضة وواضحة!")

# خيارات التحكم الجانبية
st.sidebar.header("إعدادات التعديل والتحكم")
threshold = st.sidebar.slider("مستوى عتبة التباين (Threshold)", 50, 200, 128)
blur_level = st.sidebar.slider("نعومة وتلطيف الحواف", 0, 5, 1)

# رفع الصورة
uploaded_file = st.file_uploader("اختر صورة للرفع (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # فتح الصورة الأصلية
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("الصورة الأصلية")
        st.image(image, use_column_width=True)
    
    # معالجة الصورة وتحويلها إلى استنسل أبيض وأسود
    # 1. تحويل الصورة إلى تدرج الرمادي (Grayscale)
    gray_image = ImageOps.grayscale(image)
    
    # 2. تطبيق فلتر النعومة إذا وجد
    if blur_level > 0:
        gray_image = gray_image.filter(ImageFilter.GaussianBlur(blur_level))
    
    # 3. تطبيق خوارزمية التباين الثنائي (Black & White Stencil)
    fn = lambda x: 255 if x > threshold else 0
    stencil_image = gray_image.point(fn, mode='1')
    
    with col2:
        st.subheader("رسم الاستنسل الناتج")
        st.image(stencil_image, use_column_width=True)
    
    st.success("✨ تم معالجة الصورة بنجاح وتحويلها لستايل الاستنسل المطلوب!")
