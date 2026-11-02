# Decision Report

- generated_at: 2026-11-02T04:56:50.957594+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18007**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.55% / filled 20/20。**
- 全期間 MARKET基準: n=18007, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.83% | **+1.65%** |
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.30% | **+1.04%** |
| LIMIT_ATR | 9/20 | 45.0% | +2.28% | **+1.02%** |
| LIMIT_6PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.10% | **-0.05%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.15% | **-0.14%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,522.82** / 初期 $100.00 (+1422.82%)
- 確定: 6859件 (Win 1989 / Loss 2203 / Flat 2667) / skip 7709件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAMX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,522.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$380.01** / 初期 $100.00 (+280.01%)
- 確定: 4447件 (Win 1192 / Loss 987 / Flat 2268) / skip 6971件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0901 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAMX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $380.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6171件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000256 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T04:56:30.310127+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=78430.0
- Funnel: target 1088 → liquid 140 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LYN/USDT:USDT | +30.76% | $1,746,892.72 |
| IDOL/USDT:USDT | +20.32% | $14,430,175.65 |
| RT/USDT:USDT | +15.94% | $1,603,878.55 |
| BEAMX/USDT:USDT | +14.81% | $4,683,704.70 |
| KORU/USDT:USDT | +11.56% | $26,058,074.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RT/USDT:USDT | below_1h_threshold | +3.71% | +3.92% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +3.19% | +3.39% |
| KORU/USDT:USDT | below_1h_threshold | +2.52% | +2.73% |
| DELTAELECSTOCK/USDT:USDT | below_1h_threshold | +2.35% | +2.56% |
| SNXX/USDT:USDT | below_1h_threshold | +2.10% | +2.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
