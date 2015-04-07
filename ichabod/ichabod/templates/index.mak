<html>
<head>

    <meta charset="utf-8" />

    <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'> 
    
    <link rel="stylesheet" href="static/foundation/css/foundation.css" />
    <link rel="stylesheet" href="static/foundation/css/foundation-datepicker.css" />
    <link rel="stylesheet" href="static/foundation/css/foundation-datatables.css" />

    <link rel="stylesheet" href="static/foundation/css/foundation-icons/foundation-icons.css" />

    <!--<link rel="stylesheet" href="static/css/venter/jquery-iu-1.11.4.css" />-->
    
    <link href='http://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>

    <link rel="stylesheet" href="static/css/site.css" />
    
    <link rel="stylesheet" href="static/css/customers.css" />

    <style>
        
    </style>
    
</head>
<body>

    <div class="site-loading" id="site-loading">
        <div><h2>ichabod loading ...</h2></div>
    </div>

    <div class="site-wrapper" id="site-wrapper">
        <div class="row">
             <div class="large-2 columns side-bar visible-for-large-up">
                <h1 style="color: #008cba; text-align: center;">ichabod</h1>
                <ul>
                    <hr/>
                    <li><a href="#/home" id="pages-nav-home" class="size-24"><i class="step fi-home"></i> Home</a></li>
                    <hr/>
                    <li><a href="#/customers" id="pages-nav-customers" class="size-24"><i class="step fi-torsos-all"></i> Customers</a></li>
                    <li><a href="#/accounts" id="pages-nav-accounts" class="size-24"><i class="step fi-results-demographics"></i> Accounts</a></li>
                    <li><a href="#/contacts" id="pages-nav-contacts" class="size-24"><i class="step fi-address-book"></i> Contacts</a></li>
                    <li><a href="#/leads" id="pages-nav-leads" class="size-24"><i class="step fi-comment"></i> Leads</a></li>
                    <li><a href="#/opertunities" id="pages-nav-opertunities" class="size-24"><i class="step fi-comments"></i> Opertunities</a></li>
                    <li><a href="#/jobs" id="pages-nav-jobs" class="size-24"><i class="step fi-book-bookmark"></i> Jobs</a></li>
                    <li><a href="#/files" id="pages-nav-files" class="size-24"><i class="step fi-page-copy"></i> Files</a></li>
                    <li><a href="#/assets" id="pages-nav-assets" class="size-24"><i class="step fi-burst"></i> Assets</a></li>
                    <li><a href="#/reports" id="pages-nav-reports" class="size-24"><i class="step fi-graph-trend"></i> Reports</a></li>
                    <li><a href="#/settings" id="pages-nav-settings" class="size-24"><i class="step fi-widget"></i> Settings</a></li>
                    <li><a href="#/logout" id="pages-nav-logout" class="size-24"><i class="step fi-x-circle"></i> Logout</a></li>
                </ul>
            </div>
            
            <!-- Loading -->
            <div class="large-10 columns page" id="page-loading">
                <div class="row">
                    <div class="large-12 columns">
                        <h3>please wait ...</h3>
                    </div>
                </div>
            </div>
            
            <!-- Home -->
            <div class="large-10 columns page" id="page-home">
                <div class="row">
                    <div class="large-11 columns page-header"></div>
                    <hr/>
                </div>
                <div class="row page-contents">
                    <div class="large-12 columns">
                        hi.
                    </div>
                </div>
            </div>
            
            <!-- Customers -->
            <div class="large-10 columns page force-scroll" id="page-customers">
                <div class="row">
                    <div class="large-11 columns page-header"></div>
                    <hr/>
                </div>
                <div class="row top-padding">
                    <div class="large-1 columns dummy-column">.</div>
                    
                    <div class="large-10 columns">
                        <a href="#/customers/new" class="button">New Customer</a>
                        <!--<h4>Customers</h4>-->
                        <div id="page-customers-customer-list-container"></div>
                    </div>

                    <div class="large-1 columns dummy-column">.</div>
                    <div id="page-customers-new-customer-dialog" class="reveal-modal" data-reveal aria-labelledby="New Customer" aria-hidden="true" role="dialog"></div>
                </div>
            </div>
            
            <!-- Customer -->
            <div class="large-10 columns page force-scroll" id="page-customer">
                <div class="row">
                    <div class="large-11 columns page-header"></div>
                    <hr/>
                </div>
                <div class="row top-padding">
                    <div class="large-1 columns dummy-column">.</div>
                    <div class="large-10 columns">
                        <div id="page-customer-customer-info"></div>
                    </div>
                    <div class="large-1 columns dummy-column">.</div>
                </div>
            </div>
            
            <!-- Accounts -->
            <div class="large-10 columns page" id="page-accounts">
                <div class="row">
                    <div class="large-11 columns page-header"></div>
                    <hr/>
                </div>
                
                <div class="row top-padding">
                    <div class="large-12 columns">
                        hi.
                    </div>
                </div>
            </div>
            
            <!-- Contacts -->
            <div class="large-10 columns page" id="page-contacts">
                <div class="row">
                    <div class="large-11 columns page-header"></div>
                    <hr/>
                </div>
                
                <div class="row top-padding">
                    <div class="large-12 columns">
                        hi.
                    </div>
                </div>
            </div>
            
            <!-- Leads -->
            <div class="large-10 columns page" id="page-leads">
                <div class="row">
                    <div class="large-11 columns page-header"></div>
                    <hr/>
                </div>
                
                <div class="row top-padding">
                    <div class="large-12 columns">
                        hi.
                    </div>
                </div>
            </div>
            
            <!-- Opertunities -->
            <div class="large-10 columns page" id="page-opertunities">
                <div class="row ">
                    <div class="large-11 columns page-header"></div>
                    <hr/>
                </div>
                
                <div class="row top-padding">
                    <div class="large-12 columns">
                        hi.
                    </div>
                </div>
            </div>
            
            <!-- Jobs -->
            <div class="large-10 columns page" id="page-jobs">
                <div class="row">
                    <div class="large-11 columns page-header"></div>
                    <hr/>
                </div>
                
                <div class="row top-padding">
                    <div class="large-12 columns">
                        hi.
                    </div>
                </div>
            </div>
            
            <!-- Files -->
            <div class="large-10 columns page" id="page-files">
                <div class="row">
                    <div class="large-11 columns page-header"></div>
                    <hr/>
                </div>
                
                <div class="row top-padding">
                    <div class="large-12 columns">
                        hi.
                    </div>
                </div>
            </div>
            
            <!-- Assets -->
            <div class="large-10 columns page" id="page-assets">
                <div class="row">
                    <div class="large-11 columns page-header"></div>
                    <hr/>
                </div>
                
                <div class="row top-padding">
                    <div class="large-12 columns">
                        hi.
                    </div>
                </div>
            </div>
            
            <!-- Reports -->
            <div class="large-10 columns page" id="page-reports">
                <div class="row">
                    <div class="large-11 columns page-header"></div>
                    <hr/>
                </div>
                
                <div class="row top-padding">
                    <div class="large-12 columns">
                        hi.
                    </div>
                </div>
            </div>
            
            <!-- Settings -->
            <div class="large-10 columns page" id="page-settings">
                <div class="row">
                    <div class="large-11 columns page-header"></div>
                    <hr/>
                </div>
                
                <div class="row top-padding">
                    <div class="large-12 columns">
                        hi.
                    </div>
                </div>
            </div>
            
            <!-- Logout -->
            <div class="large-10 columns page" id="page-logout">
                <div class="row">
                    <div class="large-11 columns page-header"></div>
                    <hr/>
                </div>
                
                <div class="row top-padding">
                    <div class="large-12 columns">
                        hi.
                    </div>
                </div>
            </div>
            
        </div>
    </div>
    
    <script src="static/js/site.js"></script>

    <script src="static/foundation/js/vendor/jquery.js"></script>
   
    <script src="static/foundation/js/foundation/foundation.js"></script>
    
    <script src="static/foundation/js/foundation/foundation.dropdown.js"></script>
    <script src="static/foundation/js/foundation/foundation.reveal.js"></script>
    <script src="static/foundation/js/foundation/foundation.topbar.js"></script>

    <script src="static/foundation/js/vendor/modernizr.js"></script>

    <script src="static/foundation/js/foundation-datepicker.js"></script>
    
    <script src="static/foundation/js/vendor/jquery.datatables.1.9.4.min.js"></script>
    <script src="static/foundation/js/foundation-datatables.js"></script>
   
    <!--<script src="static/js/vender/jquery-ui-1.11.4.js"></script>-->
   
    <script src="static/js/TableMaker.js"></script>
 
    <script src="static/js/Pages.js"></script>
    
    <script>
        
    </script>
    
    <script src="static/js/pages/loading.js"></script>
    <script src="static/js/pages/home.js"></script>
    <script src="static/js/pages/customers.js"></script>
    <script src="static/js/pages/customer.js"></script>
    <script src="static/js/pages/accounts.js"></script>
    <script src="static/js/pages/contacts.js"></script>
    <script src="static/js/pages/leads.js"></script>
    <script src="static/js/pages/opertunities.js"></script>
    <script src="static/js/pages/jobs.js"></script>
    <script src="static/js/pages/files.js"></script>
    <script src="static/js/pages/assets.js"></script>
    <script src="static/js/pages/reports.js"></script>
    <script src="static/js/pages/settings.js"></script>
    <script src="static/js/pages/logout.js"></script>
   
    
    <script>
        $(document).foundation({
            dropdown: {
                // specify the class used for active dropdowns
                active_class: 'open'
            }
        });
        
        $(document).ready( function() {
            Pages.init({
                'page-title-element': 'h2',
                'site-div-id': 'site-wrapper',
                'site-loading-div-id': 'site-loading',
            }); 
        });
        
    </script>
    

</body>
</html>
