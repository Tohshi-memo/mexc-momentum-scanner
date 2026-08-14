# Decision Report

- generated_at: 2026-08-14T05:16:22.215239+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11505**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11505, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.24% | **-0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.79% | **+1.25%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.84% | **+0.96%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.67% | **+1.50%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.83% | **+1.19%** |
| MARKET_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.65% | **+1.07%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.59% | **+0.87%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$601.25** / 初期 $100.00 (+501.25%)
- 確定: 3982件 (Win 1240 / Loss 1305 / Flat 1437) / skip 4084件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $601.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.94** / 初期 $100.00 (+49.94%)
- 確定: 1650件 (Win 471 / Loss 397 / Flat 782) / skip 3266件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0694 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $149.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.27** / 初期 $100.00 (+16.27%)
- 確定: 1470件 (Win 433 / Loss 556 / Flat 481) / pending 0件 / skip 1505件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000140 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $116.27

## 6. Latest Market Context

- 更新: 2026-08-14T05:16:10.243494+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=63296.3
- Funnel: target 979 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +29.48% | $30,985,144.82 |
| AKE/USDT:USDT | +19.83% | $58,093,915.32 |
| WDAYSTOCK/USDT:USDT | +19.44% | $1,524,557.02 |
| AEON1/USDT:USDT | +19.26% | $1,625,501.82 |
| PROM/USDT:USDT | +18.61% | $2,869,729.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.12% | +4.20% |
| WDAYSTOCK/USDT:USDT | below_1h_threshold | +1.40% | +1.48% |
| MMT/USDT:USDT | below_1h_threshold | +1.39% | +1.47% |
| SYN/USDT:USDT | below_1h_threshold | +1.08% | +1.17% |
| PROM/USDT:USDT | below_1h_threshold | +1.03% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
