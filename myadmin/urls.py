from django.urls import path, include
from .views import login
from .views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', login.admin_login, name="adminLogin"),
    path('adminlogout/', login.logout, name="adminlogout"),
    path('home/', home.dashboard_admin, name="dashboard_admin"),
    path('country/', home.country_view, name="country"),
    path('addcountry/', home.post_country, name="addcountry"),
    path('updatecountry/<int:id>', home.edit_country, name="updatecountry"),
    path('deletecountry/<int:id>', home.delete_country, name="deletecountry"),
    path('state/', home.state_view, name="state"),
    path('addstate/', home.post_state, name="addstate"),
    path('updatestate/<int:id>', home.edit_state, name="updatestate"),
    path('deletestate/<int:id>', home.delete_state, name="deletestate"),
    path('city/', home.city_view, name="city"),
    path('addcity/', home.post_city, name="addcity"),
    path('updatecity/<int:id>', home.edit_city, name="updatecity"),
    path('deletecity/<int:id>', home.delete_city, name="deletecity"),
    path('degree/', home.degree_view, name="degree"),
    path('adddegree/', home.post_degree, name="adddegree"),
    path('updatedegree/<int:id>', home.edit_degree, name="updatedegree"),
    path('deletedegree/<int:id>', home.delete_degree, name="deletedegree"),
    path('admintc/', home.cms_tc, name="admintc"),
    path('addtc/', home.add_tc, name="addtc"),
    path('updatetc/<int:id>', home.edit_tc, name="updatetc"),
    path('deletetc/<int:id>', home.delete_tc, name="deletetc"),
    path('adminpolicy/', home.cms_privacy, name="adminpolicy"),
    path('addpolicy/', home.add_policy, name="addpolicy"),
    path('updatepandp/<int:id>', home.edit_policy, name="updatepandp"),
    path('deletepandp/<int:id>', home.delete_policy, name="deletepandp"),
    path('admiusers/', home.users_view, name="admiusers"),
    
    path('admininquiry/', home.inquiry_view, name="admininquiry"),
    path('deleteadmininquiry/<int:id>', home.delete_inquiry, name="deleteadmininquiry"),

    path('adminentry/', home.admin_view, name="adminentry"),
    path('addadminentry/', home.add_admin, name="addadminentry"),
    path('updatedminentry/<int:id>', home.edit_admin, name="updatedminentry"),
    path('deleteadminentry/<int:id>', home.delete_admin, name="deleteadminentry"),
    path('aboutus/', home.aboutus_view, name="aboutus"),
    path('addaboutus/', home.add_aboutus, name="addaboutus"),
    path('updateaboutus/<int:id>', home.edit_aboutus, name="updateaboutus"),
    path('deleteaboutus/<int:id>', home.delete_about, name="deleteaboutus"),
    path('header/', home.header_view, name="header"),
    path('addheader/', home.add_header, name="addheader"),
    path('updateheader/<int:id>', home.edit_header, name="updateheader"),
    path('deleteheader/<int:id>', home.delete_about, name="deleteheader"),
    path('footer/', home.footer_view, name="footer"),
    path('addfooter/', home.add_footer, name="addfooter"),
    path('updatefooter/<int:id>', home.edit_footer, name="updatefooter"),
    path('deletefooter/<int:id>', home.delete_footer, name="deletefooter"),
    path('editprofile/', home.edit_profile, name="editprofile"),

    path('newscategory/', home.news_category_view, name="newscategory"),
    path('addnewscategory/', home.add_news_category, name="addnewscategory"),
    path('updatenewscategory/<int:id>', home.edit_news_category, name="updatenewscategory"),
    path('deletenewscategory/<int:id>', home.delete_news_cat, name="deletenewscategory"),

    path('news/', home.news_view, name="news"),
    path('addnews/', home.add_news, name="addnews"),
    path('updatenews/<int:id>', home.edit_news, name="updatenews"),
    path('deletenews/<int:id>', home.delete_news, name="deletenews"),

    path('blogcategory/', home.blog_category_view, name="blogcategory"),
    path('addnblogcategory/', home.add_blog_category, name="addnblogcategory"),
    path('updateblogcategory/<int:id>', home.edit_blog_category, name="updateblogcategory"),
    path('deleteblogcategory/<int:id>', home.delete_blog_cat, name="deleteblogcategory"),

    path('blog/', home.blog_view, name="blog"),
    path('addnblog/', home.add_blog, name="addnblog"),
    path('updateblog/<int:id>', home.edit_blog, name="updateblog"),
    path('deleteblog/<int:id>', home.delete_blog, name="deleteblog"),

    path('educat/', home.edu_category_view, name="educat"),
    path('addneducat/', home.add_edu_category, name="addneducat"),
    path('updateeducat/<int:id>', home.edit_edu_category, name="updateeducat"),
    path('deleteeducat/<int:id>', home.delete_edu_cat, name="deleteeducat"),

    path('edusubcat/', home.edu_sub__category_view, name="edusubcat"),
    path('addnedusubcat/', home.add_edu_sub_category, name="addnedusubcat"),
    path('updateedusubcat/<int:id>', home.edit_edu_sub_category, name="updateedusubcat"),
    path('deleteedusubcat/<int:id>', home.delete_edu_sub_cat, name="deleteedusubcat"),

    path('edusub/', home.edu_subjects_view, name="edusub"),
    path('addnedusub/', home.add_edu_subjects, name="addnedusub"),
    path('updateedusub/<int:id>', home.edit_edu_subjects, name="updateedusub"),
    path('deleteedusub/<int:id>', home.delete_edu_subject, name="deleteedusub"),

    path('educh/', home.edu_chapter_view, name="educh"),
    path('addneduch/', home.add_edu_chapter, name="addneduch"),
    path('updateeduch/<int:id>', home.edit_edu_chapter, name="updateeduch"),
    path('deleteeduch/<int:id>', home.delete_edu_chapter, name="deleteeduch"),

    path('edu/', home.edu_view, name="edu"),
    path('addnedu/', home.add_edu, name="addnedu"),
    path('updateedu/<int:id>', home.edit_edu, name="updateedu"),
    path('deleteedu/<int:id>', home.delete_edu, name="deleteedu"),

    path('ajax/edusubcat', home.load_edusubcat, name="ajax_load_edusubcat"), # AJAX
    path('ajax/edusubjects/', home.load_edusubjects, name="ajax_load_edusubjects"), # AJAX
    path('ajax/ajax_load_educh/', home.load_educhapters, name="ajax_load_educh"), # AJAX

    path('gallerycat/', home.gallery_category_view, name="gallerycat"),
    path('addgallerycat/', home.add_gallery_category, name="addgallerycat"),
    path('updategallerycat/<int:id>', home.edit_gallery_category, name="updategallerycat"),
    path('deletegallerycat/<int:id>', home.delete_gallery_cat, name="deletegallerycat"),

    path('gallery/', home.gallery_view, name="gallery"),
    path('addgallery/', home.add_gallery, name="addgallery"),
    path('deletegallery/<int:id>', home.delete_gallery, name="deletegallery"),
    path('deleteallgallery/', home.delete_all_gallery, name="deleteallgallery"),

    path('slider/', home.slider_view, name="slider"),
    path('addslider/', home.post_slider, name="addslider"),
    path('updateslider/<int:id>', home.edit_slider, name="updateslider"),
    path('deleteslider/<int:id>', home.delete_slider, name="deleteslider"),

    path('teacher/', home.teacher_view, name="teacher"),
    path('addtecher/', home.post_teacher, name="addtecher"),
    path('updateteacher/<int:id>', home.edit_teacher, name="updateteacher"),
    path('deleteteacher/<int:id>', home.delete_teacher, name="deleteteacher"),

    path('tag/', home.tag_view, name="tag"),
    path('addtagr/', home.post_tag, name="addtag"),
    path('deletag/<int:id>', home.delete_tag, name="deletag"),

    path('ebookcat/', home.ebook_category_view, name="ebookcat"),
    path('addebookcat/', home.add_ebook_category, name="addebookcat"),
    path('updateebookcat/<int:id>', home.edit_ebook_category, name="updateebookcat"),
    path('deleteebookcat/<int:id>', home.delete_ebook_cat, name="deleteebookcat"),

    path('ebook/', home.ebook_view, name="ebook"),
    path('addebook/', home.add_ebook, name="addebook"),
    path('updateebook/<int:id>', home.edit_ebook, name="updateebook"),
    path('deleteebook/<int:id>', home.delete_ebook, name="deleteebook"),

    path('exportuser/', home.export_user, name="exportuser"),
    path('exportinquiry/', home.export_inquiry, name="exportinquiry"),

    path('report/', home.report_view, name="report"),
    path('search/', home.generate_report, name="search"),
]