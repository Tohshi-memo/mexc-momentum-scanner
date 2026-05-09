# Decision Report

- generated_at: 2026-05-09T14:12:35.890802+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3887**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.67% / filled 20/20。**
- 全期間 MARKET基準: n=3887, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/13 | 30.8% | +3.34% | **+1.03%** |
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |
| ASK | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.15% | **+0.58%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +0.46% | **+0.33%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.42% | **+0.23%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.45% | **+0.20%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.30% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.27** / 初期 $100.00 (+8.27%)
- 確定: 195件 (Win 48 / Loss 65 / Flat 82) / skip 253件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +3.61%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $108.27

## 4. Latest Market Context

- 更新: 2026-05-09T14:12:33.053612+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80370.9
- Funnel: target 769 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +33.47% | $3,348,386.15 |
| DYM/USDT:USDT | +32.73% | $6,280,178.91 |
| SAHARA/USDT:USDT | +27.33% | $3,832,931.97 |
| SATO/USDT:USDT | +23.85% | $3,256,315.69 |
| PLAY/USDT:USDT | +23.08% | $25,095,500.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +3.12% | +3.11% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.21% | +2.20% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.80% | +1.79% |
| AERO/USDT:USDT | below_1h_threshold | +1.49% | +1.48% |
| ON/USDT:USDT | below_1h_threshold | +1.15% | +1.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
