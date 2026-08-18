# Decision Report

- generated_at: 2026-08-18T02:46:33.126536+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11873**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.88% / filled 20/20。**
- 全期間 MARKET基準: n=11873, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.88% | **+1.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.88% | **+1.88%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.18% | **+1.74%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.42% | **+1.70%** |
| LIMIT_ATR | 9/20 | 45.0% | +2.51% | **+1.13%** |
| LIMIT_3PCT | 9/20 | 45.0% | +2.34% | **+1.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.55% | **+0.70%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.87% | **+0.44%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.89% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$611.63** / 初期 $100.00 (+511.63%)
- 確定: 4187件 (Win 1292 / Loss 1366 / Flat 1529) / skip 4247件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $611.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1819件 (Win 502 / Loss 427 / Flat 890) / skip 3465件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0725 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.67** / 初期 $100.00 (+17.67%)
- 確定: 1685件 (Win 505 / Loss 641 / Flat 539) / pending 6件 / skip 1656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000168 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $117.67

## 6. Latest Market Context

- 更新: 2026-08-18T02:46:19.995833+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=64074.9
- Funnel: target 992 → liquid 181 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIEVERSE/USDT:USDT | +16.16% | $1,824,429.10 |
| ONG/USDT:USDT | +10.49% | $1,058,194.80 |
| H/USDT:USDT | +9.00% | $6,473,804.48 |
| STAR/USDT:USDT | +8.13% | $1,791,414.33 |
| SOXS/USDT:USDT | +7.76% | $4,937,820.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +4.50% | +4.65% |
| STAR/USDT:USDT | below_1h_threshold | +4.44% | +4.59% |
| SOXS/USDT:USDT | below_1h_threshold | +2.70% | +2.86% |
| ACU/USDT:USDT | below_1h_threshold | +1.99% | +2.14% |
| BTW/USDT:USDT | below_1h_threshold | +1.95% | +2.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
