# Decision Report

- generated_at: 2026-11-05T08:31:32.792826+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18171**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.03% / filled 20/20。**
- 全期間 MARKET基準: n=18171, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+3.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.03% | **+3.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.03% | **+3.03%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.68% | **+0.67%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +3.04% | **+0.91%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.60% | **+0.91%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.20% | **+0.60%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -0.44% | **-0.13%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | -1.05% | **-0.84%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,499.45** / 初期 $100.00 (+1399.45%)
- 確定: 6990件 (Win 2019 / Loss 2243 / Flat 2728) / skip 7742件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,499.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$372.01** / 初期 $100.00 (+272.01%)
- 確定: 4563件 (Win 1223 / Loss 1030 / Flat 2310) / skip 7019件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0066 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $372.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6330件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000269 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-05T08:31:17.569071+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=80536.5
- Funnel: target 1077 → liquid 180 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ELSA/USDT:USDT | +32.75% | $4,510,577.67 |
| UAI/USDT:USDT | +24.71% | $6,695,771.14 |
| APPSTOCK/USDT:USDT | +20.72% | $1,568,099.13 |
| FLUID/USDT:USDT | +15.20% | $5,741,614.96 |
| JCT/USDT:USDT | +15.17% | $11,185,751.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ELSA/USDT:USDT | below_1h_threshold | +4.98% | +4.77% |
| AR/USDT:USDT | below_1h_threshold | +2.42% | +2.20% |
| ICNT/USDT:USDT | below_1h_threshold | +2.21% | +2.00% |
| LYN/USDT:USDT | below_1h_threshold | +2.15% | +1.93% |
| AERO/USDT:USDT | below_1h_threshold | +1.70% | +1.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
