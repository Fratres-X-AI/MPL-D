/**
 * LaserDazzlerHero — Fratres X AI defense prototype documentation hero.
 * Visual: emitter module + multi-point beam pattern → EO sensor target only.
 * No aircraft, UAV, or flying platforms depicted.
 */

import { motion } from "framer-motion";
import type { FC, MouseEventHandler } from "react";

const BEAM_COUNT = 9;
const BEAM_ANGLES_DEG = [-18, -14, -10, -5, 0, 5, 10, 14, 18];

export interface LaserDazzlerHeroProps {
  /** Primary CTA — e.g. scroll to #architecture or route change */
  onViewArchitecture?: MouseEventHandler<HTMLButtonElement>;
  /** Secondary CTA — e.g. open brief PDF or #technical-brief */
  onTechnicalBrief?: MouseEventHandler<HTMLButtonElement>;
  /** Optional anchor hrefs instead of handlers */
  architectureHref?: string;
  technicalBriefHref?: string;
}

const LaserDazzlerHero: FC<LaserDazzlerHeroProps> = ({
  onViewArchitecture,
  onTechnicalBrief,
  architectureHref = "#architecture",
  technicalBriefHref = "#technical-brief",
}) => {
  const emitterX = 72;
  const emitterY = 200;
  const apertureX = 118;
  const sensorCenterX = 340;
  const sensorCenterY = 200;
  const sensorW = 88;
  const sensorH = 56;
  const beamLength = 165;

  return (
    <section
      className="relative flex min-h-screen w-full flex-col bg-slate-950 text-slate-200 lg:flex-row"
      aria-labelledby="hero-heading"
    >
      {/* Engineering grid overlay */}
      <div
        className="pointer-events-none absolute inset-0 opacity-[0.04]"
        aria-hidden="true"
        style={{
          backgroundImage: `
            linear-gradient(to right, rgb(148 163 184) 1px, transparent 1px),
            linear-gradient(to bottom, rgb(148 163 184) 1px, transparent 1px)
          `,
          backgroundSize: "32px 32px",
        }}
      />
      <div
        className="pointer-events-none absolute inset-0 opacity-[0.03]"
        aria-hidden="true"
        style={{
          backgroundImage:
            "repeating-linear-gradient(0deg, transparent, transparent 3px, rgb(100 116 139) 3px, rgb(100 116 139) 4px)",
        }}
      />

      {/* Text column */}
      <div className="relative z-10 flex w-full flex-col justify-center px-6 py-16 sm:px-10 lg:w-[55%] lg:px-14 xl:px-20">
        <p className="mb-4 text-xs font-medium uppercase tracking-[0.2em] text-slate-500">
          Fratres X AI — Prototype
        </p>
        <h1
          id="hero-heading"
          className="text-[clamp(2.25rem,5vw,3.75rem)] font-semibold leading-[1.05] tracking-tight text-slate-100"
        >
          Multi-Point Laser Dazzler
        </h1>
        <p className="mt-5 text-[clamp(1.125rem,2.5vw,1.5rem)] font-medium text-slate-300">
          Non-kinetic sensor denial against electro-optical systems
        </p>
        <p className="mt-6 max-w-prose text-base leading-relaxed text-slate-400">
          Prototype using multi-emitter or diffractive beam delivery to degrade or
          overload EO/IR cameras on unmanned aerial platforms. Designed within
          small-to-medium UAV payload constraints.
        </p>

        <div className="mt-10 flex flex-wrap gap-4">
          {onViewArchitecture ? (
            <button
              type="button"
              onClick={onViewArchitecture}
              className="rounded-md bg-cyan-400 px-5 py-2.5 text-sm font-semibold text-slate-950 transition-colors hover:bg-cyan-300 focus:outline-none focus-visible:ring-2 focus-visible:ring-cyan-400 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-950"
              aria-label="View system architecture documentation"
            >
              View Architecture
            </button>
          ) : (
            <a
              href={architectureHref}
              className="inline-flex rounded-md bg-cyan-400 px-5 py-2.5 text-sm font-semibold text-slate-950 transition-colors hover:bg-cyan-300 focus:outline-none focus-visible:ring-2 focus-visible:ring-cyan-400 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-950"
              aria-label="View system architecture documentation"
            >
              View Architecture
            </a>
          )}
          {onTechnicalBrief ? (
            <button
              type="button"
              onClick={onTechnicalBrief}
              className="rounded-md border border-slate-600 px-5 py-2.5 text-sm font-semibold text-slate-200 transition-colors hover:border-slate-500 hover:bg-slate-900 focus:outline-none focus-visible:ring-2 focus-visible:ring-cyan-400 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-950"
              aria-label="Open technical brief"
            >
              Technical Brief
            </button>
          ) : (
            <a
              href={technicalBriefHref}
              className="inline-flex rounded-md border border-slate-600 px-5 py-2.5 text-sm font-semibold text-slate-200 transition-colors hover:border-slate-500 hover:bg-slate-900 focus:outline-none focus-visible:ring-2 focus-visible:ring-cyan-400 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-950"
              aria-label="Open technical brief"
            >
              Technical Brief
            </a>
          )}
        </div>

        <p className="mt-auto pt-16 text-xs text-slate-600 lg:pt-24">
          Fratres X AI | Defense Projects — Prototype Documentation
        </p>
      </div>

      {/* Visual column — schematic only; no aircraft */}
      <div
        className="relative z-10 flex w-full items-center justify-center px-4 py-10 lg:w-[45%] lg:py-16"
        aria-label="Schematic diagram: laser dazzler emitter module projecting multi-point beam pattern onto electro-optical sensor target"
        role="img"
      >
        <svg
          viewBox="0 0 420 400"
          className="h-auto w-full max-w-lg"
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
        >
          <defs>
            <linearGradient id="apertureGlow" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stopColor="#22d3ee" stopOpacity="0.15" />
              <stop offset="100%" stopColor="#22d3ee" stopOpacity="0.55" />
            </linearGradient>
            <clipPath id="sensorClip">
              <rect
                x={sensorCenterX - sensorW / 2}
                y={sensorCenterY - sensorH / 2}
                width={sensorW}
                height={sensorH}
                rx="4"
              />
            </clipPath>
          </defs>

          {/* Sensor target — focal plane array */}
          <g aria-hidden="true">
            <rect
              x={sensorCenterX - sensorW / 2 - 6}
              y={sensorCenterY - sensorH / 2 - 6}
              width={sensorW + 12}
              height={sensorH + 12}
              rx="6"
              fill="none"
              stroke="#475569"
              strokeWidth="1"
            />
            <rect
              x={sensorCenterX - sensorW / 2}
              y={sensorCenterY - sensorH / 2}
              width={sensorW}
              height={sensorH}
              rx="4"
              fill="#0f172a"
              stroke="#64748b"
              strokeWidth="1.5"
            />
            {/* Pixel grid */}
            {Array.from({ length: 6 }).map((_, row) =>
              Array.from({ length: 9 }).map((__, col) => (
                <rect
                  key={`px-${row}-${col}`}
                  x={sensorCenterX - sensorW / 2 + 6 + col * 9}
                  y={sensorCenterY - sensorH / 2 + 6 + row * 7}
                  width="7"
                  height="5"
                  fill="#1e293b"
                  stroke="#334155"
                  strokeWidth="0.5"
                />
              )),
            )}
            <text
              x={sensorCenterX}
              y={sensorCenterY + sensorH / 2 + 22}
              textAnchor="middle"
              fill="#64748b"
              fontSize="10"
              fontFamily="ui-sans-serif, system-ui, sans-serif"
            >
              EO sensor (schematic)
            </text>
          </g>

          {/* Multi-point beams */}
          {BEAM_ANGLES_DEG.map((angleDeg, index) => {
            const rad = (angleDeg * Math.PI) / 180;
            const endX = apertureX + Math.cos(rad) * beamLength;
            const endY = emitterY + Math.sin(rad) * beamLength;
            const hitX = sensorCenterX - sensorW / 2 + 12 + (index / (BEAM_COUNT - 1)) * (sensorW - 24);
            const hitY = sensorCenterY - 8 + (index % 3) * 8;

            return (
              <g key={`beam-${index}`}>
                <motion.line
                  x1={apertureX}
                  y1={emitterY}
                  x2={endX}
                  y2={endY}
                  stroke="#22d3ee"
                  strokeWidth="1.25"
                  strokeLinecap="round"
                  initial={{ opacity: 0.25, pathLength: 0 }}
                  animate={{
                    opacity: [0.25, 0.95, 0.35],
                    pathLength: [0.4, 1, 0.85],
                  }}
                  transition={{
                    duration: 2.4,
                    repeat: Infinity,
                    delay: index * 0.18,
                    ease: "easeInOut",
                  }}
                />
                <motion.line
                  x1={endX}
                  y1={endY}
                  x2={hitX}
                  y2={hitY}
                  stroke="#22d3ee"
                  strokeWidth="1"
                  strokeLinecap="round"
                  strokeDasharray="3 2"
                  initial={{ opacity: 0.2 }}
                  animate={{ opacity: [0.2, 0.75, 0.25] }}
                  transition={{
                    duration: 2.4,
                    repeat: Infinity,
                    delay: index * 0.18 + 0.1,
                    ease: "easeInOut",
                  }}
                />
                <motion.circle
                  cx={hitX}
                  cy={hitY}
                  r="4"
                  fill="#22d3ee"
                  initial={{ opacity: 0.15, scale: 0.6 }}
                  animate={{
                    opacity: [0.15, 0.9, 0.2],
                    scale: [0.6, 1.15, 0.7],
                  }}
                  transition={{
                    duration: 2.4,
                    repeat: Infinity,
                    delay: index * 0.18 + 0.2,
                    ease: "easeInOut",
                  }}
                />
              </g>
            );
          })}

          {/* Emitter housing */}
          <g aria-hidden="true">
            <rect
              x={emitterX - 48}
              y={emitterY - 36}
              width="96"
              height="72"
              rx="4"
              fill="#1e293b"
              stroke="#475569"
              strokeWidth="1.5"
            />
            <rect
              x={emitterX - 40}
              y={emitterY - 28}
              width="80"
              height="20"
              rx="2"
              fill="#0f172a"
              stroke="#334155"
              strokeWidth="1"
            />
            <text
              x={emitterX}
              y={emitterY - 14}
              textAnchor="middle"
              fill="#64748b"
              fontSize="8"
              fontFamily="ui-monospace, monospace"
            >
              DRIVER
            </text>
            <rect
              x={emitterX - 28}
              y={emitterY - 2}
              width="56"
              height="28"
              rx="2"
              fill="#0f172a"
              stroke="#334155"
              strokeWidth="1"
            />
            <text
              x={emitterX}
              y={emitterY + 14}
              textAnchor="middle"
              fill="#64748b"
              fontSize="8"
              fontFamily="ui-monospace, monospace"
            >
              OPTICS
            </text>
            {/* Aperture */}
            <rect
              x={apertureX - 3}
              y={emitterY - 10}
              width="6"
              height="20"
              rx="1"
              fill="url(#apertureGlow)"
              stroke="#22d3ee"
              strokeWidth="1"
            />
            <text
              x={emitterX}
              y={emitterY + 44}
              textAnchor="middle"
              fill="#64748b"
              fontSize="10"
              fontFamily="ui-sans-serif, system-ui, sans-serif"
            >
              Emitter module
            </text>
          </g>

          {/* Overload indication on sensor (clip) */}
          <g clipPath="url(#sensorClip)" aria-hidden="true">
            <motion.rect
              x={sensorCenterX - sensorW / 2}
              y={sensorCenterY - sensorH / 2}
              width={sensorW}
              height={sensorH}
              fill="#22d3ee"
              initial={{ opacity: 0 }}
              animate={{ opacity: [0, 0.12, 0.04, 0.18, 0.06] }}
              transition={{ duration: 3.6, repeat: Infinity, ease: "easeInOut" }}
            />
          </g>
        </svg>
      </div>

      {/* Mobile footer duplicate for stacked layout */}
      <div className="border-t border-slate-800 px-6 py-4 text-center text-xs text-slate-600 lg:hidden">
        Fratres X AI | Defense Projects — Prototype Documentation
      </div>
    </section>
  );
};

export default LaserDazzlerHero;
