This contains all the changes that i need to update on the reporting bot :
1. I've added the Upload ECG Button on the ecg allocation page.
2. I've added the Non-Reportable button and logic on the Ecg logic.
3. I've added the redundant code on the upload ecg logic which i need to fix asap.
5. I've not added the Report Format logic yet which needs to be updated from the pdf-fixing project.


-- 23 Oct 24 :
I'm adding the urgent button here for testing purpose, it is required in the orthanc reporting bot i.e. production.
These are the changes in it :
## ECG :
1. updated the patient details model : added the "urgent" boolean field in it.
2. added a path in the urls.py file as update_urgent_status_ecg.
3. added a view for handling the urgent status.
4. Changed the patient ordering on the allocation view.
5. in the ecg allocation view also, i've modified the sorting by updating it's respective view.
6. on ecg allocation html template, i've added two css for urgent labelling and background and i've added the respective class in the patient data and a span in the patient id.
7. on allocation template, added the js code , and the respective th and td.

## Xray :
1. Updated the DicomData model, and then migrated the data.
2. added the path in urls.py file.
3. added the view for handing the urgent case as update_urgent_status_xray.
4. in the allocation1 template, i've added the js code and the respective th/td data.
5. in the xrayallocation page, i've added the css and the urgent label along with the conditioning the class and adding  the span in the id in the td.
6. on xray allocation page, i've modified the sorting by updating it's respective view.
7. Changed the patient ordering on the allocation1 view also.
-- Himanshu Jangid.