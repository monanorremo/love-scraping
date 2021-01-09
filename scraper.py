class JobScrape:

    def __init__(self, site_name):
        """Having the job sites in a list means we can check on initialisation and throw an error if the site is not available"""

        sites=[{"monster":{
                "url":
                "https://www.monster.com/jobs/search/",
                "query_format": "?q={keywords}&where={city}&cy={country}",
                "results":"#ResultsContainer",
        }}]

        self.site_data=[site[site_name] for site in sites if site_name in site][0]

        self.site_name=site.site_name
        print(self.site_data)
        print(self.site_name)

    def _format_monster():
        pass

    def _format_indeed():
        pass
    
    def _get_description():
        pass

    def _scrape_site():
        pass
    
    def get_jobs():
        pass
