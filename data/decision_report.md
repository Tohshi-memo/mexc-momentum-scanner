# Decision Report

- generated_at: 2026-06-18T06:32:58.390581+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7014**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=7014, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |
| LIMIT_6PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.00% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.23% | **+0.17%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$211.90** / 初期 $100.00 (+111.90%)
- 確定: 1860件 (Win 519 / Loss 590 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $211.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.80** / 初期 $100.00 (+5.80%)
- 確定: 287件 (Win 81 / Loss 76 / Flat 130) / skip 138件
- 成長率目線: 平均log +0.000197 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0562 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $105.80

## 5. Latest Market Context

- 更新: 2026-06-18T06:32:53.921305+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=64041.7
- Funnel: target 793 → liquid 175 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +100.15% | $37,994,465.77 |
| SYN/USDT:USDT | +63.39% | $5,050,598.53 |
| O/USDT:USDT | +59.57% | $2,600,962.67 |
| H/USDT:USDT | +38.07% | $32,117,018.91 |
| HOME/USDT:USDT | +26.67% | $1,986,158.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UP/USDT:USDT | below_1h_threshold | +3.75% | +3.63% |
| ALLO/USDT:USDT | below_1h_threshold | +3.32% | +3.20% |
| MEGA/USDT:USDT | below_1h_threshold | +3.31% | +3.19% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.08% | +2.96% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.63% | +2.51% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
