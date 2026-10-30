# Decision Report

- generated_at: 2026-10-30T15:41:26.658662+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17852**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=17852, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +2.97% | **+1.04%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.69% | **+0.66%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.86% | **+0.56%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.19% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.19% | **+0.83%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.03% | **+0.72%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.39% | **+0.69%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,523.56** / 初期 $100.00 (+1423.56%)
- 確定: 6806件 (Win 1975 / Loss 2181 / Flat 2650) / skip 7607件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,523.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$362.04** / 初期 $100.00 (+262.04%)
- 確定: 4357件 (Win 1171 / Loss 982 / Flat 2204) / skip 6906件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0851 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAMX/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.08% 残高後 $362.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6013件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000184 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-30T15:41:11.549692+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.43% price=77550.0
- Funnel: target 1090 → liquid 192 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAMX/USDT:USDT | +43.01% | $1,851,050.89 |
| PARTI/USDT:USDT | +39.19% | $10,106,059.98 |
| MAGMA/USDT:USDT | +30.86% | $1,689,677.42 |
| SOXS/USDT:USDT | +28.16% | $62,390,841.95 |
| Q/USDT:USDT | +26.29% | $25,850,132.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IDOL/USDT:USDT | below_1h_threshold | +4.60% | +4.17% |
| FLOKI/USDT:USDT | below_1h_threshold | +3.29% | +2.85% |
| XLM/USDT:USDT | below_1h_threshold | +2.61% | +2.18% |
| SOXS/USDT:USDT | below_1h_threshold | +2.53% | +2.10% |
| Q/USDT:USDT | below_1h_threshold | +2.50% | +2.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
