# Decision Report

- generated_at: 2026-09-05T02:16:21.278193+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13684**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13684, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_5PCT | 5/20 | 25.0% | -1.03% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.51% | **+2.26%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.53% | **+2.03%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +2.87% | **+1.43%** |
| MARKET_LONG | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.19% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 202件 (TP 75 / SL 122 / EXP 5)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$855.36** / 初期 $100.00 (+755.36%)
- 確定: 5012件 (Win 1516 / Loss 1645 / Flat 1851) / skip 5233件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $855.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.70** / 初期 $100.00 (+89.70%)
- 確定: 2432件 (Win 687 / Loss 578 / Flat 1167) / skip 4663件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1114 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $189.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.73** / 初期 $100.00 (+18.73%)
- 確定: 2318件 (Win 692 / Loss 888 / Flat 738) / pending 3件 / skip 2834件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000425 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.73

## 6. Latest Market Context

- 更新: 2026-09-05T02:16:08.643243+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=79539.8
- Funnel: target 1050 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +64.50% | $12,721,254.93 |
| AKE/USDT:USDT | +37.53% | $7,311,007.29 |
| DASH/USDT:USDT | +26.12% | $32,039,345.46 |
| ZEN/USDT:USDT | +19.38% | $7,481,833.75 |
| BASECAT/USDT:USDT | +17.65% | $1,873,428.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.44% | +3.38% |
| 4/USDT:USDT | below_1h_threshold | +2.29% | +2.22% |
| BTR/USDT:USDT | below_1h_threshold | +1.35% | +1.29% |
| ENJ/USDT:USDT | below_1h_threshold | +1.28% | +1.22% |
| BASECAT/USDT:USDT | below_1h_threshold | +1.25% | +1.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
