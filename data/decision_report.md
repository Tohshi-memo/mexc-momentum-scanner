# Decision Report

- generated_at: 2026-05-11T02:27:42.972471+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4003**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.00% / filled 20/20。**
- 全期間 MARKET基準: n=4003, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +2.96% | **+1.37%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.31% | **+1.18%** |
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |
| ASK | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.35% | **+0.84%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.35% | **+1.64%** |
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.37% | **+1.17%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.27% | **+1.08%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.35% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$109.66** / 初期 $100.00 (+9.66%)
- 確定: 209件 (Win 53 / Loss 71 / Flat 85) / skip 355件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPG/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.67% 残高後 $109.66

## 4. Latest Market Context

- 更新: 2026-05-11T02:27:39.994676+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=81152.5
- Funnel: target 775 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +30.92% | $9,687,203.54 |
| ALCH/USDT:USDT | +20.33% | $3,894,041.41 |
| TROLLSOL/USDT:USDT | +20.13% | $5,390,664.50 |
| B/USDT:USDT | +12.33% | $2,730,222.02 |
| OPG/USDT:USDT | +10.63% | $1,199,435.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +1.84% | +2.22% |
| BEAT/USDT:USDT | below_1h_threshold | +1.60% | +1.98% |
| BAS/USDT:USDT | below_1h_threshold | +1.37% | +1.75% |
| PLAY/USDT:USDT | below_1h_threshold | +1.26% | +1.64% |
| ORCA/USDT:USDT | below_1h_threshold | +1.07% | +1.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
