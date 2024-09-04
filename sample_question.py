def count_email_domains(emails: list[str], urls: list[str]) -> dict[str, int]:
    """
    Given a list of emails and URLs, returns a dictionary of count of emails per URL domain.
    :param emails: list[str]: A list of emails to be mapped
    :param urls: list[str]; A list of URLs corresponding to domains
    :return emails_per_url_domain: dict[str, int]
    """
    emails_per_url_domain = {url:0 for url in urls}
    
    for email in emails:
        if email.count('@') != 1:
            continue
        domain = email.partition('@')[2]
        if (url := 'www.' + domain) in emails_per_url_domain:
            emails_per_url_domain[url] += 1
    
    return emails_per_url_domain

def main() -> None:
    emails = ['foo@a.com','bar@a.com' , 'baz@b.com', 'qux@d.com']
    urls = ['www.a.com', 'www.b.com', 'www.c.com']
    emails_per_url_domain = count_email_domains(emails=emails, urls=urls)
    print(f'{emails_per_url_domain = }')

if __name__=='__main__':
    main()
