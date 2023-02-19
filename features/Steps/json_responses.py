import trafaret as t

contactSearchData = t.Dict({
    t.Key('contacts'): t.Dict({
        t.Key('id'): t.String,
        t.Key('direct_link'): t.String | t.Null,
        t.Key('first_name'): t.String,
        t.Key('last_name'): t.String,
        t.Key('company_name'): t.String,
        t.Key('information'): t.String,
        t.Key('is_shared'): t.String,
        t.Key('created_at'): t.List(t.Dict({})),
        t.Key('updated_at'): t.String,
        t.Key('contacts'): t.Dict({
            t.Key('id'): t.String,
            t.Key('label'): t.String | t.Null,
            t.Key('value'): t.String
            }),
        t.Key('phone_numbers'): t.Dict({
            t.Key('id'): t.String,
            t.Key('label'): t.String | t.Null,
            t.Key('value'): t.String
            })
        }),
    t.Key('meta'): t.Dict({
        t.Key('count'): t.Int,
        t.Key('total'): t.String,
        t.Key('current_page'): t.String | t.Null,
        t.Key('per_page'): t.String,
        t.Key('next_page_link'): t.String | t.Null,
        t.Key('previous_page_link'): t.String
     })      
})
