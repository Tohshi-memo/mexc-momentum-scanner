# Decision Report

- generated_at: 2026-09-05T08:31:25.789187+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13714**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13714, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.87% | **+0.78%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.70% | **+1.21%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +2.02% | **+1.11%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.57% | **+0.31%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.39% | **+0.21%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 203件 (TP 75 / SL 123 / EXP 5)
- 最新: NIULAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$858.36** / 初期 $100.00 (+758.36%)
- 確定: 5021件 (Win 1517 / Loss 1645 / Flat 1859) / skip 5254件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $858.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.20** / 初期 $100.00 (+88.20%)
- 確定: 2461件 (Win 693 / Loss 586 / Flat 1182) / skip 4664件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0726 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $188.20

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.42** / 初期 $100.00 (+18.42%)
- 確定: 2343件 (Win 700 / Loss 900 / Flat 743) / pending 5件 / skip 2843件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000269 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $118.42

## 6. Latest Market Context

- 更新: 2026-09-05T08:31:15.268113+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=79584.6
- Funnel: target 1050 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +119.07% | $9,691,809.03 |
| 4/USDT:USDT | +74.85% | $17,235,016.85 |
| B/USDT:USDT | +53.88% | $2,059,105.79 |
| AKE/USDT:USDT | +32.18% | $13,848,261.53 |
| BASECAT/USDT:USDT | +29.03% | $1,615,087.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +4.90% | +5.01% |
| UAI/USDT:USDT | below_1h_threshold | +2.82% | +2.93% |
| DASH/USDT:USDT | below_1h_threshold | +2.54% | +2.65% |
| TAO/USDT:USDT | below_1h_threshold | +1.45% | +1.56% |
| BNB/USDT:USDT | below_1h_threshold | +1.39% | +1.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
