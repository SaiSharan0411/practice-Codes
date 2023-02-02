<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="AD_Rotator.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
        <p>
            &nbsp;</p>
        <p>
            &nbsp;</p>
        <p>
            <asp:AdRotator ID="AdRotator1" runat="server" AdvertisementFile="~/XMLFile1.xml" OnAdCreated="AdRotator1_AdCreated" style="z-index: 1; left: 431px; top: 207px; position: absolute; height: 125px; width: 242px" />
        </p>
        <p>
            &nbsp;</p>
        <p>
            <asp:FileUpload ID="FileUpload1" runat="server" style="z-index: 1; left: 357px; top: 420px; position: absolute; width: 407px" />
            <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" style="z-index: 1; left: 609px; top: 518px; position: absolute" Text="Submit" />
            <asp:Label ID="Label1" runat="server" style="z-index: 1; left: 521px; top: 91px; position: absolute" Text="boobs"></asp:Label>
        </p>
    </form>
</body>
</html>
