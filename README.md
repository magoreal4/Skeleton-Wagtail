# Skeleton-Wagtail

Welcome to the Skeleton-Wagtail repository! This project serves as a skeleton for Wagtail projects, integrated with the power of Tailwind CSS and Vite for a modern and efficient development experience.

## Features

- **Wagtail**: A popular and flexible Django content management system.
- **Tailwind CSS**: A utility-first CSS framework for rapidly building custom user interfaces.
- **Vite**: A build tool that aims to provide a faster and leaner development experience for modern web projects.

## Getting Started

1. Clone the repository:
   
   ```bash
   git clone https://github.com/magoreal4/Skeleton-Wagtail.git
   ```

2. Rename the directory:
   
   ```bash
   mv Skeleton-Wagtail myproject
   cd myproject
   ```

3. Create a virtual environment named `.venv`:
   
   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment:
- On Windows:
  
  ```bash
  .venv\Scripts\activate
  ```

- On macOS and Linux:
  
  ```bash
  source .venv/bin/activate
  ```
5. Install the required Python packages:
   
   ```bash
   pip install -r requirements.txt
   ```

6. Apply migrations to set up your database schema:
   
   ```bash
   python manage.py migrate
   ```

7. Create a superuser for the Wagtail admin interface:
   
   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:
   
   ```bash
   python manage.py runserver
   ```

9. Open your browser and navigate to `http://localhost:8000/admin` to access the Wagtail admin interface using the superuser credentials you just created.
   
   If the background of the initial page at `http://127.0.0.1:8000` appears yellow, then Tailwind is functioning correctly.

##### Tailwind

To run Tailwind:

```bash
python manage.py tailwind start
```

### Vite

To run Vite within the `home/src` directory, navigate to `home/src` install npm and execute `npm run vite`:

```bash
cd home/src
npm install
npm run vite
```

This will start the Vite server, allowing you to see real-time changes as you work on the files within the `home` directory.

## Configuration

- Tailwind configuration can be found in `tailwind.config.js`.

- Vite configuration can be found in `vite.config.js`.
  
  **Note**: To work with live reload, you can run `vite`, `tailwind`, and `runserver` in separate terminals.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. Any contributions are greatly appreciated!

## License

This project is open-source and available under the MIT License.
