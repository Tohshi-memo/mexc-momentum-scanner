# Decision Report

- generated_at: 2026-11-20T14:31:32.845498+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19245**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19245, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.49% | **-0.24%** |
| LIMIT_2PCT | 15/20 | 75.0% | -0.63% | **-0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.06% | **+0.74%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.83% | **+0.62%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,701.24** / 初期 $100.00 (+1601.24%)
- 確定: 7392件 (Win 2125 / Loss 2381 / Flat 2886) / skip 8414件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KERNEL/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,701.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$440.57** / 初期 $100.00 (+340.57%)
- 確定: 5069件 (Win 1352 / Loss 1087 / Flat 2630) / skip 7587件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0021 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $440.57

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7406件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-20T14:31:19.647733+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=62082.0
- Funnel: target 1087 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KERNEL/USDT:USDT | +38.78% | $1,287,467.48 |
| SOXS/USDT:USDT | +22.20% | $69,758,479.90 |
| CYBER/USDT:USDT | +19.58% | $2,117,901.78 |
| BLESS/USDT:USDT | +18.92% | $18,436,721.95 |
| HUMA/USDT:USDT | +18.91% | $1,414,581.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HUMA/USDT:USDT | below_relative_strength | +5.01% | +4.65% |
| SKY/USDT:USDT | below_1h_threshold | +1.86% | +1.50% |
| BLESS/USDT:USDT | below_1h_threshold | +1.70% | +1.34% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.60% | +1.24% |
| ICNT/USDT:USDT | below_1h_threshold | +1.25% | +0.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
