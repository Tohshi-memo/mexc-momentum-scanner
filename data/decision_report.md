# Decision Report

- generated_at: 2026-06-17T17:49:30.063891+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6959**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6959, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.52% | **-0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/18 | 33.3% | +2.12% | **+0.71%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.77% | **+5.77%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.11% | **+1.58%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.17% | **+0.94%** |
| MARKET_LONG | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.91% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.54** / 初期 $100.00 (+97.54%)
- 確定: 1815件 (Win 495 / Loss 573 / Flat 747) / skip 1705件
- 成長率目線: 平均log +0.000375 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XPL/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.77% 残高後 $197.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$103.43** / 初期 $100.00 (+3.43%)
- 確定: 232件 (Win 61 / Loss 55 / Flat 116) / skip 138件
- 成長率目線: 平均log +0.000145 / 幾何平均 +0.015% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0955 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $103.43

## 5. Latest Market Context

- 更新: 2026-06-17T17:49:21.509230+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=65804.2
- Funnel: target 790 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RE/USDT:USDT | +13.65% | $1,330,096.88 |
| ESPORTS/USDT:USDT | +9.44% | $14,001,047.01 |
| TAC/USDT:USDT | +6.33% | $2,017,817.25 |
| ETHFI/USDT:USDT | +3.66% | $2,255,360.79 |
| BP/USDT:USDT | +3.52% | $1,145,577.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BP/USDT:USDT | below_1h_threshold | +4.75% | +4.79% |
| ETHFI/USDT:USDT | below_1h_threshold | +3.87% | +3.91% |
| LIT/USDT:USDT | below_1h_threshold | +2.93% | +2.97% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +2.20% | +2.24% |
| GUA/USDT:USDT | below_1h_threshold | +1.73% | +1.77% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
