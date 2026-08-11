# Decision Report

- generated_at: 2026-08-11T21:46:35.429428+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11300**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.71% / filled 20/20。**
- 全期間 MARKET基準: n=11300, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.03% | **+0.93%** |
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.86% | **+0.68%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.62% | **+0.43%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.92% | **+1.05%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.89% | **+0.80%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.60% | **+0.64%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.92% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 179件 (TP 69 / SL 105 / EXP 5)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3939件 (Win 1230 / Loss 1285 / Flat 1424) / skip 3922件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.74** / 初期 $100.00 (+43.74%)
- 確定: 1554件 (Win 435 / Loss 363 / Flat 756) / skip 3157件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0313 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SMCISTOCK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $143.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.64** / 初期 $100.00 (+14.64%)
- 確定: 1331件 (Win 407 / Loss 525 / Flat 399) / pending 0件 / skip 1447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000216 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.64

## 6. Latest Market Context

- 更新: 2026-08-11T21:46:25.808751+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=63644.0
- Funnel: target 967 → liquid 193 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.2 >= 65=1, 4h RSI 78.6 >= 65=1, 4h RSI 68.4 >= 65=1, 4h RSI 65.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +33.77% | $1,416,737.94 |
| HOLO/USDT:USDT | +17.06% | $2,074,164.58 |
| CRWVSTOCK/USDT:USDT | +16.13% | $3,237,185.65 |
| BMT/USDT:USDT | +11.23% | $2,539,222.83 |
| BEAT/USDT:USDT | +10.35% | $112,764,280.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.61% | +3.73% |
| BTR/USDT:USDT | below_1h_threshold | +3.34% | +3.46% |
| FHE/USDT:USDT | below_1h_threshold | +2.00% | +2.12% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.99% | +2.11% |
| BMT/USDT:USDT | below_1h_threshold | +1.80% | +1.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
