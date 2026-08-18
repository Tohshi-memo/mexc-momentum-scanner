# Decision Report

- generated_at: 2026-08-18T03:21:39.786838+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11879**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.95% / filled 20/20。**
- 全期間 MARKET基準: n=11879, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 12/20 | 60.0% | +2.26% | **+1.36%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +3.70% | **+1.29%** |
| LIMIT_ATR | 7/20 | 35.0% | +3.25% | **+1.14%** |
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.00% | **+0.70%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.10% | **+0.50%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.62% | **+0.41%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.58% | **+0.39%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$611.63** / 初期 $100.00 (+511.63%)
- 確定: 4187件 (Win 1292 / Loss 1366 / Flat 1529) / skip 4253件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $611.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1819件 (Win 502 / Loss 427 / Flat 890) / skip 3471件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0431 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.67** / 初期 $100.00 (+17.67%)
- 確定: 1690件 (Win 505 / Loss 641 / Flat 544) / pending 4件 / skip 1656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000116 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $117.67

## 6. Latest Market Context

- 更新: 2026-08-18T03:21:29.451610+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64100.1
- Funnel: target 992 → liquid 181 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIEVERSE/USDT:USDT | +15.77% | $1,950,601.73 |
| NIULAI/USDT:USDT | +13.42% | $8,411,888.90 |
| TUT/USDT:USDT | +10.19% | $29,876,486.82 |
| H/USDT:USDT | +9.44% | $6,534,862.36 |
| SOXS/USDT:USDT | +8.19% | $5,457,623.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +2.89% | +2.85% |
| APR/USDT:USDT | below_1h_threshold | +2.78% | +2.73% |
| SOXS/USDT:USDT | below_1h_threshold | +2.25% | +2.20% |
| H/USDT:USDT | below_1h_threshold | +2.09% | +2.05% |
| US/USDT:USDT | below_1h_threshold | +1.61% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
