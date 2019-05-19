from todoapp.models import Todo
def gettodolist():
    record = Todo.objects.filter(visible_status = True).values('pk','title','Descriptions', 'created_at', 'updated_at', 'completion_date', 'status', 'visible_status')
    record_list =[{'title' : each_record.get('title'),
                  'Descriptions': each_record.get('Descriptions'), 
                   'created_at': str(each_record.get('created_at').date()), 
                   'updated_at': str(each_record.get('updated_at').date()), 
                   'completion_date': str(each_record.get('completion_date').date()), 
                   'status':each_record.get('status'),
                   'visible_status':each_record.get('visible_status'),
                    'pk': each_record.get('pk') } for each_record in record]
    return record_list