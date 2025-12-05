const { useState, useEffect, useRef } = React;
const { BarChart, Bar, LineChart, Line, ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell, ReferenceLine } = Recharts;

const WhatsAppStory = () => {
  const [scrollProgress, setScrollProgress] = useState(0);
  const [visibleSections, setVisibleSections] = useState(new Set());

  useEffect(() => {
    const handleScroll = () => {
      const scrolled = window.scrollY;
      const height = document.documentElement.scrollHeight - window.innerHeight;
      setScrollProgress(scrolled / height);

      // Track visible sections
      const sections = document.querySelectorAll('[data-section]');
      const visible = new Set();
      sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        if (rect.top < window.innerHeight * 0.7 && rect.bottom > window.innerHeight * 0.3) {
          visible.add(section.dataset.section);
        }
      });
      setVisibleSections(visible);
    };

    window.addEventListener('scroll', handleScroll);
    handleScroll();
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const isVisible = (section) => visibleSections.has(section);

  // Data for visualizations
  const participationData = [
    { category: '1 message', users: 31, pct: 26.1 },
    { category: '2-5 messages', users: 52, pct: 43.7 },
    { category: '6-10 messages', users: 12, pct: 10.1 },
    { category: '11-20 messages', users: 10, pct: 8.4 },
    { category: '21-50 messages', users: 10, pct: 8.4 },
    { category: '51-100 messages', users: 4, pct: 3.4 }
  ];

  const aprilData = [
    { date: 'Apr 1-8', messages: 4 },
    { date: 'Apr 9', messages: 17 },
    { date: 'Apr 10', messages: 26 },
    { date: 'Apr 11', messages: 60 },
    { date: 'Apr 12', messages: 34 },
    { date: 'Apr 13', messages: 27 },
    { date: 'Apr 14', messages: 77 },
    { date: 'Apr 15-30', messages: 26 }
  ];

  const engagementData = [
    { name: 'Rajesh Bhura', messages: 15, reactions: 2.4, category: 'High' },
    { name: 'Pawan Bhargava', messages: 61, reactions: 1.56, category: 'High' },
    { name: 'Gaurav Vohra', messages: 39, reactions: 1.49, category: 'High' },
    { name: 'Sandeep Dongre', messages: 39, reactions: 1.26, category: 'Medium' },
    { name: 'Somnath Manna', messages: 66, reactions: 0.76, category: 'Medium' },
    { name: 'Vipul', messages: 30, reactions: 0.30, category: 'Low' },
    { name: 'Chidambaram P', messages: 61, reactions: 0.0, category: 'None' }
  ];

  const contentTypeData = [
    { type: 'Media\n(photos/videos)', reactions: 2.76, baseline: 0.68 },
    { type: 'Forwarded\ncontent', reactions: 2.71, baseline: 0.68 },
    { type: 'Original\nreplies', reactions: 0.29, baseline: 0.68 },
    { type: 'Long text\n(>200 chars)', reactions: 0.72, baseline: 0.68 }
  ];

  const deletionData = [
    { user: 'PC', deleted: 87, total: 196, rate: 44.4 },
    { user: 'Group Average', deleted: 19, total: 1896, rate: 1.0 }
  ];

  const CustomTooltip = ({ active, payload }) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-gray-900 text-white px-4 py-2 rounded shadow-lg border border-gray-700">
          {payload.map((entry, index) => (
            <div key={index}>
              <p className="font-medium">{entry.name}: {entry.value}</p>
            </div>
          ))}
        </div>
      );
    }
    return null;
  };

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900" style={{ fontFamily: 'Georgia, serif' }}>
      {/* Progress Bar */}
      <div className="fixed top-0 left-0 w-full h-1 bg-gray-200 z-50">
        <div
          className="h-full bg-red-600 transition-all duration-100"
          style={{ width: `${scrollProgress * 100}%` }}
        />
      </div>

      {/* Hero Section */}
      <header className="min-h-screen flex items-center justify-center px-6 bg-gradient-to-b from-gray-900 to-gray-800 text-white relative overflow-hidden">
        <div className="absolute inset-0 opacity-10">
          <div className="absolute inset-0" style={{
            backgroundImage: 'radial-gradient(circle at 2px 2px, rgba(255,255,255,0.15) 1px, transparent 0)',
            backgroundSize: '40px 40px'
          }} />
        </div>
        <div className="max-w-4xl mx-auto text-center relative z-10">
          <div className="text-sm uppercase tracking-wider text-red-400 mb-6 font-sans animate-fade-in">
            Data Investigation
          </div>
          <h1 className="text-6xl md:text-7xl font-bold mb-8 leading-tight" style={{
            animation: 'fadeInUp 0.8s ease-out',
            fontFamily: 'Playfair Display, Georgia, serif'
          }}>
            The Day the Group<br />Exploded
          </h1>
          <p className="text-xl md:text-2xl text-gray-300 mb-12 leading-relaxed" style={{
            animation: 'fadeInUp 0.8s ease-out 0.2s both',
            fontFamily: 'system-ui, sans-serif'
          }}>
            Inside the WhatsApp group that survived 24 years—until one member's 87 deleted messages
            revealed the hidden rules of digital community
          </p>
          <div className="flex items-center justify-center gap-8 text-sm" style={{
            animation: 'fadeInUp 0.8s ease-out 0.4s both',
            fontFamily: 'system-ui, sans-serif'
          }}>
            <div>
              <div className="text-3xl font-bold text-red-400">119</div>
              <div className="text-gray-400">Members</div>
            </div>
            <div className="text-gray-600">•</div>
            <div>
              <div className="text-3xl font-bold text-red-400">983</div>
              <div className="text-gray-400">Messages</div>
            </div>
            <div className="text-gray-600">•</div>
            <div>
              <div className="text-3xl font-bold text-red-400">545</div>
              <div className="text-gray-400">Days</div>
            </div>
          </div>
          <div className="mt-16 animate-bounce">
            <svg className="w-6 h-6 mx-auto text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
            </svg>
          </div>
        </div>
      </header>

      {/* Story Content */}
      <article className="bg-white">
        {/* Opening Scene */}
        <section className="max-w-3xl mx-auto px-6 py-24" data-section="opening">
          <div className={`transition-all duration-1000 ${isVisible('opening') ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
            <p className="text-xl leading-relaxed mb-8 first-letter:text-7xl first-letter:font-bold first-letter:mr-3 first-letter:float-left first-letter:text-red-600">
              On the morning of April 14, 2025, something strange happened in a WhatsApp group
              for Indian business school graduates. The group, which typically saw three messages
              a day, suddenly erupted. By the time the sun set over Mumbai, 77 messages had been
              exchanged—more than the previous three weeks combined.
            </p>

            <p className="text-lg leading-relaxed mb-6">
              This wasn't a reunion announcement. It wasn't tragic news. It was something far more
              revealing: a conflict over how much one person should be allowed to post.
            </p>

            <p className="text-lg leading-relaxed mb-6">
              The member in question—let's call him PC—had posted 21 messages that day. Over the
              previous 18 months, he had contributed 109 messages total. But here's what makes this
              story interesting: he had also deleted 87 of them.
            </p>

            <div className="my-12 p-8 bg-gray-50 border-l-4 border-red-600 italic text-lg">
              "PC is PC. Yesterday he keeps sending such long messages and today he deletes them."
              <span className="block mt-4 text-base not-italic text-gray-600">
                —Shivani Dwivedi, receiving 26 reactions (the most in group history)
              </span>
            </div>

            <p className="text-lg leading-relaxed mb-6">
              What happened next tells us something profound about how communities work—not just
              in WhatsApp groups, but in any space where people gather digitally. The rules, it
              turns out, only become visible when someone breaks them.
            </p>
          </div>
        </section>

        {/* Chapter 1: The April Explosion */}
        <section className="bg-gray-50 py-24" data-section="april">
          <div className="max-w-5xl mx-auto px-6">
            <h2 className="text-5xl font-bold mb-12 text-center" style={{ fontFamily: 'Playfair Display, Georgia, serif' }}>
              Chapter One: The Explosion
            </h2>

            <div className={`transition-all duration-1000 ${isVisible('april') ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
              <p className="text-lg leading-relaxed mb-8 max-w-3xl mx-auto">
                To understand what happened in April, you need to understand what normal looked like.
                For 18 months, this group of 119 IIM Bangalore alumni from the class of 2001 maintained
                a steady rhythm. A typical month saw 47 messages. A typical day saw three—or none at all.
              </p>

              <div className="bg-white rounded-lg shadow-lg p-8 mb-12">
                <h3 className="text-2xl font-bold mb-6 text-center" style={{ fontFamily: 'system-ui, sans-serif' }}>
                  The April Surge
                </h3>
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={aprilData}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" />
                    <XAxis
                      dataKey="date"
                      tick={{ fill: '#6b7280', fontSize: 12 }}
                      angle={-45}
                      textAnchor="end"
                      height={80}
                    />
                    <YAxis tick={{ fill: '#6b7280', fontSize: 12 }} />
                    <Tooltip content={<CustomTooltip />} />
                    <Bar dataKey="messages" radius={[8, 8, 0, 0]}>
                      {aprilData.map((entry, index) => (
                        <Cell
                          key={`cell-${index}`}
                          fill={entry.date === 'Apr 14' ? '#dc2626' : '#9ca3af'}
                        />
                      ))}
                    </Bar>
                    <ReferenceLine y={47} stroke="#3b82f6" strokeDasharray="3 3" label={{ value: 'Monthly Avg: 47', position: 'right', fill: '#3b82f6' }} />
                  </BarChart>
                </ResponsiveContainer>
                <p className="text-center text-sm text-gray-600 mt-4">
                  April 14: 77 messages—a 5.7x increase from the monthly average
                </p>
              </div>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                April 11 through 14 accounted for 198 messages—73% of the month's total activity.
                And at the center of it all was PC, who had posted 21 messages on April 14 alone.
                More than most members post in a year.
              </p>

              <div className="grid md:grid-cols-3 gap-6 my-12 max-w-4xl mx-auto">
                <div className="bg-white p-6 rounded-lg shadow-md text-center">
                  <div className="text-5xl font-bold text-red-600 mb-2">5.7×</div>
                  <div className="text-gray-600">Activity increase in April</div>
                </div>
                <div className="bg-white p-6 rounded-lg shadow-md text-center">
                  <div className="text-5xl font-bold text-red-600 mb-2">21</div>
                  <div className="text-gray-600">Messages from PC on April 14</div>
                </div>
                <div className="bg-white p-6 rounded-lg shadow-md text-center">
                  <div className="text-5xl font-bold text-red-600 mb-2">198</div>
                  <div className="text-gray-600">Messages in 4 days (Apr 11-14)</div>
                </div>
              </div>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                The group responded swiftly. Members who had been silent for months suddenly spoke up.
                By the end of April 14, the group had instituted a new rule: maximum four messages per day.
              </p>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                But here's the thing about rules: they only tell you what's allowed. They don't tell
                you what's expected. And the data reveals that PC's real violation wasn't quantity—it
                was something else entirely.
              </p>
            </div>
          </div>
        </section>

        {/* Chapter 2: The Silent Majority */}
        <section className="py-24" data-section="participation">
          <div className="max-w-5xl mx-auto px-6">
            <h2 className="text-5xl font-bold mb-12 text-center" style={{ fontFamily: 'Playfair Display, Georgia, serif' }}>
              Chapter Two: The 95-4-1 Rule
            </h2>

            <div className={`transition-all duration-1000 ${isVisible('participation') ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
              <p className="text-lg leading-relaxed mb-8 max-w-3xl mx-auto">
                Before we can understand what PC did wrong, we need to understand who was watching.
              </p>

              <p className="text-lg leading-relaxed mb-8 max-w-3xl mx-auto">
                In 2006, usability expert Jakob Nielsen identified what he called the "90-9-1 rule"
                of internet participation: 90% of users lurk, 9% contribute occasionally, and 1% create
                most of the content. This pattern has been observed across forums, social networks, and
                online communities for decades.
              </p>

              <p className="text-lg leading-relaxed mb-8 max-w-3xl mx-auto">
                The IIMB 2001 group doesn't follow this rule. It's more extreme.
              </p>

              <div className="bg-white rounded-lg shadow-lg p-8 mb-12">
                <h3 className="text-2xl font-bold mb-6 text-center" style={{ fontFamily: 'system-ui, sans-serif' }}>
                  Participation Inequality
                </h3>
                <ResponsiveContainer width="100%" height={350}>
                  <BarChart data={participationData} layout="vertical" margin={{ left: 100 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" />
                    <XAxis type="number" tick={{ fill: '#6b7280', fontSize: 12 }} />
                    <YAxis
                      dataKey="category"
                      type="category"
                      tick={{ fill: '#6b7280', fontSize: 12 }}
                      width={90}
                    />
                    <Tooltip content={<CustomTooltip />} />
                    <Bar dataKey="users" fill="#dc2626" radius={[0, 8, 8, 0]} />
                  </BarChart>
                </ResponsiveContainer>
                <p className="text-center text-sm text-gray-600 mt-4">
                  70% of members posted ≤5 messages over 18 months
                </p>
              </div>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                Thirty-one members posted exactly once. Their debut was their finale. Another 52 members
                posted between two and five times—less than once per quarter. Together, these 83 people
                represent 70% of the group.
              </p>

              <div className="my-12 p-8 bg-red-50 border-l-4 border-red-600">
                <p className="text-xl font-bold mb-4 text-red-900">The median member posted twice.</p>
                <p className="text-lg text-red-800">
                  That means half the group posted fewer than two messages in 18 months. Yet they
                  stayed. They read. They watched. And when PC's posting behavior crossed an invisible
                  line, they responded.
                </p>
              </div>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                This matters because lurkers aren't passive. They're the audience. They're the jury.
                And in April 2025, they delivered a verdict.
              </p>
            </div>
          </div>
        </section>

        {/* Chapter 3: The Deletion Pattern */}
        <section className="bg-gray-50 py-24" data-section="deletion">
          <div className="max-w-5xl mx-auto px-6">
            <h2 className="text-5xl font-bold mb-12 text-center" style={{ fontFamily: 'Playfair Display, Georgia, serif' }}>
              Chapter Three: The 44% Solution
            </h2>

            <div className={`transition-all duration-1000 ${isVisible('deletion') ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
              <p className="text-lg leading-relaxed mb-8 max-w-3xl mx-auto">
                Here's where the story gets interesting. PC didn't just post more than anyone else.
                He deleted more than everyone else combined.
              </p>

              <p className="text-lg leading-relaxed mb-8 max-w-3xl mx-auto">
                Of the 106 messages deleted from the group over 18 months, 87 came from PC. That's
                82% of all deletions. But the more revealing number is this: PC deleted 87 of his
                196 total messages—a deletion rate of 44.4%.
              </p>

              <div className="bg-white rounded-lg shadow-lg p-8 mb-12">
                <h3 className="text-2xl font-bold mb-6 text-center" style={{ fontFamily: 'system-ui, sans-serif' }}>
                  Deletion Rates: PC vs. Group
                </h3>
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={deletionData}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" />
                    <XAxis
                      dataKey="user"
                      tick={{ fill: '#6b7280', fontSize: 12 }}
                    />
                    <YAxis
                      tick={{ fill: '#6b7280', fontSize: 12 }}
                      label={{ value: 'Deletion Rate (%)', angle: -90, position: 'insideLeft', fill: '#6b7280' }}
                    />
                    <Tooltip content={<CustomTooltip />} />
                    <Bar dataKey="rate" radius={[8, 8, 0, 0]}>
                      {deletionData.map((entry, index) => (
                        <Cell
                          key={`cell-${index}`}
                          fill={entry.user === 'PC' ? '#dc2626' : '#9ca3af'}
                        />
                      ))}
                    </Bar>
                  </BarChart>
                </ResponsiveContainer>
                <p className="text-center text-sm text-gray-600 mt-4">
                  PC's deletion rate is 44x higher than the group average
                </p>
              </div>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                For context: the rest of the group deleted 19 messages out of 1,896—a deletion rate
                of 1%. PC's rate wasn't just higher. It was astronomically higher. Forty-four times
                higher.
              </p>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                This pattern suggests something beyond mere second thoughts. It suggests a cycle:
                post, receive feedback (or silence), delete, repeat. One member captured it perfectly:
                "Yesterday he keeps sending such long messages and today he deletes them."
              </p>

              <div className="my-12 grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
                <div className="bg-white p-8 rounded-lg shadow-md">
                  <div className="text-4xl font-bold text-red-600 mb-4">87</div>
                  <div className="text-lg font-semibold mb-2">Messages Deleted by PC</div>
                  <div className="text-gray-600">82% of all group deletions</div>
                </div>
                <div className="bg-white p-8 rounded-lg shadow-md">
                  <div className="text-4xl font-bold text-gray-600 mb-4">19</div>
                  <div className="text-lg font-semibold mb-2">Messages Deleted by Everyone Else</div>
                  <div className="text-gray-600">Out of 118 other members</div>
                </div>
              </div>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                The deletion pattern revealed something crucial: PC knew he was crossing a line.
                The deletions were a form of self-correction, an attempt to undo what had already
                been seen. But in a WhatsApp group, deletion doesn't mean forgetting. It means
                everyone knows you regretted it.
              </p>
            </div>
          </div>
        </section>

        {/* Chapter 4: The Engagement Void */}
        <section className="py-24" data-section="engagement">
          <div className="max-w-5xl mx-auto px-6">
            <h2 className="text-5xl font-bold mb-12 text-center" style={{ fontFamily: 'Playfair Display, Georgia, serif' }}>
              Chapter Four: Zero
            </h2>

            <div className={`transition-all duration-1000 ${isVisible('engagement') ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
              <p className="text-lg leading-relaxed mb-8 max-w-3xl mx-auto">
                But PC's real violation wasn't quantity. It wasn't even the deletions. It was this:
                nobody engaged with his content.
              </p>

              <p className="text-lg leading-relaxed mb-8 max-w-3xl mx-auto">
                In WhatsApp groups, engagement takes the form of reactions—emoji responses that signal
                appreciation, agreement, or amusement. The group average was 0.78 reactions per message.
                Some members did better: Rajesh Bhura averaged 2.4 reactions per message. Pawan Bhargava,
                who posted 61 messages (the same as PC), averaged 1.56.
              </p>

              <p className="text-lg leading-relaxed mb-8 max-w-3xl mx-auto">
                PC averaged zero.
              </p>

              <div className="bg-white rounded-lg shadow-lg p-8 mb-12">
                <h3 className="text-2xl font-bold mb-6 text-center" style={{ fontFamily: 'system-ui, sans-serif' }}>
                  Messages vs. Engagement
                </h3>
                <ResponsiveContainer width="100%" height={400}>
                  <ScatterChart margin={{ top: 20, right: 20, bottom: 60, left: 60 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" />
                    <XAxis
                      dataKey="messages"
                      type="number"
                      tick={{ fill: '#6b7280', fontSize: 12 }}
                      label={{ value: 'Messages Posted', position: 'bottom', fill: '#6b7280', offset: 40 }}
                    />
                    <YAxis
                      dataKey="reactions"
                      type="number"
                      tick={{ fill: '#6b7280', fontSize: 12 }}
                      label={{ value: 'Avg Reactions per Message', angle: -90, position: 'insideLeft', fill: '#6b7280' }}
                    />
                    <Tooltip
                      content={({ active, payload }) => {
                        if (active && payload && payload[0]) {
                          const data = payload[0].payload;
                          return (
                            <div className="bg-gray-900 text-white px-4 py-2 rounded shadow-lg">
                              <p className="font-medium">{data.name}</p>
                              <p className="text-sm">{data.messages} messages, {data.reactions} avg reactions</p>
                            </div>
                          );
                        }
                        return null;
                      }}
                    />
                    <Scatter data={engagementData}>
                      {engagementData.map((entry, index) => (
                        <Cell
                          key={`cell-${index}`}
                          fill={entry.category === 'None' ? '#dc2626' : entry.category === 'High' ? '#10b981' : entry.category === 'Medium' ? '#3b82f6' : '#9ca3af'}
                          r={8}
                        />
                      ))}
                    </Scatter>
                    <ReferenceLine y={0.78} stroke="#9ca3af" strokeDasharray="3 3" label={{ value: 'Group Avg', position: 'right', fill: '#9ca3af' }} />
                  </ScatterChart>
                </ResponsiveContainer>
                <p className="text-center text-sm text-gray-600 mt-4">
                  PC (red dot, far right): 61 messages, 0.00 reactions
                </p>
              </div>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                Not low. Not below average. Zero. Across 61 messages spanning 18 months, PC received
                not a single reaction from his peers.
              </p>

              <div className="my-12 p-8 bg-red-50 border-l-4 border-red-600">
                <p className="text-xl font-bold mb-4 text-red-900">
                  This wasn't indifference. It was active disengagement.
                </p>
                <p className="text-lg text-red-800">
                  When someone posts and nobody responds, that's apathy. When someone posts 61 times
                  and nobody ever responds, that's a message.
                </p>
              </div>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                Compare this to Pawan Bhargava, who posted the same number of messages (61) but
                received 95 total reactions—1.56 per message. Or Rajesh Bhura, who posted just 15
                messages but received 36 reactions—2.4 per message.
              </p>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                The data reveals something that felt true to the members but had never been quantified:
                PC's content didn't land. Not because of volume—other active members were celebrated.
                But because of something else.
              </p>
            </div>
          </div>
        </section>

        {/* Chapter 5: Personal > Professional */}
        <section className="bg-gray-50 py-24" data-section="content">
          <div className="max-w-5xl mx-auto px-6">
            <h2 className="text-5xl font-bold mb-12 text-center" style={{ fontFamily: 'Playfair Display, Georgia, serif' }}>
              Chapter Five: What Works
            </h2>

            <div className={`transition-all duration-1000 ${isVisible('content') ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
              <p className="text-lg leading-relaxed mb-8 max-w-3xl mx-auto">
                So what kind of content did the group want? The data is unambiguous.
              </p>

              <div className="bg-white rounded-lg shadow-lg p-8 mb-12">
                <h3 className="text-2xl font-bold mb-6 text-center" style={{ fontFamily: 'system-ui, sans-serif' }}>
                  Reactions by Content Type
                </h3>
                <ResponsiveContainer width="100%" height={350}>
                  <BarChart data={contentTypeData}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" />
                    <XAxis
                      dataKey="type"
                      tick={{ fill: '#6b7280', fontSize: 11 }}
                      interval={0}
                      height={80}
                    />
                    <YAxis
                      tick={{ fill: '#6b7280', fontSize: 12 }}
                      label={{ value: 'Avg Reactions', angle: -90, position: 'insideLeft', fill: '#6b7280' }}
                    />
                    <Tooltip content={<CustomTooltip />} />
                    <Bar dataKey="reactions" fill="#10b981" radius={[8, 8, 0, 0]} />
                    <ReferenceLine y={0.68} stroke="#dc2626" strokeDasharray="3 3" label={{ value: 'Baseline', position: 'right', fill: '#dc2626' }} />
                  </BarChart>
                </ResponsiveContainer>
                <p className="text-center text-sm text-gray-600 mt-4">
                  Media posts received 4x more reactions than text-only content
                </p>
              </div>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                Messages with media—photos, videos, GIFs—averaged 2.76 reactions. That's 306% higher
                than the baseline. Forwarded content performed similarly well, at 2.71 reactions.
              </p>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                But original replies—the kind of thoughtful, substantive responses PC specialized in—
                averaged just 0.29 reactions. Long-form text posts (more than 200 characters) averaged
                0.72 reactions.
              </p>

              <div className="my-12 max-w-3xl mx-auto">
                <h3 className="text-2xl font-bold mb-6" style={{ fontFamily: 'system-ui, sans-serif' }}>
                  The Top 5 Most-Reacted Posts:
                </h3>
                <div className="space-y-4">
                  <div className="bg-white p-6 rounded-lg shadow-md border-l-4 border-green-500">
                    <div className="flex justify-between items-start mb-2">
                      <div className="font-semibold">Shivani Dwivedi</div>
                      <div className="text-green-600 font-bold">26 reactions</div>
                    </div>
                    <div className="text-gray-700">Son joining IIMB PhD program (personal milestone)</div>
                  </div>
                  <div className="bg-white p-6 rounded-lg shadow-md border-l-4 border-green-500">
                    <div className="flex justify-between items-start mb-2">
                      <div className="font-semibold">Pawan Bhargava</div>
                      <div className="text-green-600 font-bold">21 reactions</div>
                    </div>
                    <div className="text-gray-700">Reunion photo with classmate from Dallas (personal connection)</div>
                  </div>
                  <div className="bg-white p-6 rounded-lg shadow-md border-l-4 border-green-500">
                    <div className="flex justify-between items-start mb-2">
                      <div className="font-semibold">Sunil Rai</div>
                      <div className="text-green-600 font-bold">19 reactions</div>
                    </div>
                    <div className="text-gray-700">Long-overdue reunion photos (nostalgia)</div>
                  </div>
                  <div className="bg-white p-6 rounded-lg shadow-md border-l-4 border-green-500">
                    <div className="flex justify-between items-start mb-2">
                      <div className="font-semibold">Pawan Bhargava</div>
                      <div className="text-green-600 font-bold">17 reactions</div>
                    </div>
                    <div className="text-gray-700">Half marathon completion (athletic achievement)</div>
                  </div>
                  <div className="bg-white p-6 rounded-lg shadow-md border-l-4 border-green-500">
                    <div className="flex justify-between items-start mb-2">
                      <div className="font-semibold">Lokesh Garg</div>
                      <div className="text-green-600 font-bold">16 reactions</div>
                    </div>
                    <div className="text-gray-700">Classmate summiting Mt. Everest (extreme achievement)</div>
                  </div>
                </div>
              </div>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                Notice a pattern? Every top post is about personal life—children, fitness, reunions,
                extraordinary achievements. None are about business. None are about current events.
                None are long analytical pieces about geopolitics or economics.
              </p>

              <div className="my-12 p-8 bg-green-50 border-l-4 border-green-600">
                <p className="text-xl font-bold mb-4 text-green-900">
                  Personal &gt; Professional
                </p>
                <p className="text-lg text-green-800">
                  This is an alumni group from a business school, filled with successful executives
                  and entrepreneurs. Yet personal milestones outperformed business updates by a factor
                  of four. The group's implicit identity wasn't "professional network"—it was
                  "friends keeping in touch."
                </p>
              </div>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                PC's content—long, analytical, focused on world affairs and abstract ideas—wasn't
                wrong. It was off-brand. He was posting LinkedIn content to a group that wanted
                Facebook vibes.
              </p>
            </div>
          </div>
        </section>

        {/* Chapter 6: The Invisible Architect */}
        <section className="py-24" data-section="architect">
          <div className="max-w-5xl mx-auto px-6">
            <h2 className="text-5xl font-bold mb-12 text-center" style={{ fontFamily: 'Playfair Display, Georgia, serif' }}>
              Chapter Six: The Man Who Starts Conversations
            </h2>

            <div className={`transition-all duration-1000 ${isVisible('architect') ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
              <p className="text-lg leading-relaxed mb-8 max-w-3xl mx-auto">
                While PC was learning painful lessons about community dynamics, another member was
                quietly doing the work that kept the group alive.
              </p>

              <p className="text-lg leading-relaxed mb-8 max-w-3xl mx-auto">
                Somnath Manna posted 66 messages over 18 months—making him the group's most prolific
                contributor. But here's what makes him interesting: he posted 30% of all conversation
                starters. Messages that broke long silences. Posts that came after 12-hour gaps when
                the group had gone quiet.
              </p>

              <div className="my-12 grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
                <div className="bg-white p-8 rounded-lg shadow-lg">
                  <div className="text-5xl font-bold text-blue-600 mb-4">30%</div>
                  <div className="text-xl font-semibold mb-2">Of conversation starts</div>
                  <div className="text-gray-600">35 out of 118 conversations initiated by Somnath after silence</div>
                </div>
                <div className="bg-white p-8 rounded-lg shadow-lg">
                  <div className="text-5xl font-bold text-blue-600 mb-4">28%</div>
                  <div className="text-xl font-semibold mb-2">Of conversation endings</div>
                  <div className="text-gray-600">33 of his posts were followed by 12+ hours of silence</div>
                </div>
              </div>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                Somnath's role is subtle but crucial. He shares reunion photos. He posts administrative
                updates about alumni events. He breaks the ice with a question or observation. And then
                he steps back and lets others take the conversation wherever it needs to go.
              </p>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                His engagement rate—0.76 reactions per message—is below the group average. But that's
                not the point. His content isn't designed to be the most engaging. It's designed to
                create space for engagement.
              </p>

              <div className="my-12 p-8 bg-blue-50 border-l-4 border-blue-600">
                <p className="text-xl font-bold mb-4 text-blue-900">
                  Every community needs someone willing to post into the void.
                </p>
                <p className="text-lg text-blue-800">
                  Most super-contributors dominate conversations. Somnath enables them. Without his
                  conversation starters, the group would likely have 30-40% fewer active days. He's
                  not the loudest voice in the room. He's the person who makes sure there's a
                  conversation to join.
                </p>
              </div>

              <p className="text-lg leading-relaxed mb-6 max-w-3xl mx-auto">
                This creates a dependency risk. Somnath is a single point of failure. If he stopped
                posting, would someone else fill the void? Or would the group slide into permanent
                dormancy? The data can't tell us. But it's a question worth asking.
              </p>
            </div>
          </div>
        </section>

        {/* Epilogue */}
        <section className="bg-gray-900 text-white py-24" data-section="epilogue">
          <div className="max-w-3xl mx-auto px-6">
            <h2 className="text-5xl font-bold mb-12 text-center" style={{ fontFamily: 'Playfair Display, Georgia, serif' }}>
              Epilogue: What It All Means
            </h2>

            <div className={`transition-all duration-1000 ${isVisible('epilogue') ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
              <p className="text-xl leading-relaxed mb-8">
                Twenty-four years after graduating from IIM Bangalore, 119 people still choose to stay
                in this WhatsApp group. Most of them barely post. Some have posted only once. The group
                is silent 75% of the time.
              </p>

              <p className="text-xl leading-relaxed mb-8">
                And yet, they stay.
              </p>

              <p className="text-lg leading-relaxed mb-8 text-gray-300">
                The April 2025 controversy revealed something profound: communities don't need constant
                activity to be meaningful. They need the right kind of activity at the right time. They
                need shared understanding of what belongs and what doesn't—even if that understanding
                is never articulated until someone violates it.
              </p>

              <p className="text-lg leading-relaxed mb-8 text-gray-300">
                PC posted 21 messages on April 14, and the group erupted. But it wasn't just about
                quantity. Pawan posted 61 messages over 18 months and was celebrated. The difference
                was fit: Pawan posted reunion photos and personal milestones. PC posted long analytical
                texts about geopolitics.
              </p>

              <p className="text-lg leading-relaxed mb-8 text-gray-300">
                PC deleted 87 messages—44% of everything he posted—and received zero reactions across
                109 total messages. These aren't just numbers. They're a story about what happens when
                someone misreads the room at scale.
              </p>

              <div className="my-12 p-8 bg-gray-800 rounded-lg border-l-4 border-red-500">
                <p className="text-2xl font-bold mb-4 text-red-400">
                  The invisible rules only become visible when someone breaks them.
                </p>
                <p className="text-lg text-gray-300">
                  For 18 months, the group operated on implicit understandings: Post occasionally.
                  Share personal updates. Don't dominate. Don't lecture. These rules were nowhere
                  written. They emerged from collective behavior. And when PC violated them, the
                  community responded not with malice but with clarity: "Four messages per day."
                </p>
              </div>

              <p className="text-lg leading-relaxed mb-8 text-gray-300">
                But here's the thing: groups like this aren't anomalies. They're everywhere. Alumni
                networks, family chats, friend groups, work channels—all operating on invisible norms,
                sustained by a few active members, watched by a silent majority that only speaks up
                when something goes wrong.
              </p>

              <p className="text-lg leading-relaxed mb-8 text-gray-300">
                The IIMB 2001 group works not because it's perfectly designed or optimally engaged.
                It works because it's good enough. It maintains a background connection that can be
                activated when needed. Most of the time, that means silence. Occasionally, it means
                a burst of 77 messages in a single day.
              </p>

              <p className="text-xl leading-relaxed mb-8">
                Twenty-four years on, they're still there. Still lurking. Still watching. Still waiting
                for the right moment to speak up.
              </p>

              <p className="text-xl leading-relaxed mb-8">
                And when that moment comes—when someone posts a reunion photo or shares news about
                their child or announces something extraordinary—they respond. Not with essays. Not
                with analysis. But with something simpler: a thumbs up. A heart. A brief comment.
              </p>

              <p className="text-xl leading-relaxed font-bold">
                Because sometimes, that's all a community needs.
              </p>
            </div>
          </div>
        </section>

        {/* Methodology */}
        <section className="bg-white py-16 border-t border-gray-200">
          <div className="max-w-3xl mx-auto px-6">
            <h3 className="text-2xl font-bold mb-6" style={{ fontFamily: 'system-ui, sans-serif' }}>
              Methodology & Limitations
            </h3>

            <div className="text-sm text-gray-600 space-y-4" style={{ fontFamily: 'system-ui, sans-serif' }}>
              <p>
                <strong>Data Source:</strong> This analysis is based on 983 messages from the IIMB 2001
                Global WhatsApp group spanning April 1, 2024 to September 28, 2025 (545 days). System
                messages and recalled (deleted) messages were excluded from most analyses.
              </p>

              <p>
                <strong>Participation metrics:</strong> Calculated from message counts, reaction data,
                and temporal patterns. The 95-4-1 characterization is derived from the distribution of
                message counts across 119 unique participants.
              </p>

              <p>
                <strong>Engagement analysis:</strong> Based on WhatsApp reaction data, which tracks emoji
                responses to messages. Average reactions per message were calculated for each user and
                content type.
              </p>

              <p>
                <strong>Key limitations:</strong>
              </p>
              <ul className="list-disc pl-6 space-y-2">
                <li>
                  <strong>Survivorship bias:</strong> We only have data from members who remained in the
                  group. Members who left are not represented, potentially biasing findings toward those
                  who tolerated or approved of group dynamics.
                </li>
                <li>
                  <strong>Deleted content:</strong> We know which messages were deleted and by whom, but
                  not the content of deleted messages, limiting our ability to understand what prompted
                  deletions.
                </li>
                <li>
                  <strong>External context:</strong> We lack information about communication happening
                  outside the group (private messages, other platforms, in-person conversations) that may
                  have influenced group dynamics.
                </li>
                <li>
                  <strong>Causation:</strong> While we can identify correlations (e.g., PC's posting
                  preceded the April spike), we cannot definitively establish causation without additional
                  data.
                </li>
                <li>
                  <strong>Generalizability:</strong> These findings represent one group from one cohort
                  at one institution. Patterns may not apply to other contexts.
                </li>
              </ul>

              <p>
                <strong>Cross-validation:</strong> Participation patterns were compared against published
                research on online community engagement, including Nielsen's 90-9-1 rule and subsequent
                studies. The IIMB 2001 group's patterns fall within known ranges but toward the more
                extreme end of the participation inequality spectrum.
              </p>

              <p>
                <strong>Tools:</strong> Analysis conducted using Python (pandas, numpy) for data processing
                and statistical analysis. Visualizations created using Recharts in React.
              </p>
            </div>
          </div>
        </section>

        {/* Footer */}
        <footer className="bg-gray-900 text-gray-400 py-8">
          <div className="max-w-3xl mx-auto px-6 text-center text-sm" style={{ fontFamily: 'system-ui, sans-serif' }}>
            <p>Data analysis period: April 1, 2024 – September 28, 2025</p>
            <p className="mt-2">983 messages • 119 participants • 545 days</p>
            <p className="mt-4 text-xs text-gray-500">
              Names have been pseudonymized except where discussing aggregate patterns
            </p>
          </div>
        </footer>
      </article>

      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&display=swap');

        @keyframes fadeInUp {
          from {
            opacity: 0;
            transform: translateY(30px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        @keyframes fadeIn {
          from {
            opacity: 0;
          }
          to {
            opacity: 1;
          }
        }

        .animate-fade-in {
          animation: fadeIn 1s ease-out;
        }

        html {
          scroll-behavior: smooth;
        }
      `}</style>
    </div>
  );
};

// Expose for inline bootstrap script
window.WhatsAppStory = WhatsAppStory;
