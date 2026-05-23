import {AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate, Sequence, spring} from 'remotion';
import {loadFont as loadAnton} from '@remotion/google-fonts/Anton';
import {loadFont as loadPlayfair} from '@remotion/google-fonts/PlayfairDisplay';

const {fontFamily: ANTON} = loadAnton();
const {fontFamily: PLAYFAIR} = loadPlayfair('normal', {weights: ['900'], subsets: ['latin']});

const TEAL = '#2A7A6D';
const TEAL_BRIGHT = '#3FA08F';

const FPS = 30;

const CHAR_FRAMES = 1.6;

type Line = {
  text: string;
  size: number;
  color?: string;
  italic?: boolean;
  font?: string;
  letterSpacing?: string;
  gapAfter?: number;
};

const CharReveal: React.FC<{
  char: string;
  enterAt: number;
  localFrame: number;
}> = ({char, enterAt, localFrame}) => {
  const dt = localFrame - enterAt;
  if (dt < 0) return <span style={{opacity: 0}}>{char === ' ' ? ' ' : char}</span>;

  const pop = interpolate(dt, [0, 2, 5], [1.18, 1.02, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const opacity = interpolate(dt, [0, 2], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <span
      style={{
        display: 'inline-block',
        transform: `scale(${pop})`,
        opacity,
        whiteSpace: 'pre',
      }}
    >
      {char === ' ' ? ' ' : char}
    </span>
  );
};

const TypedLine: React.FC<{
  line: Line;
  startFrame: number;
  localFrame: number;
  showCaret?: boolean;
  caretActiveTo?: number;
}> = ({line, startFrame, localFrame, showCaret = true, caretActiveTo}) => {
  const chars = line.text.split('');
  const finishAt = startFrame + chars.length * CHAR_FRAMES;
  const caretCutoff = caretActiveTo ?? finishAt + 24;

  const caretVisible =
    localFrame >= startFrame &&
    localFrame <= caretCutoff &&
    Math.floor((localFrame - startFrame) / 8) % 2 === 0;

  return (
    <div
      style={{
        fontFamily: line.font ?? ANTON,
        fontSize: line.size,
        color: line.color ?? '#fff',
        textAlign: 'center',
        lineHeight: 0.98,
        letterSpacing: line.letterSpacing ?? '0.005em',
        textTransform: line.italic ? 'none' : 'uppercase',
        fontStyle: line.italic ? 'italic' : 'normal',
        fontWeight: line.italic ? 900 : 400,
        marginBottom: line.gapAfter ?? 16,
        whiteSpace: 'nowrap',
      }}
    >
      {chars.map((c, i) => (
        <CharReveal
          key={i}
          char={c}
          enterAt={startFrame + i * CHAR_FRAMES}
          localFrame={localFrame}
        />
      ))}
      <span
        style={{
          display: 'inline-block',
          width: '0.08em',
          marginLeft: '0.04em',
          height: `${line.size * 0.78}px`,
          verticalAlign: 'middle',
          background: line.color ?? '#fff',
          opacity: caretVisible ? 1 : 0,
          transform: 'translateY(-6%)',
        }}
      />
    </div>
  );
};

const TypewriterShot: React.FC<{
  lines: Line[];
  duration: number;
  postFlash?: boolean;
}> = ({lines, duration, postFlash = false}) => {
  const localFrame = useCurrentFrame();

  const lineStarts: number[] = [];
  let cursor = 4;
  for (const l of lines) {
    lineStarts.push(cursor);
    cursor += l.text.length * CHAR_FRAMES + 8;
  }
  const lastFinish = lineStarts[lines.length - 1] + lines[lines.length - 1].text.length * CHAR_FRAMES;

  const fadeOut = interpolate(localFrame, [duration - 5, duration], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const flashOpacity = postFlash
    ? interpolate(localFrame, [duration - 8, duration - 4, duration], [0, 0.6, 0], {
        extrapolateLeft: 'clamp',
        extrapolateRight: 'clamp',
      })
    : 0;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#000',
        justifyContent: 'center',
        alignItems: 'center',
        flexDirection: 'column',
        padding: '0 100px',
        opacity: fadeOut,
      }}
    >
      {lines.map((line, i) => (
        <TypedLine
          key={i}
          line={line}
          startFrame={lineStarts[i]}
          localFrame={localFrame}
          showCaret={i === lines.length - 1}
          caretActiveTo={lastFinish + 18}
        />
      ))}
      <AbsoluteFill
        style={{
          backgroundColor: TEAL_BRIGHT,
          opacity: flashOpacity,
          mixBlendMode: 'screen',
          pointerEvents: 'none',
        }}
      />
    </AbsoluteFill>
  );
};

const MegaTypewriter: React.FC<{duration: number}> = ({duration}) => {
  const localFrame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const text = '$25,000';
  const chars = text.split('');
  const startFrame = 6;
  const finishAt = startFrame + chars.length * 2.2;

  const breathe = 1 + Math.sin(localFrame / 7) * 0.015;

  const glowRamp = interpolate(localFrame, [finishAt, finishAt + 14], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const fadeOut = interpolate(localFrame, [duration - 5, duration], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const caretVisible =
    localFrame >= startFrame &&
    localFrame <= finishAt + 18 &&
    Math.floor((localFrame - startFrame) / 8) % 2 === 0;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#000',
        justifyContent: 'center',
        alignItems: 'center',
        flexDirection: 'column',
        opacity: fadeOut,
      }}
    >
      <div
        style={{
          fontFamily: ANTON,
          fontSize: 440,
          color: TEAL_BRIGHT,
          letterSpacing: '-0.02em',
          textTransform: 'uppercase',
          lineHeight: 0.95,
          transform: `scale(${breathe})`,
          textShadow: `0 0 ${60 + glowRamp * 80}px ${TEAL_BRIGHT}${glowRamp > 0.5 ? '99' : '55'}, 0 0 ${120 + glowRamp * 120}px ${TEAL_BRIGHT}${glowRamp > 0.5 ? '55' : '22'}`,
          whiteSpace: 'nowrap',
        }}
      >
        {chars.map((c, i) => (
          <CharReveal
            key={i}
            char={c}
            enterAt={startFrame + i * 2.2}
            localFrame={localFrame}
          />
        ))}
        <span
          style={{
            display: 'inline-block',
            width: '0.08em',
            marginLeft: '0.04em',
            height: '340px',
            verticalAlign: 'middle',
            background: TEAL_BRIGHT,
            opacity: caretVisible ? 1 : 0,
            transform: 'translateY(-6%)',
          }}
        />
      </div>
      <div
        style={{
          fontFamily: ANTON,
          fontSize: 72,
          color: 'rgba(255,255,255,0.85)',
          letterSpacing: '0.04em',
          textTransform: 'uppercase',
          marginTop: 30,
          opacity: glowRamp,
        }}
      >
        EXTRA REVENUE
      </div>
    </AbsoluteFill>
  );
};

const FinalCta: React.FC<{duration: number}> = ({duration}) => {
  const localFrame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const line1Start = 4;
  const line1Text = "TODAY'S EDITION:";
  const line1End = line1Start + line1Text.length * CHAR_FRAMES;

  const line2Start = line1End + 8;
  const line2Text = 'THE FULL PLAYBOOK.';
  const line2End = line2Start + line2Text.length * CHAR_FRAMES;

  const urlStart = line2End + 14;
  const urlText = 'thebillionperson.com';

  const urlSpring = spring({
    frame: Math.max(0, localFrame - urlStart),
    fps,
    config: {damping: 12, stiffness: 130, mass: 0.6},
  });
  const urlScale = interpolate(urlSpring, [0, 1], [0.7, 1]);
  const urlOpacity = interpolate(localFrame, [urlStart, urlStart + 12], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const urlPulse = 1 + Math.sin((localFrame - urlStart) / 8) * 0.02;

  const caret1Visible =
    localFrame >= line1Start &&
    localFrame <= line2Start - 2 &&
    Math.floor((localFrame - line1Start) / 8) % 2 === 0;

  const caret2Visible =
    localFrame >= line2Start &&
    localFrame <= urlStart - 2 &&
    Math.floor((localFrame - line2Start) / 8) % 2 === 0;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#000',
        justifyContent: 'center',
        alignItems: 'center',
        flexDirection: 'column',
      }}
    >
      <div
        style={{
          fontFamily: ANTON,
          fontSize: 86,
          color: '#fff',
          letterSpacing: '0.04em',
          textTransform: 'uppercase',
          marginBottom: 24,
          whiteSpace: 'nowrap',
        }}
      >
        {line1Text.split('').map((c, i) => (
          <CharReveal key={i} char={c} enterAt={line1Start + i * CHAR_FRAMES} localFrame={localFrame} />
        ))}
        <span
          style={{
            display: 'inline-block',
            width: '0.08em',
            marginLeft: '0.04em',
            height: '70px',
            verticalAlign: 'middle',
            background: '#fff',
            opacity: caret1Visible ? 1 : 0,
            transform: 'translateY(-6%)',
          }}
        />
      </div>

      <div
        style={{
          fontFamily: ANTON,
          fontSize: 170,
          color: TEAL_BRIGHT,
          letterSpacing: '-0.01em',
          textTransform: 'uppercase',
          marginBottom: 70,
          lineHeight: 0.95,
          whiteSpace: 'nowrap',
        }}
      >
        {line2Text.split('').map((c, i) => (
          <CharReveal key={i} char={c} enterAt={line2Start + i * CHAR_FRAMES} localFrame={localFrame} />
        ))}
        <span
          style={{
            display: 'inline-block',
            width: '0.08em',
            marginLeft: '0.04em',
            height: '140px',
            verticalAlign: 'middle',
            background: TEAL_BRIGHT,
            opacity: caret2Visible ? 1 : 0,
            transform: 'translateY(-6%)',
          }}
        />
      </div>

      <div
        style={{
          fontFamily: PLAYFAIR,
          fontWeight: 900,
          fontStyle: 'italic',
          fontSize: 130,
          color: '#fff',
          letterSpacing: '-0.02em',
          transform: `scale(${urlScale * urlPulse})`,
          opacity: urlOpacity,
          textShadow: `0 0 60px ${TEAL_BRIGHT}66`,
          whiteSpace: 'nowrap',
        }}
      >
        {urlText}
      </div>
    </AbsoluteFill>
  );
};

const Vignette: React.FC = () => (
  <AbsoluteFill
    style={{
      background: 'radial-gradient(circle at center, transparent 60%, rgba(0,0,0,0.45) 100%)',
      pointerEvents: 'none',
    }}
  />
);

const Grain: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill
      style={{
        opacity: 0.04,
        mixBlendMode: 'overlay',
        backgroundImage: `radial-gradient(circle at ${20 + (frame % 35)}% ${30 + (frame % 28)}%, white 1px, transparent 2px)`,
        backgroundSize: '6px 6px',
        pointerEvents: 'none',
      }}
    />
  );
};

const SHOT_DURATIONS = [
  44,
  44,
  60,
  40,
  40,
  40,
  74,
  40,
  10,
  60,
  40,
  44,
  60,
  130,
];

const SHOT_STARTS: number[] = [];
{
  let acc = 0;
  for (const d of SHOT_DURATIONS) {
    SHOT_STARTS.push(acc);
    acc += d;
  }
}

const TOTAL_FRAMES = SHOT_DURATIONS.reduce((a, b) => a + b, 0);
export const PRE_CTA_DURATION = TOTAL_FRAMES;

export const PreCtaGoogle: React.FC = () => {
  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      <Sequence from={SHOT_STARTS[0]} durationInFrames={SHOT_DURATIONS[0]}>
        <TypewriterShot
          duration={SHOT_DURATIONS[0]}
          postFlash
          lines={[{text: '$108', size: 460, color: TEAL_BRIGHT, letterSpacing: '-0.02em'}]}
        />
      </Sequence>

      <Sequence from={SHOT_STARTS[1]} durationInFrames={SHOT_DURATIONS[1]}>
        <TypewriterShot
          duration={SHOT_DURATIONS[1]}
          lines={[{text: 'BILLION.', size: 380, color: '#fff', letterSpacing: '-0.005em'}]}
        />
      </Sequence>

      <Sequence from={SHOT_STARTS[2]} durationInFrames={SHOT_DURATIONS[2]}>
        <TypewriterShot
          duration={SHOT_DURATIONS[2]}
          lines={[
            {
              text: 'A market quietly',
              size: 64,
              color: 'rgba(255,255,255,0.85)',
              italic: true,
              letterSpacing: '0.01em',
              gapAfter: 28,
            },
            {text: 'DOUBLES BY 2030.', size: 200, color: TEAL_BRIGHT, letterSpacing: '-0.01em'},
          ]}
        />
      </Sequence>

      <Sequence from={SHOT_STARTS[3]} durationInFrames={SHOT_DURATIONS[3]}>
        <TypewriterShot
          duration={SHOT_DURATIONS[3]}
          lines={[{text: 'ONE FOUNDER.', size: 260, color: '#fff'}]}
        />
      </Sequence>

      <Sequence from={SHOT_STARTS[4]} durationInFrames={SHOT_DURATIONS[4]}>
        <TypewriterShot
          duration={SHOT_DURATIONS[4]}
          lines={[{text: '8 PROMPTS.', size: 320, color: TEAL_BRIGHT, letterSpacing: '-0.01em'}]}
        />
      </Sequence>

      <Sequence from={SHOT_STARTS[5]} durationInFrames={SHOT_DURATIONS[5]}>
        <TypewriterShot
          duration={SHOT_DURATIONS[5]}
          lines={[{text: 'ONE PLUMBER.', size: 260, color: '#fff'}]}
          postFlash
        />
      </Sequence>

      <Sequence from={SHOT_STARTS[6]} durationInFrames={SHOT_DURATIONS[6]}>
        <MegaTypewriter duration={SHOT_DURATIONS[6]} />
      </Sequence>

      <Sequence from={SHOT_STARTS[7]} durationInFrames={SHOT_DURATIONS[7]}>
        <TypewriterShot
          duration={SHOT_DURATIONS[7]}
          lines={[{text: 'IN 30 DAYS.', size: 260, color: '#fff'}]}
        />
      </Sequence>

      <Sequence from={SHOT_STARTS[8]} durationInFrames={SHOT_DURATIONS[8]}>
        <AbsoluteFill style={{backgroundColor: TEAL_BRIGHT}} />
      </Sequence>

      <Sequence from={SHOT_STARTS[9]} durationInFrames={SHOT_DURATIONS[9]}>
        <TypewriterShot
          duration={SHOT_DURATIONS[9]}
          lines={[
            {
              text: '1 in 4 Google listings',
              size: 64,
              color: 'rgba(255,255,255,0.85)',
              italic: true,
              letterSpacing: '0.01em',
              gapAfter: 28,
            },
            {text: 'ABANDONED.', size: 240, color: TEAL_BRIGHT, letterSpacing: '-0.01em'},
          ]}
        />
      </Sequence>

      <Sequence from={SHOT_STARTS[10]} durationInFrames={SHOT_DURATIONS[10]}>
        <TypewriterShot
          duration={SHOT_DURATIONS[10]}
          lines={[{text: 'THE REST?', size: 240, color: '#fff'}]}
        />
      </Sequence>

      <Sequence from={SHOT_STARTS[11]} durationInFrames={SHOT_DURATIONS[11]}>
        <TypewriterShot
          duration={SHOT_DURATIONS[11]}
          lines={[{text: 'UNTOUCHED.', size: 240, color: TEAL_BRIGHT, letterSpacing: '-0.01em'}]}
          postFlash
        />
      </Sequence>

      <Sequence from={SHOT_STARTS[12]} durationInFrames={SHOT_DURATIONS[12]}>
        <TypewriterShot
          duration={SHOT_DURATIONS[12]}
          lines={[
            {
              text: '$1,000/mo agency clients',
              size: 58,
              color: 'rgba(255,255,255,0.85)',
              italic: true,
              letterSpacing: '0.01em',
              gapAfter: 28,
            },
            {text: 'WAITING.', size: 260, color: TEAL_BRIGHT, letterSpacing: '-0.01em'},
          ]}
        />
      </Sequence>

      <Sequence from={SHOT_STARTS[13]} durationInFrames={SHOT_DURATIONS[13]}>
        <FinalCta duration={SHOT_DURATIONS[13]} />
      </Sequence>

      <Grain />
      <Vignette />
    </AbsoluteFill>
  );
};
