# Decision Report

- generated_at: 2026-09-05T08:46:36.106390+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13715**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13715, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +0.92% | **+0.83%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.23% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +3.11% | **+1.71%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.53% | **+1.41%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.66% | **+0.91%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.48% | **+0.81%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.55% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 203件 (TP 75 / SL 123 / EXP 5)
- 最新: NIULAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$858.36** / 初期 $100.00 (+758.36%)
- 確定: 5022件 (Win 1517 / Loss 1645 / Flat 1860) / skip 5254件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $858.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.20** / 初期 $100.00 (+88.20%)
- 確定: 2462件 (Win 693 / Loss 586 / Flat 1183) / skip 4664件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0726 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $188.20

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.42** / 初期 $100.00 (+18.42%)
- 確定: 2344件 (Win 700 / Loss 900 / Flat 744) / pending 6件 / skip 2843件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000132 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $118.42

## 6. Latest Market Context

- 更新: 2026-09-05T08:46:22.632806+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=79581.7
- Funnel: target 1050 → liquid 156 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.3 >= 65=1, 4h RSI 77.9 >= 65=1, 4h RSI 70.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +118.20% | $9,984,239.69 |
| 4/USDT:USDT | +71.67% | $17,348,103.07 |
| B/USDT:USDT | +54.19% | $2,115,324.00 |
| NIULAI/USDT:USDT | +40.27% | $1,131,113.10 |
| AKE/USDT:USDT | +30.76% | $14,030,416.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKR/USDT:USDT | below_1h_threshold | +3.31% | +3.42% |
| UAI/USDT:USDT | below_1h_threshold | +3.00% | +3.11% |
| CAKE/USDT:USDT | below_1h_threshold | +2.89% | +3.01% |
| DASH/USDT:USDT | below_1h_threshold | +2.61% | +2.73% |
| EDGE/USDT:USDT | below_1h_threshold | +1.96% | +2.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
