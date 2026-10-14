# Decision Report

- generated_at: 2026-10-14T04:56:31.764675+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16665**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16665, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.72% | **-0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.20% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.87% | **+0.93%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +3.08% | **+0.92%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.90% | **+0.86%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.31% | **+0.85%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.39% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,278.87** / 初期 $100.00 (+1178.87%)
- 確定: 6296件 (Win 1845 / Loss 2018 / Flat 2433) / skip 6930件
- 成長率目線: 平均log +0.000405 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RSR/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,278.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$270.76** / 初期 $100.00 (+170.76%)
- 確定: 3654件 (Win 1015 / Loss 864 / Flat 1775) / skip 6422件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0121 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGIC/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $270.76

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4824件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000193 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-14T04:56:19.790346+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=83723.2
- Funnel: target 1094 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +30.07% | $31,100,935.39 |
| TRUTH/USDT:USDT | +26.86% | $2,651,855.68 |
| PONS/USDT:USDT | +11.49% | $4,305,294.97 |
| BAT/USDT:USDT | +11.48% | $44,129,068.73 |
| OP/USDT:USDT | +9.51% | $42,387,230.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAT/USDT:USDT | below_1h_threshold | +3.63% | +3.56% |
| PONS/USDT:USDT | below_1h_threshold | +3.16% | +3.09% |
| USELESS/USDT:USDT | below_1h_threshold | +2.99% | +2.92% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.22% | +2.15% |
| CT/USDT:USDT | below_1h_threshold | +1.64% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
