# Decision Report

- generated_at: 2026-08-18T08:26:31.241167+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11890**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=11890, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +0.62% | **+0.47%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.87% | **+0.35%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.40% | **+0.32%** |
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_BB3S | 2/20 | 10.0% | +1.82% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.10% | **+0.50%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.55% | **+0.30%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$612.37** / 初期 $100.00 (+512.37%)
- 確定: 4191件 (Win 1293 / Loss 1367 / Flat 1531) / skip 4260件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $612.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1819件 (Win 502 / Loss 427 / Flat 890) / skip 3482件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0055 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.64** / 初期 $100.00 (+16.64%)
- 確定: 1701件 (Win 505 / Loss 646 / Flat 550) / pending 6件 / skip 1656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000123 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.64

## 6. Latest Market Context

- 更新: 2026-08-18T08:26:20.202584+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64200.0
- Funnel: target 992 → liquid 182 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PRL/USDT:USDT | +21.98% | $2,942,255.69 |
| NIULAI/USDT:USDT | +16.04% | $9,135,578.75 |
| ACE/USDT:USDT | +15.41% | $36,956,548.06 |
| RED/USDT:USDT | +14.43% | $2,428,965.93 |
| SOXS/USDT:USDT | +12.41% | $7,445,758.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +1.73% | +1.68% |
| GPS/USDT:USDT | below_1h_threshold | +1.44% | +1.40% |
| OPN/USDT:USDT | below_1h_threshold | +1.07% | +1.02% |
| TUT/USDT:USDT | below_1h_threshold | +0.76% | +0.71% |
| PRL/USDT:USDT | below_1h_threshold | +0.62% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
