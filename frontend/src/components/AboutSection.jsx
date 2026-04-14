import React, { useState, useEffect, useRef } from 'react';
import { aboutData, statsData } from '../mock/mockData';
import { Check } from 'lucide-react';
import AnimatedCounter from './AnimatedCounter';

const AboutSection = () => {
  const [isVisible, setIsVisible] = useState(false);
  const sectionRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
        }
      },
      { threshold: 0.2 }
    );

    if (sectionRef.current) {
      observer.observe(sectionRef.current);
    }

    return () => {
      if (sectionRef.current) {
        observer.unobserve(sectionRef.current);
      }
    };
  }, []);

  return (
    <section id="about" ref={sectionRef} className="py-20 bg-gradient-to-b from-white to-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Stats Section */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mb-20">
          {statsData.map((stat, index) => (
            <div
              key={index}
              className="text-center p-6 bg-white rounded-2xl shadow-lg hover:shadow-xl transition-shadow duration-300"
              style={{
                animationDelay: `${index * 100}ms`
              }}
            >
              <div className="text-4xl md:text-5xl font-bold text-blue-600 mb-2">
                <AnimatedCounter
                  end={stat.number}
                  duration={stat.duration}
                  suffix={stat.suffix}
                  inView={isVisible}
                />
              </div>
              <div className="text-gray-600 font-medium">{stat.label}</div>
            </div>
          ))}
        </div>

        {/* About Content */}
        <div className="grid md:grid-cols-2 gap-12 items-center">
          {/* Image */}
          <div className="relative">
            <div className="relative rounded-2xl overflow-hidden shadow-2xl">
              <img
                src={aboutData.image}
                alt="SPARK AI Hub Facility"
                className="w-full h-full object-cover"
              />
              <div className="absolute inset-0 bg-gradient-to-tr from-blue-600/20 to-transparent"></div>
            </div>
            {/* Decorative Element */}
            <div className="absolute -bottom-6 -right-6 w-48 h-48 bg-blue-100 rounded-2xl -z-10"></div>
            <div className="absolute -top-6 -left-6 w-32 h-32 bg-blue-50 rounded-2xl -z-10"></div>
          </div>

          {/* Content */}
          <div className="space-y-6">
            <div>
              <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
                {aboutData.title}
              </h2>
              <div className="h-1 w-24 bg-gradient-to-r from-blue-600 to-blue-400 rounded-full"></div>
            </div>

            <p className="text-lg text-gray-700 leading-relaxed">
              {aboutData.description}
            </p>

            <p className="text-gray-600 leading-relaxed">
              {aboutData.mission}
            </p>

            {/* Features List */}
            <div className="space-y-3 pt-4">
              {aboutData.features.map((feature, index) => (
                <div
                  key={index}
                  className="flex items-start space-x-3 group"
                >
                  <div className="mt-1 p-1 bg-blue-100 rounded-full group-hover:bg-blue-600 transition-colors duration-300">
                    <Check className="h-4 w-4 text-blue-600 group-hover:text-white transition-colors duration-300" />
                  </div>
                  <span className="text-gray-700">{feature}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutSection;
