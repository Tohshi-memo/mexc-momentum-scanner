# Decision Report

- generated_at: 2026-10-29T22:41:31.696821+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17816**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.63% / filled 20/20。**
- 全期間 MARKET基準: n=17816, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.63% | **+1.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/14 | 21.4% | +8.00% | **+1.71%** |
| MARKET | 20/20 | 100.0% | +1.63% | **+1.63%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.46% | **+1.17%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.50% | **+0.90%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.27% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.33% | **+0.29%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +0.54% | **+0.27%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.10% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.22** / 初期 $100.00 (+1431.22%)
- 確定: 6804件 (Win 1975 / Loss 2180 / Flat 2649) / skip 7573件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,531.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$363.52** / 初期 $100.00 (+263.52%)
- 確定: 4336件 (Win 1167 / Loss 980 / Flat 2189) / skip 6891件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0030 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRX/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $363.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5977件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000268 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T22:41:16.876063+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=79071.1
- Funnel: target 1086 → liquid 183 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PARTI/USDT:USDT | +70.65% | $5,636,783.32 |
| Q/USDT:USDT | +27.36% | $24,413,376.04 |
| SOXS/USDT:USDT | +16.54% | $71,906,164.65 |
| BLESS/USDT:USDT | +8.69% | $14,406,716.32 |
| BULLA/USDT:USDT | +5.20% | $1,650,228.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +2.18% | +2.09% |
| SOXS/USDT:USDT | below_1h_threshold | +1.88% | +1.79% |
| AGT/USDT:USDT | below_1h_threshold | +1.52% | +1.43% |
| PARTI/USDT:USDT | below_1h_threshold | +1.23% | +1.14% |
| JASMY/USDT:USDT | below_1h_threshold | +1.22% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
