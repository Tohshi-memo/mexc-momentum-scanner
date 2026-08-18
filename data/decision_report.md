# Decision Report

- generated_at: 2026-08-18T08:51:32.204117+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11896**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11896, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 13/20 | 65.0% | +1.23% | **+0.80%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.62% | **+0.47%** |
| LIMIT_BB3S | 2/20 | 10.0% | +3.22% | **+0.32%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.33% | **+0.31%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.81% | **+0.98%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.87% | **+0.93%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.91% | **+0.87%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$622.13** / 初期 $100.00 (+522.13%)
- 確定: 4197件 (Win 1295 / Loss 1369 / Flat 1533) / skip 4260件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $622.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1819件 (Win 502 / Loss 427 / Flat 890) / skip 3488件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0005 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.84** / 初期 $100.00 (+17.84%)
- 確定: 1707件 (Win 509 / Loss 648 / Flat 550) / pending 5件 / skip 1656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000309 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $117.84

## 6. Latest Market Context

- 更新: 2026-08-18T08:51:21.946968+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=64232.4
- Funnel: target 992 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PRL/USDT:USDT | +21.79% | $3,032,861.30 |
| CYS/USDT:USDT | +15.30% | $17,927,497.20 |
| RED/USDT:USDT | +15.02% | $2,545,391.35 |
| SOXS/USDT:USDT | +12.74% | $7,779,227.60 |
| ONG/USDT:USDT | +11.79% | $1,026,843.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEMI/USDT:USDT | below_1h_threshold | +4.03% | +3.93% |
| SOXS/USDT:USDT | below_1h_threshold | +1.73% | +1.63% |
| GPS/USDT:USDT | below_1h_threshold | +1.63% | +1.53% |
| OPN/USDT:USDT | below_1h_threshold | +1.17% | +1.08% |
| CAP/USDT:USDT | below_1h_threshold | +1.15% | +1.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
