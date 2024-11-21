import streamlit as st
import svgwrite

class UserAppWireframes:
    def __init__(self):
        self.screen_width = 360
        self.screen_height = 640
        self.padding = 20
        self.colors = {
            'background': '#FFFFFF',
            'text': '#000000',
            'primary': '#007AFF',
            'secondary': '#666666',
            'border': '#C5C5C7',
            'surface': '#F5F5F5'
        }

    def create_base_screen(self, name):
        """Create base screen with iPhone frame"""
        dwg = svgwrite.Drawing(size=(self.screen_width, self.screen_height))
        
        # Phone frame
        dwg.add(dwg.rect(
            (0, 0),
            (self.screen_width, self.screen_height),
            rx=40, ry=40,
            fill=self.colors['background'],
            stroke=self.colors['border'],
            stroke_width=2
        ))
        
        # Status bar
        dwg.add(dwg.rect(
            (0, 0),
            (self.screen_width, 44),
            fill=self.colors['surface']
        ))
        
        # Notch
        dwg.add(dwg.rect(
            (self.screen_width/2 - 60, 0),
            (120, 30),
            rx=15, ry=15,
            fill='#333333'
        ))
        
        return dwg

    def add_nav_bar(self, dwg, title, show_back=True):
        """Add navigation bar to screen"""
        # Nav bar background
        dwg.add(dwg.rect(
            (0, 44),
            (self.screen_width, 44),
            fill=self.colors['background']
        ))
        
        # Back button if needed
        if show_back:
            dwg.add(dwg.path(
                d=f'M 20,66 L 35,58 L 35,74 Z',
                fill=self.colors['primary']
            ))
        
        # Title
        dwg.add(dwg.text(
            title,
            insert=(self.screen_width/2, 74),
            text_anchor='middle',
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
        ))

    def create_welcome_screen(self):
        """Create user welcome screen"""
        dwg = self.create_base_screen("welcome")
        self.add_nav_bar(dwg, "Welcome", show_back=False)
        
        # App logo
        dwg.add(dwg.circle(
            (self.screen_width/2, 180),
            50,
            fill=self.colors['primary']
        ))
        
        # Welcome text
        dwg.add(dwg.text(
            "Welcome to Ball Talk",
            insert=(self.screen_width/2, 280),
            text_anchor='middle',
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 24px; font-weight: 600'
        ))
        
        # Description
        dwg.add(dwg.text(
            "Connect with your favorite athletes",
            insert=(self.screen_width/2, 320),
            text_anchor='middle',
            fill=self.colors['secondary'],
            style='font-family: SF Pro Text; font-size: 16px'
        ))
        
        # Sign up buttons
        y = self.screen_height - 200
        buttons = [
            {'text': 'Continue with Email', 'primary': True},
            {'text': 'Continue with Social', 'primary': False}
        ]
        
        for button in buttons:
            dwg.add(dwg.rect(
                (20, y),
                (self.screen_width - 40, 50),
                rx=25, ry=25,
                fill=self.colors['primary'] if button['primary'] else 'none',
                stroke=self.colors['primary']
            ))
            dwg.add(dwg.text(
                button['text'],
                insert=(self.screen_width/2, y + 32),
                text_anchor='middle',
                fill='white' if button['primary'] else self.colors['primary'],
                style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
            ))
            y += 70
        
        return dwg
    def create_user_discovery_screen(self):
        """Create user discovery screen wireframe"""
        dwg = self.create_base_screen("discovery")
        self.add_nav_bar(dwg, "Discover")
        
        # Search bar
        y = 108
        dwg.add(dwg.rect(
            (20, y),
            (self.screen_width - 40, 44),
            rx=22, ry=22,
            fill=self.colors['surface']
        ))
        dwg.add(dwg.text(
            "Search athletes, leagues...",
            insert=(50, y + 28),
            fill=self.colors['secondary'],
            style='font-family: SF Pro Text; font-size: 15px'
        ))
        
    # Filter chips
        y += 64
        filters = ['All', 'NBA', 'NFL', 'MLB']
        x = 20
        for filter_text in filters:
            width = len(filter_text) * 10 + 30
            dwg.add(dwg.rect(
                (x, y),
                (width, 32),
                rx=16, ry=16,
                fill=self.colors['surface'] if filter_text == 'All' else 'none',
                stroke=self.colors['border']
            ))
            dwg.add(dwg.text(
                filter_text,
                insert=(x + width/2, y + 20),
                text_anchor='middle',
                fill=self.colors['primary'] if filter_text == 'All' else self.colors['text'],
                style='font-family: SF Pro Text; font-size: 13px'
            ))
            x += width + 10
    
    # Featured Athletes
        y += 60
        dwg.add(dwg.text(
            "Featured Athletes",
            insert=(20, y),
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
        ))
    
    # Artist grid
        y += 20
        for i in range(4):
            dwg.add(dwg.rect(
                (20, y + i*120),
                (self.screen_width - 40, 100),
                rx=8, ry=8,
                fill=self.colors['surface']
            ))
            # Artist avatar
            dwg.add(dwg.circle(
                (60, y + i*120 + 50),
                30,
                fill='#E5E5EA'
            ))
            # Artist info
            dwg.add(dwg.text(
                f"Athlete Name",
                insert=(100, y + i*120 + 40),
                fill=self.colors['text'],
                style='font-family: SF Pro Text; font-size: 15px; font-weight: 600'
            ))
            dwg.add(dwg.text(
                "NBA • Detroit Pistons",
                insert=(100, y + i*120 + 60),
                fill=self.colors['secondary'],
                style='font-family: SF Pro Text; font-size: 13px'
            ))
        return dwg

    def create_playlist_screen(self):
        """Create playlist creation screen"""
        dwg = self.create_base_screen("playlist")
        self.add_nav_bar(dwg, "Create Playlist")
        
        # Playlist name input
        y = 108
        dwg.add(dwg.text(
            "Playlist Name",
            insert=(20, y),
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 15px'
        ))
        dwg.add(dwg.rect(
            (20, y + 10),
            (self.screen_width - 40, 44),
            rx=8, ry=8,
            fill='none',
            stroke=self.colors['border']
        ))
        
        # Track selection
        y += 84
        dwg.add(dwg.text(
            "Add Tracks",
            insert=(20, y),
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 15px'
        ))
        
        # Track list
        for i in range(5):
            dwg.add(dwg.rect(
                (20, y + 20 + i*60),
                (self.screen_width - 40, 50),
                rx=8, ry=8,
                fill=self.colors['surface']
            ))
            # Track info
            dwg.add(dwg.text(
                f"Track {i+1}",
                insert=(40, y + 45 + i*60),
                fill=self.colors['text'],
                style='font-family: SF Pro Text; font-size: 15px'
            ))
            # Add button
            dwg.add(dwg.circle(
                (self.screen_width - 45, y + 45 + i*60),
                15,
                fill=self.colors['primary']
            ))
            dwg.add(dwg.text(
                "+",
                insert=(self.screen_width - 45, y + 50 + i*60),
                text_anchor='middle',
                fill='white',
                style='font-family: SF Pro Text; font-size: 20px'
            ))
        
        # Create button
        dwg.add(dwg.rect(
            (20, self.screen_height - 80),
            (self.screen_width - 40, 50),
            rx=25, ry=25,
            fill=self.colors['primary']
        ))
        dwg.add(dwg.text(
            "Create Playlist",
            insert=(self.screen_width/2, self.screen_height - 45),
            text_anchor='middle',
            fill='white',
            style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
        ))
        
        return dwg
    def create_engagement_screen(self):
        """Create user engagement screen wireframe"""
        dwg = self.create_base_screen("engagement")
        self.add_nav_bar(dwg, "Community")
        
        # Tab bar
        y = 88
        tabs = ['Feed', 'Events', 'Messages']
        tab_width = self.screen_width / len(tabs)
        for i, tab in enumerate(tabs):
            # Tab background
            dwg.add(dwg.rect(
                (i * tab_width, y),
                (tab_width, 44),
                fill=self.colors['surface'] if i == 0 else 'none',
                stroke=self.colors['border']
            ))
            # Tab text
            dwg.add(dwg.text(
                tab,
                insert=(i * tab_width + tab_width/2, y + 28),
                text_anchor='middle',
                fill=self.colors['primary'] if i == 0 else self.colors['secondary'],
                style='font-family: SF Pro Text; font-size: 15px'
            ))
        
        # Community Feed
        y = 152
        dwg.add(dwg.text(
            "Community Feed",
            insert=(20, y),
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
        ))
        
        # Feed items
        y += 20
        for i in range(3):
            dwg.add(dwg.rect(
                (20, y + i*120),
                (self.screen_width - 40, 100),
                rx=8, ry=8,
                fill=self.colors['surface']
            ))
            # User avatar
            dwg.add(dwg.circle(
                (50, y + i*120 + 30),
                20,
                fill='#E5E5EA'
            ))
            # Post content
            dwg.add(dwg.text(
                "Athlete Name",
                insert=(80, y + i*120 + 25),
                fill=self.colors['text'],
                style='font-family: SF Pro Text; font-size: 15px; font-weight: 600'
            ))
            dwg.add(dwg.text(
                "Post preview...",
                insert=(80, y + i*120 + 45),
                fill=self.colors['secondary'],
                style='font-family: SF Pro Text; font-size: 13px'
            ))
        
        return dwg

    def create_events_screen(self):
        """Create events screen wireframe"""
        dwg = self.create_base_screen("events")
        self.add_nav_bar(dwg, "Events")
        
        # Search bar
        y = 108
        dwg.add(dwg.rect(
            (20, y),
            (self.screen_width - 40, 44),
            rx=22, ry=22,
            fill=self.colors['surface']
        ))
        dwg.add(dwg.text(
            "Search events...",
            insert=(50, y + 28),
            fill=self.colors['secondary'],
            style='font-family: SF Pro Text; font-size: 15px'
        ))
        
        # Upcoming Events
        y += 64
        dwg.add(dwg.text(
            "Upcoming Events",
            insert=(20, y),
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
        ))
        
        # Event cards
        y += 20
        for i in range(3):
            dwg.add(dwg.rect(
                (20, y + i*140),
                (self.screen_width - 40, 120),
                rx=8, ry=8,
                fill=self.colors['surface']
            ))
            # Event image placeholder
            dwg.add(dwg.rect(
                (20, y + i*140),
                (self.screen_width - 40, 60),
                rx=8, ry=8,
                fill='#E5E5EA'
            ))
            # Event details
            dwg.add(dwg.text(
                f"Event {i+1}",
                insert=(30, y + i*140 + 80),
                fill=self.colors['text'],
                style='font-family: SF Pro Text; font-size: 15px; font-weight: 600'
            ))
            dwg.add(dwg.text(
                "Date & Location",
                insert=(30, y + i*140 + 100),
                fill=self.colors['secondary'],
                style='font-family: SF Pro Text; font-size: 13px'
            ))
            # RSVP button
            dwg.add(dwg.rect(
                (self.screen_width - 100, y + i*140 + 75),
                (60, 30),
                rx=15, ry=15,
                fill=self.colors['primary']
            ))
            dwg.add(dwg.text(
                "RSVP",
                insert=(self.screen_width - 70, y + i*140 + 95),
                text_anchor='middle',
                fill='white',
                style='font-family: SF Pro Text; font-size: 13px'
            ))
        
        return dwg
    def create_premium_features_screen(self):
        """Create premium features screen wireframe"""
        dwg = self.create_base_screen("premium_features")
        self.add_nav_bar(dwg, "Premium Features")
        
        # Plans section
        y = 108
        dwg.add(dwg.text(
            "Premium Plans",
            insert=(20, y),
            fill=self.colors['text'],
            style='font-family: -apple-system, SF Pro Text, Helvetica; font-size: 17px; font-weight: 600'
        ))
        
        # Subscription plans with proper spacing and content
        plans = [
            {
                'name': 'Basic',
                'price': '$0',
                'features': 'Previews + Limited access',
                'selected': False
            },
            {
                'name': 'Plus',
                'price': '$6.99',
                'features': 'Basic streaming access',
                'selected': False
            },
            {
                'name': 'Pro',
                'price': '$9.99',
                'features': 'Unlimited streaming + Downloads',
                'selected': True
            },
            {
                'name': 'Elite',
                'price': '$17.99',
                'features': 'All features + VIP access',
                'selected': False
            }
        ]
        
        y += 30
        for i, plan in enumerate(plans):
            # Plan container with proper spacing
            dwg.add(dwg.rect(
                (20, y),
                (self.screen_width - 40, 120),
                rx=8, ry=8,
                fill=self.colors['surface']
            ))
            
            # Plan name
            dwg.add(dwg.text(
                plan['name'],
                insert=(40, y + 30),
                fill=self.colors['text'],
                style='font-family: -apple-system, SF Pro Text, Helvetica; font-size: 17px; font-weight: 600'
            ))
            
            # Price with currency symbol
            dwg.add(dwg.text(
                plan['price'],
                insert=(40, y + 60),
                fill=self.colors['primary'],
                style='font-family: -apple-system, SF Pro Text, Helvetica; font-size: 24px; font-weight: bold'
            ))
            
            # Features text
            dwg.add(dwg.text(
                plan['features'],
                insert=(40, y + 90),
                fill=self.colors['secondary'],
                style='font-family: -apple-system, SF Pro Text, Helvetica; font-size: 13px'
            ))
            
            # Select button
            dwg.add(dwg.rect(
                (self.screen_width - 100, y + 45),  # Adjusted y position
                (60, 30),
                rx=15, ry=15,
                fill=self.colors['primary'] if plan['selected'] else 'none',
                stroke=self.colors['primary']
            ))
            
            dwg.add(dwg.text(
                "Select",
                insert=(self.screen_width - 70, y + 65),  # Adjusted y position
                text_anchor='middle',
                fill='white' if plan['selected'] else self.colors['primary'],
                style='font-family: -apple-system, SF Pro Text, Helvetica; font-size: 13px'
            ))
            
            y += 100  # Increased spacing between plans
        
        return dwg

    def create_exclusive_content_screen(self):
        """Create exclusive content screen wireframe"""
        dwg = self.create_base_screen("exclusive_content")
        self.add_nav_bar(dwg, "Exclusive Content")
        
        # VIP Events section
        y = 108
        dwg.add(dwg.text(
            "VIP Events",
            insert=(20, y),
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
        ))
        
        # Event cards
        y += 30
        for i in range(2):
            dwg.add(dwg.rect(
                (20, y),
                (self.screen_width - 40, 120),
                rx=8, ry=8,
                fill=self.colors['surface']
            ))
            # Event image area
            dwg.add(dwg.rect(
                (20, y),
                (self.screen_width - 40, 60),
                rx=8, ry=8,
                fill='#E5E5EA'
            ))
            # Event details
            dwg.add(dwg.text(
                f"VIP Event {i+1}",
                insert=(40, y + 80),
                fill=self.colors['text'],
                style='font-family: SF Pro Text; font-size: 15px; font-weight: 600'
            ))
            dwg.add(dwg.text(
                "Exclusive Meet & Greet",
                insert=(40, y + 100),
                fill=self.colors['secondary'],
                style='font-family: SF Pro Text; font-size: 13px'
            ))
            y += 140
        
        # Premium Content section
        dwg.add(dwg.text(
            "Premium Content",
            insert=(20, y),
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
        ))
        
        # Content grid
        y += 30
        for i in range(2):
            dwg.add(dwg.rect(
                (20, y),
                (self.screen_width - 40, 80),
                rx=8, ry=8,
                fill=self.colors['surface']
            ))
            # Content info
            dwg.add(dwg.text(
                f"Exclusive Track {i+1}",
                insert=(40, y + 30),
                fill=self.colors['text'],
                style='font-family: SF Pro Text; font-size: 15px; font-weight: 600'
            ))
            dwg.add(dwg.text(
                "Premium Release",
                insert=(40, y + 50),
                fill=self.colors['secondary'],
                style='font-family: SF Pro Text; font-size: 13px'
            ))
            y += 100
        
        return dwg

    def create_user_content_screen(self):
        """Create user content management screen wireframe"""
        dwg = self.create_base_screen("user_content")
        self.add_nav_bar(dwg, "My Library")
        
        # Search and filter
        y = 108
        dwg.add(dwg.rect(
            (20, y),
            (self.screen_width - 40, 44),
            rx=22, ry=22,
            fill=self.colors['surface']
        ))
        dwg.add(dwg.text(
            "Search playlists...",
            insert=(50, y + 28),
            fill=self.colors['secondary'],
            style='font-family: SF Pro Text; font-size: 15px'
        ))
        
        # Playlists section
        y += 74
        dwg.add(dwg.text(
            "My Playlists",
            insert=(20, y),
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
        ))
        
        # Playlist grid
        y += 20
        for i in range(3):
            dwg.add(dwg.rect(
                (20, y + i*120),
                (self.screen_width - 40, 100),
                rx=8, ry=8,
                fill=self.colors['surface']
            ))
            # Playlist cover
            dwg.add(dwg.rect(
                (20, y + i*120),
                (100, 100),
                rx=8, ry=8,
                fill='#E5E5EA'
            ))
            # Playlist info
            dwg.add(dwg.text(
                f"Playlist {i+1}",
                insert=(140, y + i*120 + 30),
                fill=self.colors['text'],
                style='font-family: SF Pro Text; font-size: 15px; font-weight: 600'
            ))
            dwg.add(dwg.text(
                f"{(i+1)*10} tracks",
                insert=(140, y + i*120 + 50),
                fill=self.colors['secondary'],
                style='font-family: SF Pro Text; font-size: 13px'
            ))
            
        return dwg

    def create_user_favorites_screen(self):
        """Create user favorites screen wireframe"""
        dwg = self.create_base_screen("favorites")
        self.add_nav_bar(dwg, "Favorites")
        
        # Tabs
        y = 88
        tabs = ['Tracks', 'Artists', 'Playlists']
        tab_width = self.screen_width / len(tabs)
        for i, tab in enumerate(tabs):
            # Tab background
            dwg.add(dwg.rect(
                (i * tab_width, y),
                (tab_width, 44),
                fill=self.colors['surface'] if i == 0 else 'none',
                stroke=self.colors['border']
            ))
            # Tab text
            dwg.add(dwg.text(
                tab,
                insert=(i * tab_width + tab_width/2, y + 28),
                text_anchor='middle',
                fill=self.colors['primary'] if i == 0 else self.colors['secondary'],
                style='font-family: SF Pro Text; font-size: 15px'
            ))
        
        # Favorites list
        y = 152
        for i in range(5):
            dwg.add(dwg.rect(
                (20, y + i*70),
                (self.screen_width - 40, 60),
                rx=8, ry=8,
                fill=self.colors['surface']
            ))
            # Track/Artist image
            dwg.add(dwg.rect(
                (20, y + i*70),
                (60, 60),
                rx=8, ry=8,
                fill='#E5E5EA'
            ))
            # Info
            dwg.add(dwg.text(
                f"Track {i+1}",
                insert=(100, y + i*70 + 25),
                fill=self.colors['text'],
                style='font-family: SF Pro Text; font-size: 15px; font-weight: 600'
            ))
            dwg.add(dwg.text(
                "Artist Name",
                insert=(100, y + i*70 + 45),
                fill=self.colors['secondary'],
                style='font-family: SF Pro Text; font-size: 13px'
            ))
            # Favorite icon
            dwg.add(dwg.circle(
                (self.screen_width - 40, y + i*70 + 30),
                15,
                fill=self.colors['primary']
            ))
        
        return dwg
    def create_user_analytics_screen(self):
        """Create user analytics screen wireframe"""
        dwg = self.create_base_screen("user_analytics")
        self.add_nav_bar(dwg, "My Stats")
        
        # Listening Stats
        y = 108
        dwg.add(dwg.text(
            "Listening Activity",
            insert=(20, y),
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
        ))
        
        # Stats cards
        stats = [
            {'label': 'Hours Listened', 'value': '24.5'},
            {'label': 'Artists', 'value': '12'},
            {'label': 'Playlists', 'value': '5'}
        ]
        
        y += 30
        for i, stat in enumerate(stats):
            x = 20 + i*(self.screen_width/3 - 20)
            dwg.add(dwg.rect(
                (x, y),
                ((self.screen_width/3 - 30), 80),
                rx=8, ry=8,
                fill=self.colors['surface']
            ))
            # Stat value
            dwg.add(dwg.text(
                stat['value'],
                insert=(x + (self.screen_width/3 - 30)/2, y + 35),
                text_anchor='middle',
                fill=self.colors['text'],
                style='font-family: SF Pro Text; font-size: 24px; font-weight: bold'
            ))
            # Stat label
            dwg.add(dwg.text(
                stat['label'],
                insert=(x + (self.screen_width/3 - 30)/2, y + 60),
                text_anchor='middle',
                fill=self.colors['secondary'],
                style='font-family: SF Pro Text; font-size: 13px'
            ))
        
        # Top Artists section
        y += 120
        dwg.add(dwg.text(
            "Top Artists",
            insert=(20, y),
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 15px'
        ))
        
        # Artist list
        y += 20
        for i in range(3):
            dwg.add(dwg.rect(
                (20, y + i*70),
                (self.screen_width - 40, 60),
                rx=8, ry=8,
                fill=self.colors['surface']
            ))
            # Artist image
            dwg.add(dwg.circle(
                (50, y + i*70 + 30),
                25,
                fill='#E5E5EA'
            ))
            # Artist info
            dwg.add(dwg.text(
                f"Artist {i+1}",
                insert=(90, y + i*70 + 25),
                fill=self.colors['text'],
                style='font-family: SF Pro Text; font-size: 15px; font-weight: 600'
            ))
            dwg.add(dwg.text(
                f"{(3-i)} hours listened",
                insert=(90, y + i*70 + 45),
                fill=self.colors['secondary'],
                style='font-family: SF Pro Text; font-size: 13px'
            ))
        
        return dwg

    def create_user_profile_screen(self):
        """Create user profile screen wireframe"""
        dwg = self.create_base_screen("user_profile")
        self.add_nav_bar(dwg, "Profile")
        
        # Profile header
        y = 108
        # Profile image
        dwg.add(dwg.circle(
            (self.screen_width/2, y + 50),
            40,
            fill=self.colors['surface']
        ))
        # Username
        dwg.add(dwg.text(
            "Username",
            insert=(self.screen_width/2, y + 110),
            text_anchor='middle',
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
        ))
        
        # Stats summary
        y += 140
        stats = [
            {'label': 'Playlists', 'value': '12'},
            {'label': 'Following', 'value': '45'},
            {'label': 'Events', 'value': '3'}
        ]
        
        for i, stat in enumerate(stats):
            x = 20 + i*(self.screen_width/3 - 20)
            dwg.add(dwg.rect(
                (x, y),
                ((self.screen_width/3 - 30), 60),
                rx=8, ry=8,
                fill=self.colors['surface']
            ))
            dwg.add(dwg.text(
                stat['value'],
                insert=(x + (self.screen_width/3 - 30)/2, y + 25),
                text_anchor='middle',
                fill=self.colors['text'],
                style='font-family: SF Pro Text; font-size: 17px; font-weight: bold'
            ))
            dwg.add(dwg.text(
                stat['label'],
                insert=(x + (self.screen_width/3 - 30)/2, y + 45),
                text_anchor='middle',
                fill=self.colors['secondary'],
                style='font-family: SF Pro Text; font-size: 13px'
            ))
        
        # Settings button
        dwg.add(dwg.rect(
            (20, self.screen_height - 80),
            (self.screen_width - 40, 50),
            rx=25, ry=25,
            fill=self.colors['primary']
        ))
        dwg.add(dwg.text(
            "Edit Profile",
            insert=(self.screen_width/2, self.screen_height - 45),
            text_anchor='middle',
            fill='white',
            style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
        ))
        
        return dwg
    def create_user_profile_screenb(self):
        """Create user profile screen wireframe"""
        dwg = self.create_base_screen("user_profile")
        self.add_nav_bar(dwg, "Profile")
        
        # Profile header
        y = 108
        # Profile image
        dwg.add(dwg.circle(
            (self.screen_width/2, y + 50),
            40,
            fill=self.colors['surface']
        ))
        # Username
        dwg.add(dwg.text(
            "Username",
            insert=(self.screen_width/2, y + 110),
            text_anchor='middle',
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
        ))
        
        # Stats summary
        y += 140
        stats = [
            {'label': 'Following', 'value': '45'},
            {'label': 'Playlists', 'value': '12'},
            {'label': 'Events', 'value': '3'}
        ]
        
        for i, stat in enumerate(stats):
            x = 20 + i*(self.screen_width/3 - 20)
            dwg.add(dwg.rect(
                (x, y),
                ((self.screen_width/3 - 30), 60),
                rx=8, ry=8,
                fill=self.colors['surface']
            ))
            dwg.add(dwg.text(
                stat['value'],
                insert=(x + (self.screen_width/3 - 30)/2, y + 25),
                text_anchor='middle',
                fill=self.colors['text'],
                style='font-family: SF Pro Text; font-size: 17px; font-weight: bold'
            ))
            dwg.add(dwg.text(
                stat['label'],
                insert=(x + (self.screen_width/3 - 30)/2, y + 45),
                text_anchor='middle',
                fill=self.colors['secondary'],
                style='font-family: SF Pro Text; font-size: 13px'
            ))
        
        # Activity section
        y += 100
        dwg.add(dwg.text(
            "Recent Activity",
            insert=(20, y),
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 15px; font-weight: 600'
        ))
        
        # Activity list
        y += 20
        for i in range(3):
            dwg.add(dwg.rect(
                (20, y + i*60),
                (self.screen_width - 40, 50),
                rx=8, ry=8,
                fill=self.colors['surface']
            ))
            dwg.add(dwg.text(
                f"Activity {i+1}",
                insert=(40, y + i*60 + 30),
                fill=self.colors['text'],
                style='font-family: SF Pro Text; font-size: 15px'
            ))
        
        return dwg

    def create_user_preferences_screen(self):
        """Create user preferences screen wireframe"""
        dwg = self.create_base_screen("preferences")
        self.add_nav_bar(dwg, "Preferences")
        
        # Music preferences
        y = 108
        dwg.add(dwg.text(
            "Music Preferences",
            insert=(20, y),
            fill=self.colors['text'],
            style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
        ))
        
        # Genre selection
        y += 40
        genres = ['Hip Hop', 'R&B', 'Pop', 'Rock']
        for genre in genres:
            dwg.add(dwg.rect(
                (20, y),
                (self.screen_width - 40, 50),
                rx=8, ry=8,
                fill='none',
                stroke=self.colors['border']
            ))
            dwg.add(dwg.text(
                genre,
                insert=(40, y + 30),
                fill=self.colors['text'],
                style='font-family: SF Pro Text; font-size: 15px'
            ))
            # Checkbox
            dwg.add(dwg.rect(
                (self.screen_width - 60, y + 15),
                (20, 20),
                rx=4, ry=4,
                fill='none',
                stroke=self.colors['border']
            ))
            y += 60
        
        # Save button
        dwg.add(dwg.rect(
            (20, self.screen_height - 80),
            (self.screen_width - 40, 50),
            rx=25, ry=25,
            fill=self.colors['primary']
        ))
        dwg.add(dwg.text(
            "Save Preferences",
            insert=(self.screen_width/2, self.screen_height - 45),
            text_anchor='middle',
            fill='white',
            style='font-family: SF Pro Text; font-size: 17px; font-weight: 600'
        ))
        
        return dwg

def main():
    st.set_page_config(layout="wide", page_title="User Journey Wireframes")
    
    st.markdown("""
        <style>
        .stApp {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        </style>
    """, unsafe_allow_html=True)
    
    wireframes = UserAppWireframes()
    
    st.title("User Journey - Welcome Flow")
    
    # Show first screen
    welcome_screen = wireframes.create_welcome_screen()
    st.markdown(welcome_screen.tostring(), unsafe_allow_html=True)

    st.title("User Journey - Discovery Flow")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Discovery Screen")
        discovery = wireframes.create_user_discovery_screen()
        st.markdown(discovery.tostring(), unsafe_allow_html=True)
        st.markdown("**Next:** Playlist Creation")
    
    with col2:
        st.subheader("Playlist Screen")
        playlist = wireframes.create_playlist_screen()
        st.markdown(playlist.tostring(), unsafe_allow_html=True)
        st.markdown("**Next:** Community")

    st.title("User Journey - Engagement Flow")
    
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Community Feed")
        engagement = wireframes.create_engagement_screen()
        st.markdown(engagement.tostring(), unsafe_allow_html=True)
        st.markdown("**Next:** Events")
    
    with col4:
        st.subheader("Events")
        events = wireframes.create_events_screen()
        st.markdown(events.tostring(), unsafe_allow_html=True)
        st.markdown("**Next:** Premium Features")

    st.title("User Journey - Premium Features")
    
    col5, col6 = st.columns(2) 
    with col5:
        st.subheader("Premium Features")
        premium = wireframes.create_premium_features_screen()
        st.markdown(premium.tostring(), unsafe_allow_html=True)
        st.markdown("**Next:** Exclusive Content")
    
    with col6:
        st.subheader("Exclusive Content")
        exclusive = wireframes.create_exclusive_content_screen()
        st.markdown(exclusive.tostring(), unsafe_allow_html=True)

    st.title("User Journey - Content Management")
    
    col7, col8 = st.columns(2)
    with col7:
        st.subheader("My Library")
        content = wireframes.create_user_content_screen()
        st.markdown(content.tostring(), unsafe_allow_html=True)
        st.markdown("**Next:** Favorites")
    
    with col8:
        st.subheader("Favorites")
        favorites = wireframes.create_user_favorites_screen()
        st.markdown(favorites.tostring(), unsafe_allow_html=True)
        st.markdown("**Next:** Community")
    
    st.title("User Journey - Profile & Analytics")
    
    col9, col10 = st.columns(2)
    with col9:
        st.subheader("Analytics")
        analytics = wireframes.create_user_analytics_screen()
        st.markdown(analytics.tostring(), unsafe_allow_html=True)
        st.markdown("**Next:** Profile")
    
    with col10:
        st.subheader("Profile")
        profile = wireframes.create_user_profile_screen()
        st.markdown(profile.tostring(), unsafe_allow_html=True)

    st.title("User Journey - Profile & Preferences")
    
    col11, col12 = st.columns(2)
    with col11:
        st.subheader("User Profile")
        profile = wireframes.create_user_profile_screenb()
        st.markdown(profile.tostring(), unsafe_allow_html=True)
        st.markdown("**Next:** Preferences")
    
    with col12:
        st.subheader("User Preferences")
        preferences = wireframes.create_user_preferences_screen()
        st.markdown(preferences.tostring(), unsafe_allow_html=True)

    st.markdown("""
        ### User Journey Flow Description

        1. **Registration Flow**
        - Welcome → Account Creation → Profile Setup
        - Sign up and personalize experience

        2. **Discovery Flow**
        - Browse Athletes → Search Interface → Playlist Creation
        - Find and collect favorite music

        3. **Engagement Flow**
        - Community Feed → Events Calendar
        - Connect with athletes and attend events

        4. **Premium Features**
        - Premium Plans → Exclusive Content
        - Access VIP features and special events

        5. **Content Access**
        - Library Management → Favorites
        - Organize personal collection and playlists

        This journey flow shows:
        - Clear user progression from registration to premium features
        - Focus on discovery and engagement
        - Emphasis on community participation
        - Path to exclusive content access
        """)


if __name__ == "__main__":
    main()