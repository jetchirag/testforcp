from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.loadWebsitesHome, name='loadWebsitesHome'),
    url(r'^createWebsite', views.createWebsite, name='createWebsite'),
    url(r'^listWebsites', views.listWebsites, name='listWebsites'),
    url(r'^modifyWebsite', views.modifyWebsite, name='modifyWebsite'),
    url(r'^deleteWebsite', views.deleteWebsite, name='deleteWebsite'),
    url(r'^siteState', views.siteState, name='siteState'),


    # Website modification url


    url(r'^submitWebsiteCreation', views.submitWebsiteCreation, name='submitWebsiteCreation'),
    url(r'^submitWebsiteDeletion', views.submitWebsiteDeletion, name='submitWebsiteDeletion'),
    url(r'^submitWebsiteListing', views.getFurtherAccounts, name='submitWebsiteListing'),
    url(r'^submitWebsiteModification', views.deleteWebsite, name='submitWebsiteModification'),
    url(r'^submitWebsiteStatus', views.submitWebsiteStatus, name='submitWebsiteStatus'),


    url(r'^getWebsiteDetails', views.submitWebsiteModify, name='getWebsiteDetails'),
    url(r'^saveWebsiteChanges', views.saveWebsiteChanges, name='saveWebsiteChanges'),


    url(r'^(?P<domain>([\da-z\.-]+\.[a-z\.]{2,6}|[\d\.]+)([\/:?=&#]{1}[\da-z\.-]+)*[\/\?]?)$', views.domain, name='domain'),
    url(r'^getDataFromLogFile', views.getDataFromLogFile, name='getDataFromLogFile'),
    url(r'^fetchErrorLogs', views.fetchErrorLogs, name='fetchErrorLogs'),


    url(r'^installWordpress', views.installWordpress, name='installWordpress'),
    url(r'^installJoomla', views.installJoomla, name='installJoomla'),
    
    url(r'^getDataFromConfigFile', views.getDataFromConfigFile, name='getDataFromConfigFile'),

    url(r'^saveConfigsToFile', views.saveConfigsToFile, name='saveConfigsToFile'),


    url(r'^getRewriteRules', views.getRewriteRules, name='getRewriteRules'),

    url(r'^saveRewriteRules', views.saveRewriteRules, name='saveRewriteRules'),

    url(r'^saveSSL', views.saveSSL, name='saveSSL'),


    url(r'^CreateWebsiteFromBackup', views.CreateWebsiteFromBackup, name='CreateWebsiteFromBackup'),

    ## sub/add/park domains

    url(r'^submitDomainCreation', views.submitDomainCreation, name='submitDomainCreation'),

    ## fetch domains

    url(r'^fetchDomains', views.fetchDomains, name='submitDomainCreation'),
    url(r'^changePHP', views.changePHP, name='changePHP'),
    url(r'^submitDomainDeletion', views.submitDomainDeletion, name='submitDomainDeletion'),

    url(r'^listCron',views.listCron,name="listCron"),
    url(r'^getWebsiteCron',views.getWebsiteCron,name="getWebsiteCron"),
    url(r'^getCronbyLine',views.getCronbyLine,name="getCronbyLine"),
    url(r'^remCronbyLine',views.remCronbyLine,name="remCronbyLine"),
    url(r'^saveCronChanges',views.saveCronChanges,name="saveCronChanges"),
    url(r'^addNewCron',views.addNewCron,name="addNewCron"),
  
]