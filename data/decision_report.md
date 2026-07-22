# Decision Report

- generated_at: 2026-07-22T08:21:23.484074+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9262**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9262, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.83% | **-0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.81% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.93% | **+1.61%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.56% | **+1.41%** |
| MARKET_LONG | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.42% | **+0.35%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +0.61% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$428.35** / 初期 $100.00 (+328.35%)
- 確定: 3260件 (Win 1027 / Loss 1043 / Flat 1190) / skip 2563件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ERA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $428.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1513件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1776 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.63** / 初期 $100.00 (+2.63%)
- 確定: 403件 (Win 139 / Loss 165 / Flat 99) / pending 6件 / skip 327件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000430 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ERA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $102.63

## 6. Latest Market Context

- 更新: 2026-07-22T08:21:15.308359+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=66056.5
- Funnel: target 888 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +36.87% | $3,449,964.44 |
| ERA/USDT:USDT | +30.05% | $11,952,806.96 |
| RE/USDT:USDT | +20.03% | $4,223,724.85 |
| LAB/USDT:USDT | +16.33% | $13,464,433.93 |
| SMCISTOCK/USDT:USDT | +15.97% | $4,264,029.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +4.91% | +4.54% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.35% | +1.98% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.24% | +1.87% |
| USOIL/USDT:USDT | below_1h_threshold | +1.86% | +1.49% |
| US/USDT:USDT | below_1h_threshold | +1.65% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
