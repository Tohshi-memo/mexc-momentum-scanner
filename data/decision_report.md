# Decision Report

- generated_at: 2026-11-02T09:36:31.276419+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18018**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.42% / filled 20/20。**
- 全期間 MARKET基準: n=18018, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.42% | **+2.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.42% | **+2.42%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.34% | **+2.22%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.14% | **+1.71%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.27% | **+0.76%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.52% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.88% | **+1.88%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.15% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,522.36** / 初期 $100.00 (+1422.36%)
- 確定: 6870件 (Win 1991 / Loss 2204 / Flat 2675) / skip 7709件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARIA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,522.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$377.87** / 初期 $100.00 (+277.87%)
- 確定: 4458件 (Win 1194 / Loss 991 / Flat 2273) / skip 6971件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0198 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARIA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $377.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6179件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000258 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T09:36:18.118093+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=78027.7
- Funnel: target 1088 → liquid 144 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARIA/USDT:USDT | +44.98% | $1,295,992.44 |
| IDOL/USDT:USDT | +33.23% | $16,288,769.08 |
| LYN/USDT:USDT | +28.53% | $2,870,517.87 |
| EVAA/USDT:USDT | +16.87% | $5,162,695.74 |
| SOPH/USDT:USDT | +13.50% | $1,003,906.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +0.88% | +1.11% |
| SOPH/USDT:USDT | below_1h_threshold | +0.63% | +0.86% |
| BEAMX/USDT:USDT | below_1h_threshold | +0.63% | +0.86% |
| NGAS/USDT:USDT | below_1h_threshold | +0.45% | +0.68% |
| SNXX/USDT:USDT | below_1h_threshold | +0.42% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
