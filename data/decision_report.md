# Decision Report

- generated_at: 2026-07-22T03:26:28.363567+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9244**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9244, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +7.23% | **+1.08%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.23% | **+0.18%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.28% | **+0.10%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.13% | **+0.03%** |
| LIMIT_8PCT | 4/20 | 20.0% | -0.09% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +3.26% | **+3.10%** |
| MARKET_LONG | 20/20 | 100.0% | +2.77% | **+2.77%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.21% | **+2.41%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +0.99% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3250件 (Win 1021 / Loss 1039 / Flat 1190) / skip 2555件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1496件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1552 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.87** / 初期 $100.00 (+1.87%)
- 確定: 388件 (Win 132 / Loss 159 / Flat 97) / pending 5件 / skip 325件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000336 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.87

## 6. Latest Market Context

- 更新: 2026-07-22T03:26:19.952043+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=66239.9
- Funnel: target 885 → liquid 174 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.0 >= 65=1, 4h RSI 78.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +44.32% | $4,173,497.58 |
| LAB/USDT:USDT | +22.14% | $6,571,319.00 |
| PONS/USDT:USDT | +19.90% | $2,157,958.90 |
| SMCISTOCK/USDT:USDT | +19.46% | $3,789,940.59 |
| FWDISTOCK/USDT:USDT | +16.62% | $4,190,513.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FWDISTOCK/USDT:USDT | below_1h_threshold | +2.76% | +2.83% |
| RE/USDT:USDT | below_1h_threshold | +2.17% | +2.23% |
| MYX/USDT:USDT | below_1h_threshold | +2.10% | +2.17% |
| B/USDT:USDT | below_1h_threshold | +2.05% | +2.12% |
| TLM/USDT:USDT | below_1h_threshold | +1.54% | +1.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
