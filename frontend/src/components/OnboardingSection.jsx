import React from 'react';
import { onboardingSteps } from '../mock/mockData';
import { FileText, Users, ClipboardCheck, Rocket, CheckCircle2 } from 'lucide-react';

const iconMap = {
  FileText,
  Users,
  ClipboardCheck,
  Rocket
};

const OnboardingSection = () => {

  return (
    <section id="onboarding" className="py-20 bg-gradient-to-b from-gray-50 to-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            How to Onboard With Us
          </h2>
          <div className="flex items-center justify-center space-x-2 mb-6">
            <div className="h-1 w-24 bg-gradient-to-r from-transparent via-blue-600 to-blue-600 rounded-full"></div>
            <div className="h-1 w-24 bg-gradient-to-r from-blue-600 to-transparent rounded-full"></div>
          </div>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Join SPARK AI Hub in four simple steps and start your innovation journey
          </p>
        </div>

        {/* Steps Timeline */}
        <div className="mb-20">
          <div className="grid md:grid-cols-4 gap-8">
            {onboardingSteps.map((step, index) => {
              const Icon = iconMap[step.icon];
              return (
                <div key={step.step} className="relative">
                  {/* Connecting Line */}
                  {index < onboardingSteps.length - 1 && (
                    <div className="hidden md:block absolute top-12 left-1/2 w-full h-0.5 bg-gradient-to-r from-blue-600 to-blue-400 z-0"></div>
                  )}

                  {/* Step Card */}
                  <div className="relative z-10 text-center">
                    {/* Icon Circle */}
                    <div className="inline-flex items-center justify-center w-24 h-24 bg-gradient-to-br from-blue-600 to-blue-400 rounded-full shadow-lg mb-4 group hover:scale-110 transition-transform duration-300">
                      <Icon className="h-10 w-10 text-white" />
                    </div>

                    {/* Step Number */}
                    <div className="absolute top-0 right-1/2 transform translate-x-1/2 -translate-y-2">
                      <div className="w-8 h-8 bg-white border-4 border-blue-600 rounded-full flex items-center justify-center text-sm font-bold text-blue-600">
                        {step.step}
                      </div>
                    </div>

                    {/* Content */}
                    <h3 className="text-xl font-bold text-gray-900 mb-2">
                      {step.title}
                    </h3>
                    <p className="text-gray-600">
                      {step.description}
                    </p>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Application Button */}
        <div className="max-w-2xl mx-auto text-center">
          <div className="bg-white rounded-2xl shadow-xl p-12 border border-gray-100">
            <h3 className="text-3xl font-bold text-gray-900 mb-4">
              Ready to Start Your Journey?
            </h3>
            <p className="text-gray-600 mb-8 text-lg">
              Click below to submit your application and join SPARK AI Hub's innovation community
            </p>
            <a
              href="https://ai.srtip.ae/#contact"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center px-12 py-4 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg shadow-lg hover:shadow-xl transition-all duration-300 space-x-2"
            >
              <span>Submit Application</span>
              <CheckCircle2 className="h-5 w-5" />
            </a>
          </div>
        </div>
      </div>
    </section>
  );
};

export default OnboardingSection;
