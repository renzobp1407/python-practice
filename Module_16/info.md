## API

Often we start learning coding because we want to do something with code. For example, you might want to download a list of your sales from Shopify and put them in a spreadsheet. Or you might be looking to search through Twitter and count how many times your website has been shared by people. You may want to do these things every night, and therefore writing some code to help you is going to save you a lot of time in the long run.

This is where APIs come in.

An API is a program that accepts data from you, and gives you data back. For example, Twitter has an API.

This API accepts data (your search terms) and returns data (the tweets that match the search terms).

Twitter's API can also accept other things, such as a username, and return the user's information.

These APIs are usually designed to allow you to retrieve information that the website holds in a more program-friendly way. Instead of loading the website, you can just get the data you're interested in.

At the end of the day, websites are there for people to use. You may use the Twitter website to gain access to Twitter's data. It is displayed in a nice way so that you'll enjoy using the site and come back to it. Programs don't need niceness, so when you're interacting with an API all the program gets back is the raw data. Something like this:

code example:

```API
{
  "tweets": [
    {
      "body": "Learning #Python today with @TecladoCode!",
      "user": "Phil Best"
    },
    {
      "body": "We've just put out a new #Python course, going from beginner to expert. #LearnPython",
      "user": "TecladoCode"
    },
    {
      "body": "Writing some code to search the Twitter API for cat images. So far just getting back dog images though... :thinking:",
      "user": "Rolf Smith"
    }
  ]
}
```

-------------------------------------

pages for API
https://openexchangerates.org/

