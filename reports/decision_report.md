# Decision Report

- generated_at: 2026-07-25T13:50:41.879474+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9515**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=9515, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/19 | 31.6% | +3.40% | **+1.07%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.60% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.69% | **+1.44%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.50% | **+1.12%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.69% | **+0.62%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.72% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$435.20** / 初期 $100.00 (+335.20%)
- 確定: 3343件 (Win 1056 / Loss 1083 / Flat 1204) / skip 2733件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $435.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$132.95** / 初期 $100.00 (+32.95%)
- 確定: 1169件 (Win 316 / Loss 254 / Flat 599) / skip 1757件
- 成長率目線: 平均log +0.000244 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1422 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $132.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$106.87** / 初期 $100.00 (+6.87%)
- 確定: 562件 (Win 190 / Loss 216 / Flat 156) / pending 4件 / skip 420件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000492 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $106.87

## 6. Latest Market Context

- 更新: 2026-07-25T13:36:15.088025+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64099.1
- Funnel: target 898 → liquid 148 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +58.67% | $10,216,920.15 |
| DEXE/USDT:USDT | +49.69% | $119,186,526.91 |
| AKE/USDT:USDT | +28.67% | $46,748,675.66 |
| ESPORTS/USDT:USDT | +21.46% | $15,928,201.54 |
| PROM/USDT:USDT | +20.31% | $4,836,060.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +2.36% | +2.35% |
| MORPHO/USDT:USDT | below_1h_threshold | +1.96% | +1.94% |
| B2/USDT:USDT | below_1h_threshold | +1.67% | +1.65% |
| VVV/USDT:USDT | below_1h_threshold | +1.43% | +1.42% |
| SAGA/USDT:USDT | below_1h_threshold | +1.05% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
