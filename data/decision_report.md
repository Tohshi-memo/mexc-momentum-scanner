# Decision Report

- generated_at: 2026-07-23T01:21:22.498837+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9336**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9336, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.46% | **-0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_8PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.20% | **+0.78%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.13% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +3.71% | **+2.60%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.44% | **+1.71%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.91% | **+1.31%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.03% | **+0.88%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.24% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$428.20** / 初期 $100.00 (+328.20%)
- 確定: 3319件 (Win 1048 / Loss 1074 / Flat 1197) / skip 2578件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B2/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $428.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1161件 (Win 312 / Loss 254 / Flat 595) / skip 1586件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1000 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.27** / 初期 $100.00 (+1.27%)
- 確定: 428件 (Win 143 / Loss 178 / Flat 107) / pending 0件 / skip 378件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000355 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CBRSSTOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.27

## 6. Latest Market Context

- 更新: 2026-07-23T01:21:15.582477+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=65881.2
- Funnel: target 890 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +58.94% | $5,886,658.40 |
| BANK/USDT:USDT | +37.03% | $108,798,907.80 |
| RIF/USDT:USDT | +17.17% | $4,663,885.67 |
| ZAMA/USDT:USDT | +16.96% | $3,411,366.79 |
| ON/USDT:USDT | +15.72% | $2,391,829.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +3.85% | +4.06% |
| EVAA/USDT:USDT | below_1h_threshold | +3.04% | +3.26% |
| TRIA/USDT:USDT | below_1h_threshold | +2.57% | +2.78% |
| SOXL/USDT:USDT | below_1h_threshold | +2.35% | +2.57% |
| ZAMA/USDT:USDT | below_1h_threshold | +2.35% | +2.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
