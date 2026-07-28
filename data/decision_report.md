# Decision Report

- generated_at: 2026-07-28T17:06:30.100560+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9713**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9713, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.53% | **-0.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.62% | **+0.57%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.50% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.20% | **+1.43%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.99% | **+1.20%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.39% | **+1.18%** |
| MARKET_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +1.50% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定トレード: 150件 (TP 52 / SL 93 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.44
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$493.07** / 初期 $100.00 (+393.07%)
- 確定: 3483件 (Win 1101 / Loss 1128 / Flat 1254) / skip 2791件
- 成長率目線: 平均log +0.000458 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $493.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1898件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1146 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.58** / 初期 $100.00 (+9.58%)
- 確定: 731件 (Win 237 / Loss 278 / Flat 216) / pending 6件 / skip 450件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000457 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $109.58

## 6. Latest Market Context

- 更新: 2026-07-28T17:06:23.062124+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=63955.3
- Funnel: target 904 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +18.34% | $5,941,831.66 |
| JIMOTHY/USDT:USDT | +8.88% | $1,245,291.86 |
| BULLA/USDT:USDT | +8.04% | $2,468,932.93 |
| AEON1/USDT:USDT | +4.31% | $2,210,708.78 |
| ZIL/USDT:USDT | +3.97% | $1,524,603.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QNTSTOCK/USDT:USDT | below_1h_threshold | +1.43% | +1.53% |
| REZ/USDT:USDT | below_1h_threshold | +1.39% | +1.49% |
| AEON1/USDT:USDT | below_1h_threshold | +1.29% | +1.39% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.38% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.21% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
