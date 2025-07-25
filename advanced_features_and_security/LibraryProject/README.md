# Permissions and Groups Setup in advanced_features_and_security

This project implements a custom user model and leverages Django's built-in permission and group system for granular access control.

## 1. Custom Permissions in Models

Custom permissions are defined within the `Meta` class of the `Article` model in `blog/models.py`. These permissions control actions on `Article` instances.

- `blog.can_view_article`: Allows viewing of articles.
- `blog.can_create_article`: Allows creation of new articles.
- `blog.can_edit_article`: Allows editing of existing articles.
- `blog.can_delete_article`: Allows deletion of articles.

## 2. Groups and Assigned Permissions

Groups are created and managed via the Django admin interface (`/admin/`). The following groups are set up with specific permissions:

- **Admins:**
    - `blog.can_view_article`
    - `blog.can_create_article`
    - `blog.can_edit_article`
    - `blog.can_delete_article`
    (Full control over articles)

- **Editors:**
    - `blog.can_view_article`
    - `blog.can_create_article`
    - `blog.can_edit_article`
    (Can view, create, and edit articles, but not delete)

- **Viewers:**
    - `blog.can_view_article`
    (Can only view articles)

To set up:
1. Log in to Django admin as a superuser.
2. Navigate to "Groups" under "AUTHENTICATION AND AUTHORIZATION".
3. Add the groups ("Admins", "Editors", "Viewers") and assign the specified permissions.

## 3. Enforcing Permissions in Views

Permissions are enforced in `blog/views.py` using Django's `@permission_required` decorator for function-based views.

- `@permission_required('blog.can_view_article', raise_exception=True)`: Protects `article_list` and `article_detail` views. If a user doesn't have this permission, a 403 Forbidden error is raised.
- `@permission_required('blog.can_create_article', raise_exception=True)`: Protects `article_create` view.
- `@permission_required('blog.can_edit_article', raise_exception=True)`: Protects `article_edit` view.
- `@permission_required('blog.can_delete_article', raise_exception=True)`: Protects `article_delete` view.

For class-based views, `PermissionRequiredMixin` can be used (commented out examples in `blog/views.py`).

Templates also use `{% if perms.app_name.permission_name %}` to conditionally display links based on user permissions (e.g., Edit/Delete links on `article_list.html` and `article_detail.html`).

## 4. Testing

To test the permission system:
1. Create new users (e.g., `viewer@example.com`, `editor@example.com`, `admin@example.com`) via Django admin.
2. Assign these users to their respective groups (`Viewers`, `Editors`, `Admins`).
3. Log in as each user and verify that they can only perform actions allowed by their assigned group's permissions. Attempts to perform unauthorized actions should result in a "403 Forbidden" error.