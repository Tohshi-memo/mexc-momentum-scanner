# Decision Report

- generated_at: 2026-11-02T22:31:36.706401+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18038**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18038, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.14% | **-1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_ATR | 17/20 | 85.0% | +1.33% | **+1.13%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.12% | **+1.80%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.70% | **+1.67%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.99% | **+1.39%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.74% | **+1.37%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.28% | **+1.37%** |

## 2. $100 Live Portfolio

- 残高: **$121.86** / 初期 $100.00 (+21.86%)
- 確定トレード: 259件 (TP 96 / SL 155 / EXP 8)
- 最新: BTW/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.86
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,562.92** / 初期 $100.00 (+1462.92%)
- 確定: 6890件 (Win 1998 / Loss 2209 / Flat 2683) / skip 7709件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.22% 残高後 $1,562.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$380.43** / 初期 $100.00 (+280.43%)
- 確定: 4478件 (Win 1203 / Loss 999 / Flat 2276) / skip 6971件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0202 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $380.43

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6199件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000134 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T22:31:19.014843+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=76852.2
- Funnel: target 1093 → liquid 162 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +27.56% | $17,455,545.66 |
| AGT/USDT:USDT | +11.29% | $2,587,880.26 |
| EVAA/USDT:USDT | +11.16% | $6,001,019.83 |
| SOXS/USDT:USDT | +11.12% | $23,573,280.13 |
| JCT/USDT:USDT | +6.48% | $2,120,033.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| Q/USDT:USDT | below_1h_threshold | +2.99% | +2.97% |
| AIN/USDT:USDT | below_1h_threshold | +1.50% | +1.47% |
| AKE/USDT:USDT | below_1h_threshold | +1.19% | +1.16% |
| ALUMINUM/USDT:USDT | below_1h_threshold | +0.41% | +0.39% |
| JCT/USDT:USDT | below_1h_threshold | +0.22% | +0.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
