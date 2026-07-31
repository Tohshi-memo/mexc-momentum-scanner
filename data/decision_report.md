# Decision Report

- generated_at: 2026-07-31T04:16:27.053220+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9957**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9957, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.36% | **-1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.65% | **+0.66%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.54% | **+0.19%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +4.13% | **+2.07%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.36% | **+2.01%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.56% | **+1.66%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.07% | **+1.53%** |
| MARKET_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$548.89** / 初期 $100.00 (+448.89%)
- 確定: 3548件 (Win 1131 / Loss 1154 / Flat 1263) / skip 2970件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $548.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.17** / 初期 $100.00 (+41.17%)
- 確定: 1254件 (Win 351 / Loss 285 / Flat 618) / skip 2114件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2127 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $141.17

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.57** / 初期 $100.00 (+10.57%)
- 確定: 805件 (Win 262 / Loss 320 / Flat 223) / pending 0件 / skip 629件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000672 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARMSTOCK/USDT:USDT `MARKET` EXPIRED account -0.04% 残高後 $110.57

## 6. Latest Market Context

- 更新: 2026-07-31T04:16:18.326854+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64335.5
- Funnel: target 920 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +40.55% | $7,859,311.09 |
| MMT/USDT:USDT | +35.36% | $10,275,026.30 |
| AXTISTOCK/USDT:USDT | +30.73% | $3,967,475.68 |
| RLC/USDT:USDT | +18.77% | $1,110,481.63 |
| AMZU/USDT:USDT | +16.93% | $1,826,092.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +3.48% | +3.49% |
| MMT/USDT:USDT | below_1h_threshold | +2.90% | +2.92% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.08% | +2.09% |
| UB/USDT:USDT | below_1h_threshold | +1.71% | +1.72% |
| UNI/USDT:USDT | below_1h_threshold | +1.55% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
