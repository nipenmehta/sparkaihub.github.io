// Mock data for SPARK AI Hub website

export const heroData = {
  title: "SPARK AI Hub",
  subtitle: "Sharjah's Innovation Center for Artificial Intelligence",
  description: "Empowering innovation through cutting-edge AI technology, collaborative research, and entrepreneurial excellence",
  backgroundImage: "https://images.pexels.com/photos/8386437/pexels-photo-8386437.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
};

export const statsData = [
  { number: 50, suffix: "+", label: "AI Projects", duration: 2000 },
  { number: 100, suffix: "+", label: "Partnerships", duration: 2500 },
  { number: 1000, suffix: "+", label: "Innovators", duration: 3000 },
  { number: 25, suffix: "+", label: "Research Labs", duration: 2200 }
];

export const aboutData = {
  title: "About SPARK AI Hub",
  description: "The SPARK AI Hub is Sharjah's premier innovation center dedicated to strengthening the emirate's technological leadership through advanced AI research, development, and collaboration.",
  mission: "Our mission is to create a thriving ecosystem where innovation flourishes, supporting local talent, fostering cross-sector partnerships, and transforming AI possibilities into real-world solutions for a sustainable, knowledge-based economy.",
  image: "https://images.unsplash.com/photo-1655393001768-d946c97d6fd1?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NjAxODF8MHwxfHNlYXJjaHwzfHxhcnRpZmljaWFsJTIwaW50ZWxsaWdlbmNlfGVufDB8fHxibHVlfDE3NzYxODg5MzN8MA&ixlib=rb-4.1.0&q=85",
  features: [
    "State-of-the-art laboratories and research facilities",
    "Advanced AI and machine learning infrastructure",
    "Collaborative spaces for government, industry, and academia",
    "Comprehensive skills development programs",
    "Startup incubation and acceleration support"
  ]
};

export const aiServicesData = [
  {
    id: 1,
    title: "Machine Learning Solutions",
    description: "Advanced ML models and algorithms for predictive analytics, pattern recognition, and intelligent automation",
    image: "https://images.pexels.com/photos/8566526/pexels-photo-8566526.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    icon: "Brain"
  },
  {
    id: 2,
    title: "Natural Language Processing",
    description: "Cutting-edge NLP solutions for text analysis, sentiment detection, chatbots, and language translation",
    image: "https://images.unsplash.com/photo-1607895232440-6ba075948c14?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NTYxNzV8MHwxfHNlYXJjaHw0fHx0ZWNobm9sb2d5JTIwZnV0dXJpc3RpY3xlbnwwfHx8Ymx1ZXwxNzc2MTg4OTM3fDA&ixlib=rb-4.1.0&q=85",
    icon: "MessageSquare"
  },
  {
    id: 3,
    title: "Computer Vision",
    description: "Image recognition, object detection, facial analysis, and visual data processing for diverse applications",
    image: "https://images.unsplash.com/photo-1660165458059-57cfb6cc87e5?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NjAxODF8MHwxfHNlYXJjaHwyfHxhcnRpZmljaWFsJTIwaW50ZWxsaWdlbmNlfGVufDB8fHxibHVlfDE3NzYxODg5MzN8MA&ixlib=rb-4.1.0&q=85",
    icon: "Eye"
  },
  {
    id: 4,
    title: "AI Research & Development",
    description: "Collaborative research programs exploring frontier AI technologies and their practical applications",
    image: "https://images.unsplash.com/photo-1535448674466-81707cbfe0f7?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NTYxNzV8MHwxfHNlYXJjaHwzfHx0ZWNobm9sb2d5JTIwZnV0dXJpc3RpY3xlbnwwfHx8Ymx1ZXwxNzc2MTg4OTM3fDA&ixlib=rb-4.1.0&q=85",
    icon: "Lightbulb"
  },
  {
    id: 5,
    title: "AI Training & Workshops",
    description: "Comprehensive training programs to upskill professionals and students in AI technologies",
    image: "https://images.pexels.com/photos/8566526/pexels-photo-8566526.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    icon: "GraduationCap"
  },
  {
    id: 6,
    title: "Innovation Consulting",
    description: "Strategic guidance for businesses to integrate AI solutions and drive digital transformation",
    image: "https://images.unsplash.com/photo-1660165458059-57cfb6cc87e5?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NjAxODF8MHwxfHNlYXJjaHwyfHxhcnRpZmljaWFsJTIwaW50ZWxsaWdlbmNlfGVufDB8fHxibHVlfDE3NzYxODg5MzN8MA&ixlib=rb-4.1.0&q=85",
    icon: "Briefcase"
  }
];

export const onboardingSteps = [
  {
    step: 1,
    title: "Submit Your Interest",
    description: "Fill out our onboarding application form with your details and area of interest",
    icon: "FileText"
  },
  {
    step: 2,
    title: "Initial Consultation",
    description: "Our team will review your application and schedule a consultation to understand your needs",
    icon: "Users"
  },
  {
    step: 3,
    title: "Customized Plan",
    description: "We'll create a tailored collaboration plan based on your objectives and requirements",
    icon: "ClipboardCheck"
  },
  {
    step: 4,
    title: "Start Innovating",
    description: "Begin your journey with access to our facilities, resources, and expert support",
    icon: "Rocket"
  }
];

export const mockContactSubmission = async (formData) => {
  // Simulate API delay
  await new Promise(resolve => setTimeout(resolve, 1000));
  
  console.log("Mock Contact Form Submission:", formData);
  
  return {
    success: true,
    message: "Thank you for your interest! We'll contact you soon."
  };
};

export const mockOnboardingSubmission = async (formData) => {
  // Simulate API delay
  await new Promise(resolve => setTimeout(resolve, 1200));
  
  console.log("Mock Onboarding Form Submission:", formData);
  
  return {
    success: true,
    message: "Your application has been submitted successfully! We'll be in touch shortly."
  };
};
