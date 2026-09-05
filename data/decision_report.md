# Decision Report

- generated_at: 2026-09-05T01:31:23.826565+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13680**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=13680, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.07% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.41% | **+1.36%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.57% | **+1.34%** |
| MARKET_LONG | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.40% | **+1.05%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 202件 (TP 75 / SL 122 / EXP 5)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$855.36** / 初期 $100.00 (+755.36%)
- 確定: 5012件 (Win 1516 / Loss 1645 / Flat 1851) / skip 5229件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $855.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$186.80** / 初期 $100.00 (+86.80%)
- 確定: 2428件 (Win 684 / Loss 578 / Flat 1166) / skip 4663件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0876 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $186.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.54** / 初期 $100.00 (+18.54%)
- 確定: 2314件 (Win 690 / Loss 887 / Flat 737) / pending 3件 / skip 2834件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000294 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` TP_HIT account +0.34% 残高後 $118.54

## 6. Latest Market Context

- 更新: 2026-09-05T01:31:12.444229+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=79631.0
- Funnel: target 1050 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +51.46% | $12,028,690.83 |
| DASH/USDT:USDT | +24.56% | $30,971,515.73 |
| AKE/USDT:USDT | +24.12% | $5,621,554.60 |
| BASECAT/USDT:USDT | +20.03% | $1,999,508.18 |
| USELESS/USDT:USDT | +19.63% | $45,272,149.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_1h_threshold | +3.63% | +3.52% |
| CHIP/USDT:USDT | below_1h_threshold | +2.66% | +2.54% |
| 1000BONK/USDT:USDT | below_1h_threshold | +2.18% | +2.07% |
| USELESS/USDT:USDT | below_1h_threshold | +1.97% | +1.86% |
| ZEN/USDT:USDT | below_1h_threshold | +1.58% | +1.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
