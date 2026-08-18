# Decision Report

- generated_at: 2026-08-18T02:41:35.548945+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11872**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.48% / filled 20/20。**
- 全期間 MARKET基準: n=11872, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +2.13% | **+1.60%** |
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.69% | **+1.35%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.12% | **+1.06%** |
| LIMIT_3PCT | 10/20 | 50.0% | +2.01% | **+1.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.55% | **+0.70%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.86% | **+0.56%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$611.63** / 初期 $100.00 (+511.63%)
- 確定: 4187件 (Win 1292 / Loss 1366 / Flat 1529) / skip 4246件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $611.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1819件 (Win 502 / Loss 427 / Flat 890) / skip 3464件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0729 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.67** / 初期 $100.00 (+17.67%)
- 確定: 1685件 (Win 505 / Loss 641 / Flat 539) / pending 6件 / skip 1656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000168 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $117.67

## 6. Latest Market Context

- 更新: 2026-08-18T02:41:21.558872+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=64176.0
- Funnel: target 992 → liquid 180 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIEVERSE/USDT:USDT | +16.65% | $1,802,544.48 |
| ONG/USDT:USDT | +10.16% | $1,055,322.33 |
| STAR/USDT:USDT | +8.65% | $1,789,647.27 |
| NIULAI/USDT:USDT | +8.38% | $8,289,575.66 |
| H/USDT:USDT | +6.89% | $6,430,952.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STAR/USDT:USDT | below_1h_threshold | +4.78% | +4.77% |
| SOXS/USDT:USDT | below_1h_threshold | +2.70% | +2.70% |
| APR/USDT:USDT | below_1h_threshold | +1.89% | +1.89% |
| BTW/USDT:USDT | below_1h_threshold | +1.88% | +1.87% |
| ACU/USDT:USDT | below_1h_threshold | +1.67% | +1.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
