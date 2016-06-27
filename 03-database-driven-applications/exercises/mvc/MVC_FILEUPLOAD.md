
###Upload And Save a File to the Database
##Learning Objectives
* Create a view that displays all of the documents in the database table and order by upload date.
* Give the user and opportunity to upload a new file and give the file a name.
* Create the ability to download the file.

##Bonus
* Limit the type of files the user can upload to a particular type of file like jpeg, pdf, or excel.
* Add a foreign key to another table in your database and display some data from both tables. 

##Steps
* Create a table in your Chinook or Zoolandia database that fits this definition:
```
CREATE TABLE [dbo].[Document] (
    [DocumentId]   INT             IDENTITY (1, 1) NOT NULL,
    [Title]        VARCHAR (100)   NOT NULL,
    [Contents]     VARBINARY (MAX) NOT NULL,
    [FileName]     VARCHAR (200)   NOT NULL,
    [UploadDate]   SMALLDATETIME   NOT NULL,
    [UploadUserId] VARCHAR (100)   NOT NULL,
    PRIMARY KEY CLUSTERED ([DocumentId] ASC)
);
```
* Create a new asp.net mvc application by choosing file/new project/ asp.net web application. When the next screen displays choose "Empty" then check the box for "MVC".
* Create the DbContext class and the model you will need for the "Document" database table.
* Add your connection string to the web config.
* Add a new controller called "Document".
* Make sure your "Route.Config" file points to the controller called "Document" and the action called "Index".
* Your are going to need a view model class to specify the data needed to display on the view. It need to look like this:
```
  public class DocumentDetailsViewModel
    {
        public int DocumentId { get; set; }
        public string Title { get; set; }
        public string FileName { get; set; }
        public byte[] Contents { get; set; }
        public DateTime UploadDate { get; set; }
        public string UploadUserId { get; set; }
        public List<Document> Documents { get; set; }
    }
```
* Go to the action called "Index" in your controller. Add an attribute above the action, that will indicate that this action will get data rather than post.
 
```
   [HttpGet]
```

* Within your index action you need to create an instance of your DBContext and write a linq query that gets all the data from the 
"Documents" table and orders them by upload date.
* Create an instance of the DocumentDetailsView Model and populate the Documents property with the results of your query. 
* Pass view model to the index page. 
* Your code should be similar to this:

```
 using (var dbContext = new MyStoreContext())
            {
                var docs = (from d in dbContext.Document
                           orderby d.FileName
                           select d).ToList();

                DocumentDetailsViewModel vm = new DocumentDetailsViewModel()
                {
                    Documents = docs
                };
                return View(vm);
```
* Create the index view by right clicking on the name of the action result called "Index" and add a view. Accept the defaults when prompted
* Add to the top of your index view 
 ```
 @model YourApp.ViewModels.DocumentDetailsViewModel
 ```
 *Add the following to your index page to indicate that this page will post data and a file to the controller.
 
 ```
 @using (Html.BeginForm("Index", "Document", FormMethod.Post, new { enctype = "multipart/form-data" }))
{ 

 ```
 * Add a closing bracket at the end of the page.
 * Add the following to give users the ability to upload files
 ```
   <label for="file">File Upload:</label><br/>
    @Html.Label("File Name:   ")@Html.TextBoxFor(model=>model.Title)
    <input type="file" name="file" id="file" /><br><br>
    <input type="submit" value="Upload File" />
    <br><br>
 ```
 * Create a table to display the data, we don't have data yet and won't until we add the functionality to upload.
 * Add another action in your controller called index. Give the action and attribute of [HttpPost]
 * This action will accept a file and a view model when the page is posted.
 ```
 [HttpPost]
        public ActionResult Index(HttpPostedFileBase file, DocumentDetailsViewModel docViewModel)
        {
 ```
* Once again create an instance of your db context.
* Add the following code, we will discuss what it is doing later. 
```
 using (var dbContext = new MyStoreContext())
            {
                if (file != null && file.ContentLength > 0)
                    try
                    {
                        if ((file != null) && (file.ContentLength > 0) && !string.IsNullOrEmpty(file.FileName))
                        {
                            string fileName = file.FileName;
                            string fileContentType = file.ContentType;
                            byte[] fileBytes = new byte[file.ContentLength];
                            file.InputStream.Read(fileBytes, 0, Convert.ToInt32(file.ContentLength));

                            Document doc = new Document()
                            {
                                Title = docViewModel.Title,
                                FileName = fileName,
                                Contents = fileBytes,
                                UploadDate = DateTime.Now,
                                UploadUserId = "dtinsley91@gmail.com"
                            };
                            dbContext.Document.Add(doc);
                            dbContext.SaveChanges();
                        }

                        ViewBag.Message = "File uploaded successfully";
                    }
                    catch (Exception ex)
                    {
                        ViewBag.Message = "ERROR:" + ex.Message.ToString();
                    }
                //go back to index and the new doc should show

                var docs = from d in dbContext.Document
                           orderby d.FileName
                           select d;

                DocumentDetailsViewModel vm = new DocumentDetailsViewModel()
                {
                    Documents = docs.ToList()

                };
                return View(vm);
            }
```
* Build and run your application, see if your upload button uploads a file.
* Now we need to create a link for downloading documents. 
* Go to your view and modify the cod ein the <td> tag that contains the document title to be an action link that will call the FileDownload action in the Index controller.

```
 @Html.ActionLink(item.Title, "FileDownLoad", "Document", new { @documentId = item.DocumentId }, null)
 
```
* Add an action to your controller called "FileDownload". it will have a document Id passed to it.   
* The code in your action should look something like this:

```
 using (var dbContext = new MyStoreContext())
            {
                var fileId = documentId;

                var myFile = dbContext.Document.Find(documentId);

                if (myFile != null)
                {
                    byte[] file = myFile.Contents;
                    var cd = new System.Net.Mime.ContentDisposition
                    {
                        FileName = myFile.FileName,
                        // always prompt the user for downloading, set to true if you want
                        // the browser to try to show the file inline
                        Inline = true,
                    };
                    Response.AppendHeader("Content-Disposition", cd.ToString());
                    return File(file, System.Net.Mime.MediaTypeNames.Application.Octet);
                }
                else return null;

            }
```

