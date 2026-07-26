# Decision Report

- generated_at: 2026-07-26T11:16:20.372855+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9570**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=9570, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.24% | **+1.17%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.33% | **+0.67%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.85% | **+0.64%** |
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.86% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.94% | **+5.94%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.48% | **+0.38%** |
| MARKET_LONG | 20/20 | 100.0% | +0.36% | **+0.36%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.87% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$454.84** / 初期 $100.00 (+354.84%)
- 確定: 3398件 (Win 1078 / Loss 1105 / Flat 1215) / skip 2733件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DIA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $454.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.72** / 初期 $100.00 (+37.72%)
- 確定: 1222件 (Win 338 / Loss 274 / Flat 610) / skip 1759件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0564 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.47** / 初期 $100.00 (+8.47%)
- 確定: 613件 (Win 206 / Loss 236 / Flat 171) / pending 3件 / skip 425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000309 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $108.47

## 6. Latest Market Context

- 更新: 2026-07-26T11:16:12.036963+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64481.9
- Funnel: target 898 → liquid 118 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +67.21% | $37,759,904.24 |
| DIA/USDT:USDT | +42.49% | $3,566,356.39 |
| PIEVERSE/USDT:USDT | +34.32% | $5,298,702.26 |
| BANK/USDT:USDT | +26.01% | $91,058,135.22 |
| KAITO/USDT:USDT | +22.10% | $4,468,721.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EUL/USDT:USDT | below_1h_threshold | +2.40% | +2.42% |
| UNI/USDT:USDT | below_1h_threshold | +1.83% | +1.84% |
| BEAT/USDT:USDT | below_1h_threshold | +1.21% | +1.22% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.17% | +1.18% |
| VELVET/USDT:USDT | below_1h_threshold | +0.99% | +1.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
